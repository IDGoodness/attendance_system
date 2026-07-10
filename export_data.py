import sqlite3
import csv
import os
from datetime import datetime

class DataExporter:
    def __init__(self):
        self.db_path = "data/database.db"
        self.export_dir = "data/attendance_logs"
        
        # Ensure the output directory exists
        if not os.path.exists(self.export_dir):
            os.makedirs(self.export_dir)

    def export_to_csv(self):
        print("=== LAUTECH Admin: Generate Attendance Report ===")
        print("[INFO] Connecting to secure database...")
        
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            # Perform an SQL JOIN to combine the Student details with their exact check-in times
            query = '''
                SELECT Attendance.date, Attendance.time, Students.name, 
                       Students.matric_number, Students.department, Attendance.status
                FROM Attendance
                JOIN Students ON Attendance.student_id = Students.id
                ORDER BY Attendance.date DESC, Attendance.time DESC
            '''
            cursor.execute(query)
            records = cursor.fetchall()

            if not records:
                print("[WARNING] The database is empty. No attendance records to export.")
                return

            # Generate a unique filename based on the exact second the report is pulled
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"Attendance_Report_{timestamp}.csv"
            filepath = os.path.join(self.export_dir, filename)

            # Write the data into a structured CSV file
            with open(filepath, mode='w', newline='') as file:
                writer = csv.writer(file)
                # Write the column headers
                writer.writerow(["Date", "Time", "Student Name", "Matric Number", "Department", "Status"])
                # Write all the rows of data
                writer.writerows(records)

            print(f"[SUCCESS] Beautifully formatted report generated!")
            print(f"[SUCCESS] {len(records)} records saved to: {filepath}")
            
        except Exception as e:
            print(f"[ERROR] Failed to export data: {e}")
        finally:
            if conn:
                conn.close()

if __name__ == "__main__":
    exporter = DataExporter()
    exporter.export_to_csv()