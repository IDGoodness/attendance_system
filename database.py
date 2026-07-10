import sqlite3
import os

class DatabaseManager:
    def __init__(self):
        self.db_dir = "data"
        self.db_path = os.path.join(self.db_dir, "database.db")
        
        if not os.path.exists(self.db_dir):
            os.makedirs(self.db_dir)

    def init_db(self):
        print("[INFO] Initializing SQLite Database...")
        # Connect to SQLite (this automatically creates the file if it doesn't exist)
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Create Students Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                matric_number TEXT UNIQUE NOT NULL,
                embedding BLOB NOT NULL,
                department TEXT
            )
        ''')

        # Create Attendance Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Attendance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER,
                date TEXT,
                time TEXT,
                status TEXT,
                FOREIGN KEY(student_id) REFERENCES Students(id)
            )
        ''')

        conn.commit()
        conn.close()
        print(f"[SUCCESS] Database created securely at: {self.db_path}")

if __name__ == "__main__":
    db = DatabaseManager()
    db.init_db()