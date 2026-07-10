import cv2
import sqlite3
import numpy as np
import threading
import time
from insightface.app import FaceAnalysis
from datetime import datetime

class AsyncSecureRecognizer:
    def __init__(self):
        print("[INFO] Booting Asynchronous Edge-AI Recognition Engine...")
        # Limiting the AI to only what we need for secure liveness detection
        self.app = FaceAnalysis(name='buffalo_l', allowed_modules=['detection', 'recognition', 'landmark_2d_106'])
        self.app.prepare(ctx_id=0, det_size=(320, 320))
        
        self.db_path = "data/database.db"
        self.known_students = self.load_database()
        self.similarity_threshold = 0.45 
        
        self.liveness_tracker = {}
        self.marked_today = []
        
        # --- MULTITHREADING VARIABLES ---
        self.running = True
        self.latest_frame = None       # The bridge between the camera and the AI
        self.ai_results = []           # Where the AI stores its findings for the UI to draw
        
    def load_database(self):
        print("[INFO] Loading student blueprints from SQLite...")
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, matric_number, embedding FROM Students")
        rows = cursor.fetchall()
        conn.close()
        
        students = []
        for row in rows:
            student_id, name, matric, embedding_blob = row
            embedding_array = np.frombuffer(embedding_blob, dtype=np.float32)
            students.append({
                "id": student_id,
                "name": name,
                "matric": matric,
                "embedding": embedding_array
            })
        print(f"[SUCCESS] Loaded {len(students)} student(s).")
        return students

    def compute_cosine_similarity(self, vec1, vec2):
        dot_product = np.dot(vec1, vec2)
        return dot_product / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

    def calculate_ear(self, landmarks):
        try:
            # Robust method: Grab the entire cluster of points for the left eye (indices 33 to 42)
            left_eye_points = landmarks[33:43]
            
            # Calculate the literal height and width of the eye cluster
            h_dist = np.max(left_eye_points[:, 0]) - np.min(left_eye_points[:, 0])
            v_dist = np.max(left_eye_points[:, 1]) - np.min(left_eye_points[:, 1])
            
            return v_dist / max(h_dist, 0.001)
        except Exception:
            return 1.0 

    def log_attendance(self, student_id, name, matric):
        today_date = datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.now().strftime("%H:%M:%S")
        
        if student_id not in self.marked_today:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Attendance (student_id, date, time, status)
                VALUES (?, ?, ?, ?)
            ''', (student_id, today_date, current_time, "Present"))
            conn.commit()
            conn.close()
            
            self.marked_today.append(student_id)
            print(f"[SECURE ATTENDANCE LOGGED] {name} ({matric}) verified and marked present!")

    # ==========================================
    # THREAD 2: THE BACKGROUND AI ENGINE
    # ==========================================
    def run_ai_loop(self):
        while self.running:
            if self.latest_frame is not None:
                # Grab a snapshot of the current frame to process
                frame_to_process = self.latest_frame.copy()
                faces = self.app.get(frame_to_process)
                
                processed_results = []
                
                for face in faces:
                    bbox = face.bbox.astype(int)
                    live_embedding = face.embedding
                    landmarks = face.landmark_2d_106 if hasattr(face, 'landmark_2d_106') else None
                    
                    best_match_name = "Unknown"
                    best_match_matric = ""
                    highest_similarity = -1.0
                    matched_id = None
                    
                    for student in self.known_students:
                        similarity = self.compute_cosine_similarity(live_embedding, student["embedding"])
                        if similarity > highest_similarity:
                            highest_similarity = similarity
                            if similarity >= self.similarity_threshold:
                                best_match_name = student["name"]
                                best_match_matric = student["matric"]
                                matched_id = student["id"]
                    
                    color = (0, 0, 255)
                    text = "Unknown Face"
                    
                    if best_match_name != "Unknown":
                        # Initialize their personal tracking state
                        if matched_id not in self.liveness_tracker:
                            self.liveness_tracker[matched_id] = {
                                "has_blinked": False, 
                                "personal_baseline": 0.0 # Track their unique eye shape
                            }
                        
                        if landmarks is not None:
                            ear = self.calculate_ear(landmarks)
                            
                            # Constantly update the baseline to the widest their eyes open
                            if ear > self.liveness_tracker[matched_id]["personal_baseline"]:
                                self.liveness_tracker[matched_id]["personal_baseline"] = ear
                            
                            # A blink is when their eyes drop below 70% of their OWN baseline
                            blink_threshold = self.liveness_tracker[matched_id]["personal_baseline"] * 0.70
                            
                            if ear < blink_threshold and self.liveness_tracker[matched_id]["personal_baseline"] > 0.15:  
                                self.liveness_tracker[matched_id]["has_blinked"] = True
                        
                        if self.liveness_tracker[matched_id]["has_blinked"]:
                            color = (0, 255, 0)
                            text = f"VERIFIED: {best_match_name}"
                            self.log_attendance(matched_id, best_match_name, best_match_matric)
                        else:
                            color = (0, 165, 255)
                            text = f"BLINK (Math: {ear:.2f})"

                    
                    # Package the math results and send them back to the UI thread
                    processed_results.append({"bbox": bbox, "color": color, "text": text})
                
                # Update the shared bridge variable securely
                self.ai_results = processed_results
            
            # Brief pause to prevent the CPU from overheating
            time.sleep(0.05)

    # ==========================================
    # THREAD 1: THE MAIN UI & CAMERA FEED
    # ==========================================
    def start_camera(self):
        print("\n=== LAUTECH Secure Edge-AI: Attendance System Active ===")
        
        ai_thread = threading.Thread(target=self.run_ai_loop)
        ai_thread.daemon = True
        ai_thread.start()
        
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        
        # FIX 1: The loop now strictly obeys the self.running flag
        while self.running: 
            ret, frame = cap.read()
            if not ret: break
            
            self.latest_frame = frame
            display_frame = frame.copy()
            
            for result in self.ai_results:
                bbox = result["bbox"]
                color = result["color"]
                text = result["text"]
                
                cv2.rectangle(display_frame, (bbox[0], bbox[1]), (bbox[2], bbox[3]), color, 2)
                cv2.putText(display_frame, text, (bbox[0], bbox[1] - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

            cv2.imshow("Secure Live Attendance Scanner", display_frame)
            
            # FIX 2: Safely handles 'q' OR clicking the "X" on the camera window itself
            if cv2.waitKey(1) & 0xFF == ord('q') or cv2.getWindowProperty("Secure Live Attendance Scanner", cv2.WND_PROP_VISIBLE) < 1:
                print("[INFO] Shutting down camera hardware...")
                self.running = False 
                break

        # This will now successfully execute!
        cap.release()
        cv2.destroyAllWindows()
if __name__ == "__main__":
    recognizer = AsyncSecureRecognizer()
    recognizer.start_camera()