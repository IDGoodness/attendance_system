import cv2
import sqlite3
import numpy as np
from insightface.app import FaceAnalysis

class ModernEnroller:
    def __init__(self):
        print("[INFO] Booting up InsightFace AI engine...")
        # Strictly limiting the AI to bypass the PyInstaller 3D crash and boost speed
        self.app = FaceAnalysis(name='buffalo_l', allowed_modules=['detection', 'recognition'])
        self.app.prepare(ctx_id=0, det_size=(320, 320))
        self.db_path = "data/database.db"

    # New function to check the math
    def compute_cosine_similarity(self, vec1, vec2):
        dot_product = np.dot(vec1, vec2)
        return dot_product / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

    def enroll_student(self, name, matric, dept):
        print(f"\n=== LAUTECH Edge-AI: Enrolling {name} ===")
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        
        # Load existing faces to prevent duplicates
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name, embedding FROM Students")
        existing_students = cursor.fetchall()
        conn.close()

        while True:
            ret, frame = cap.read()
            if not ret: break
                
            display_frame = frame.copy()
            faces = self.app.get(frame)
            
            if len(faces) > 0:
                face = faces[0]
                bbox = face.bbox.astype(int)
                
                cv2.rectangle(display_frame, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 255, 0), 2)
                cv2.putText(display_frame, "Face Detected - Press 's' to Save", (bbox[0], bbox[1] - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            else:
                cv2.putText(display_frame, "No face detected...", (20, 40), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

            cv2.imshow("InsightFace Enrollment", display_frame)
            
            key = cv2.waitKey(1) & 0xFF
            if key == ord('s'):
                if len(faces) > 0:
                    embedding = faces[0].embedding
                    
                    # --- BIOMETRIC DEDUPLICATION CHECK ---
                    is_duplicate = False
                    for existing_name, existing_blob in existing_students:
                        existing_math = np.frombuffer(existing_blob, dtype=np.float32)
                        similarity = self.compute_cosine_similarity(embedding, existing_math)
                        
                        if similarity > 0.45: # The industry threshold for a match
                            print(f"\n[SECURITY ALERT] Enrollment Blocked!")
                            print(f"[REASON] This face is already registered in the system to: {existing_name}")
                            is_duplicate = True
                            break
                    
                    if not is_duplicate:
                        print("[INFO] Unique face verified. Saving to database...")
                        embedding_blob = embedding.tobytes()
                        self.save_to_database(name, matric, dept, embedding_blob)
                    break
                else:
                    print("[WARNING] No face in frame! Cannot save.")
            elif key == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def save_to_database(self, name, matric, dept, embedding_blob):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Students (name, matric_number, embedding, department)
                VALUES (?, ?, ?, ?)
            ''', (name, matric, embedding_blob, dept))
            conn.commit()
            print(f"[SUCCESS] {name} ({matric}) successfully enrolled!")
        except sqlite3.IntegrityError:
            print(f"[ERROR] A student with Matric Number {matric} is already registered.")
        finally:
            conn.close()