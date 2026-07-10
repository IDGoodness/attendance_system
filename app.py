import customtkinter as ctk
from tkinter import ttk, messagebox
import threading
import sqlite3
import sys
import os
import multiprocessing

from enroll import ModernEnroller
from recognize import AsyncSecureRecognizer
from export_data import DataExporter
from database import DatabaseManager  # <--- NEW IMPORT

# --- PYINSTALLER CRASH PREVENTION & PATH FIX ---
if getattr(sys, 'frozen', False):
    # 1. Figure out exactly where the .exe is sitting on the Windows machine
    application_path = os.path.dirname(sys.executable)
    
    # 2. Force the app to strictly operate inside that folder
    os.chdir(application_path) 
    
    # 3. The "Black Hole" telemetry patch
    log_path = os.path.join(application_path, "admin_system_log.txt")
    sys.stdout = open(log_path, "a")
    sys.stderr = sys.stdout

# --- SELF-HEALING DATABASE ---
# Guarantee the 'data' folder and SQLite schema exist before the UI is allowed to boot
db_manager = DatabaseManager()
db_manager.init_db()

# Configure the modern aesthetic
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class AdminDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- WINDOW CONFIGURATION ---
        self.title("Edge-AI Attendance System")
        self.geometry("700x550") # Expanded for the admin grid
        self.resizable(False, False)
        
        # Capture the "X" button click for a graceful shutdown
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.db_path = "data/database.db"
        self.recognizer_instance = None # Track the camera instance so we can kill it safely

        # --- UI HEADER ---
        self.title_label = ctk.CTkLabel(self, text="Edge-AI Attendance System", font=ctk.CTkFont(size=24, weight="bold"))
        self.title_label.pack(pady=(20, 5))

        self.subtitle_label = ctk.CTkLabel(self, text="Dept. of Computer Science, LAUTECH", font=ctk.CTkFont(size=14), text_color="gray")
        self.subtitle_label.pack(pady=(0, 15))

        # --- TABBED INTERFACE ---
        self.tabview = ctk.CTkTabview(self, width=650, height=350)
        self.tabview.pack(padx=20, pady=5, fill="both", expand=True)
        
        self.tabview.add("System Operations")
        self.tabview.add("Database Admin")

        self.setup_operations_tab()
        self.setup_database_tab()

        # Status Bar
        self.status_label = ctk.CTkLabel(self, text="System Status: Ready", font=ctk.CTkFont(size=12))
        self.status_label.pack(side="bottom", pady=10)

    # ==========================================
    # TAB 1: SYSTEM OPERATIONS
    # ==========================================
    def setup_operations_tab(self):
        ops_frame = self.tabview.tab("System Operations")
        
        self.btn_enroll = ctk.CTkButton(
            ops_frame, text="1. Enroll New Student", command=self.open_enrollment_window, 
            width=250, height=45, font=ctk.CTkFont(size=15, weight="bold")
        )
        self.btn_enroll.pack(pady=25)

        self.btn_recognize = ctk.CTkButton(
            ops_frame, text="2. Start Live Scanner", command=self.launch_recognize, 
            width=250, height=45, font=ctk.CTkFont(size=15, weight="bold"), 
            fg_color="#28a745", hover_color="#218838"
        )
        self.btn_recognize.pack(pady=10)

        self.btn_export = ctk.CTkButton(
            ops_frame, text="3. Export Attendance Report", command=self.launch_export, 
            width=250, height=45, font=ctk.CTkFont(size=15, weight="bold"), 
            fg_color="#ffc107", text_color="black", hover_color="#e0a800"
        )
        self.btn_export.pack(pady=25)

    # ==========================================
    # TAB 2: DATABASE ADMIN (VIEW & DELETE)
    # ==========================================
    def setup_database_tab(self):
        db_frame = self.tabview.tab("Database Admin")
        
        # Style the data grid to match the dark theme
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", background="#2b2b2b", foreground="white", rowheight=25, fieldbackground="#2b2b2b")
        style.map('Treeview', background=[('selected', '#1f538d')])
        
        # Create the Data Grid
        columns = ("ID", "Name", "Matric Number", "Department")
        self.tree = ttk.Treeview(db_frame, columns=columns, show='headings', height=10)
        
        # Format the columns
        self.tree.heading("ID", text="ID")
        self.tree.column("ID", width=50, anchor="center")
        
        self.tree.heading("Name", text="Full Name")
        self.tree.column("Name", width=200)
        
        self.tree.heading("Matric Number", text="Matric Number")
        self.tree.column("Matric Number", width=150, anchor="center")
        
        self.tree.heading("Department", text="Department")
        self.tree.column("Department", width=150)
        
        self.tree.pack(fill="both", expand=True, padx=10, pady=(10, 0))
        
        # Admin Buttons Frame
        btn_frame = ctk.CTkFrame(db_frame, fg_color="transparent")
        btn_frame.pack(fill="x", pady=10, padx=10)
        
        ctk.CTkButton(btn_frame, text="Refresh Data", command=self.load_students, width=120).pack(side="left")
        ctk.CTkButton(btn_frame, text="Delete Selected Student", command=self.delete_student, width=150, fg_color="#dc3545", hover_color="#c82333").pack(side="right")
        
        # Populate the table initially
        self.load_students()

    def load_students(self):
        # Clear existing rows
        for row in self.tree.get_children():
            self.tree.delete(row)
            
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, matric_number, department FROM Students ORDER BY id DESC")
            for row in cursor.fetchall():
                self.tree.insert("", "end", values=row)
            conn.close()
        except Exception as e:
            print(f"Database error: {e}")

    def delete_student(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please click on a student to delete.")
            return
            
        # Extract the data from the selected row
        item_values = self.tree.item(selected_item[0])['values']
        student_id = item_values[0]
        student_name = item_values[1]
        
        # Pop a confirmation dialog before doing destructive actions
        confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to permanently delete {student_name}?\n\nThis will also delete all their attendance records.")
        
        if confirm:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            # Cascade delete: Remove attendance records first, then the student
            cursor.execute("DELETE FROM Attendance WHERE student_id = ?", (student_id,))
            cursor.execute("DELETE FROM Students WHERE id = ?", (student_id,))
            conn.commit()
            conn.close()
            
            self.load_students()
            self.status_label.configure(text=f"System Status: {student_name} deleted successfully.", text_color="#28a745")

    # ==========================================
    # LOGIC WRAPPERS & SHUTDOWN HANDLING
    # ==========================================
    def open_enrollment_window(self):
        self.enroll_window = ctk.CTkToplevel(self)
        self.enroll_window.title("Student Enrollment Form")
        self.enroll_window.geometry("400x350")
        self.enroll_window.attributes("-topmost", True) 
        
        ctk.CTkLabel(self.enroll_window, text="Enter Student Details", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=20)
        
        self.name_entry = ctk.CTkEntry(self.enroll_window, placeholder_text="Full Name", width=300)
        self.name_entry.pack(pady=10)
        
        self.matric_entry = ctk.CTkEntry(self.enroll_window, placeholder_text="Matric Number", width=300)
        self.matric_entry.pack(pady=10)
        
        self.dept_entry = ctk.CTkEntry(self.enroll_window, placeholder_text="Department", width=300)
        self.dept_entry.pack(pady=10)
        
        ctk.CTkButton(self.enroll_window, text="Open Camera & Enroll", command=self.process_enrollment).pack(pady=25)

    def process_enrollment(self):
        name = self.name_entry.get()
        matric = self.matric_entry.get()
        dept = self.dept_entry.get()
        
        if not name or not matric or not dept:
            self.status_label.configure(text="System Status: Error - All fields required!", text_color="#dc3545")
            return
            
        self.enroll_window.destroy()
        self.status_label.configure(text=f"System Status: Booting camera for {name}...", text_color="white")
        
        def run_ai():
            enroller = ModernEnroller()
            enroller.enroll_student(name, matric, dept)
            self.status_label.configure(text="System Status: Enrollment Complete / Ready")
            self.load_students() # Automatically refresh the admin grid!
            
        threading.Thread(target=run_ai, daemon=True).start()

    def launch_recognize(self):
        self.status_label.configure(text="System Status: Initializing Live Scanner...")
        def run_ai():
            self.recognizer_instance = AsyncSecureRecognizer()
            self.recognizer_instance.start_camera()
            self.status_label.configure(text="System Status: Scanner Closed / Ready")
            self.recognizer_instance = None
            
        threading.Thread(target=run_ai, daemon=True).start()

    def launch_export(self):
        self.status_label.configure(text="System Status: Exporting CSV...")
        def run_export():
            exporter = DataExporter()
            exporter.export_to_csv()
            self.status_label.configure(text="System Status: Report saved to data/attendance_logs!", text_color="#28a745")
            
        threading.Thread(target=run_export, daemon=True).start()

    def on_closing(self):
        print("[INFO] Shutting down application gracefully...")
        
        # 1. Signal the camera loop to break
        if self.recognizer_instance:
            self.recognizer_instance.running = False 
            
            # Give OpenCV exactly half a second to release the physical hardware
            import time
            time.sleep(0.5) 
            
        # 2. Destroy the UI and forcefully kill all background processes
        self.destroy()
        os._exit(0) # os._exit is safer than sys.exit for hardware threads

if __name__ == "__main__":
    # Required for Windows .exe files handling heavy AI threads
    multiprocessing.freeze_support() 
    app = AdminDashboard()
    app.mainloop()