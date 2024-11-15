import sqlite3

# Connect to the database
conn = sqlite3.connect('healthcare.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Patients (
        PatientID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        DOB TEXT NOT NULL,
        Address TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Doctors (
        DoctorID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Specialization TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Appointments (
        AppointmentID INTEGER PRIMARY KEY,
        PatientID INTEGER NOT NULL,
        DoctorID INTEGER NOT NULL,
        AppointmentTime TEXT NOT NULL,
        FOREIGN KEY (PatientID) REFERENCES Patients (PatientID),
        FOREIGN KEY (DoctorID) REFERENCES Doctors (DoctorID)
    )
''')

conn.commit()
conn.close()