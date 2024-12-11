import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from dotenv import load_dotenv
import os
load_dotenv()
database_url = os.getenv("DATABASE_URL")
storage_bucket = os.getenv("STORAGE_BUCKET")
firebase_credentials = os.getenv("FIREBASE_CREDENTIALS")

# Initialize Firebase Admin SDK
cred = credentials.Certificate(firebase_credentials)
firebase_admin.initialize_app(cred, {
    'databaseURL': database_url,
})

# Reference to 'Students' node in the database
ref = db.reference('Students')

# Student Data to Upload
data = {
    "1235": {
        "name": "Barack Obama",
        "major": "Msc",
        "starting_year": 2014,
        "total_attendance": 8,
        "standing": "G",
        "year": 4,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "12346": {
        "name": "Jon Snow",
        "major": "CG",
        "starting_year": 2019,
        "total_attendance": 9,
        "standing": "E",
        "year": 4,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "123456": {
        "name": "Dibyansu Mishra",
        "major": "CSE",
        "starting_year": 2017,
        "total_attendance": 6,
        "standing": "G",
        "year": 4,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "22057031": {
        "name": "HaraPrasad Pradhan",
        "major": "CSE",
        "starting_year": 2022,
        "total_attendance": 0,
        "standing": "B",
        "year": 4,
        "last_attendance_time": "2022-12-11 00:00:00"
    }
}

# Upload Data to Firebase
try:
    for key, value in data.items():
        ref.child(key).set(value)
    print("Student data successfully uploaded to Firebase!")
except Exception as e:
    print(f"Error uploading data: {e}")
