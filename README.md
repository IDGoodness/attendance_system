# LAUTECH Edge-AI Attendance System

LAUTECH Edge-AI Attendance System is a Windows desktop attendance app built with Python, CustomTkinter, OpenCV, SQLite, and InsightFace. It supports face-based student enrollment, live attendance recognition with blink-based liveness checking, student database administration, and CSV attendance export.

## Features

- Student enrollment with webcam face capture
- Duplicate face checking during enrollment
- Live attendance scanning with face recognition
- Blink/liveness verification before marking attendance
- SQLite-backed student and attendance storage
- Database admin view for refreshing and deleting students
- CSV export of attendance logs
- PyInstaller packaging into a standalone `.exe`

## Project Structure

- `app.py` - main desktop dashboard and app entry point
- `database.py` - creates and initializes the SQLite database
- `enroll.py` - handles student enrollment and face embedding capture
- `recognize.py` - runs live recognition and attendance logging
- `export_data.py` - exports attendance records to CSV
- `data/` - database and generated attendance reports
- `students/` - reserved for student-related assets if needed

## Requirements

- Windows 10/11
- Python 3.10 or newer
- Webcam
- Git

Python packages used by the app:

- `customtkinter`
- `insightface`
- `opencv-python`
- `numpy`
- `pyinstaller` for building the executable

## Installation

### 1. Pull the latest code

If you already have the repository cloned, open a terminal in the project folder and pull the latest changes:

```bash
git pull origin main
```

If you do not have the project yet, clone it first:

```bash
git clone <your-repository-url>
cd attendance_system
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install customtkinter insightface opencv-python numpy pyinstaller
```

If InsightFace asks for an ONNX runtime backend, install it as well:

```bash
pip install onnxruntime
```

### 4. Initialize the database

The database is created automatically when the app starts, but you can also initialize it manually:

```bash
python database.py
```

This creates `data/database.db` and the required `Students` and `Attendance` tables.

## Running the App

Start the desktop application with:

```bash
python app.py
```

When the dashboard opens, you can:

- Enroll a new student using the webcam
- Start live attendance recognition
- Export attendance records to CSV
- View and delete students from the built-in admin table

## Generating the EXE File

This project already includes a PyInstaller spec file: `LAUTECH_Attendance.spec`.

### Build using the spec file

```bash
pyinstaller LAUTECH_Attendance.spec
```

### Or build directly from the app entry point

```bash
pyinstaller --noconsole --name "LAUTECH_Attendance" --collect-all customtkinter --collect-all insightface app.py
```

After the build completes, the distributable app will be available in the `dist\LAUTECH_Attendance\` folder.

## Output Files

- SQLite database: `data/database.db`
- Attendance CSV exports: `data/attendance_logs/Attendance_Report_YYYYMMDD_HHMMSS.csv`
- Executable output: `dist\LAUTECH_Attendance\`

## Notes

- The app uses the webcam, so make sure no other program is blocking camera access.
- Enrollment and recognition depend on face visibility and lighting quality.
- On first launch, the database folder is created automatically if it does not already exist.
- The packaged executable writes its log output to `admin_system_log.txt` in the same folder as the `.exe`.

## Troubleshooting

- If the camera does not open, close other apps that are using the webcam and try again.
- If PyInstaller fails on InsightFace or OpenCV assets, rebuild using the provided spec file.
- If you get a missing module error after cloning, confirm that your virtual environment is activated before running the install commands.

## License

Add your project license here if you plan to distribute the code publicly.