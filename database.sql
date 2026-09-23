-- SQLite Database Schema Definition
-- Location: data/database.db

PRAGMA foreign_keys = ON;

-- 1. Students Master Demographic & Biometric Table
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    matric_no TEXT UNIQUE NOT NULL,
    department TEXT NOT NULL,
    embedding BLOB NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Attendance Transaction Log Table
CREATE TABLE IF NOT EXISTS attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT DEFAULT 'Present',
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE
);

-- Index optimization for real-time querying
CREATE INDEX IF NOT EXISTS idx_matric ON students(matric_no);
CREATE INDEX IF NOT EXISTS idx_attendance_date ON attendance(timestamp);