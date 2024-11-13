## README: Healthcare Management System with HDU Unit

### Overview

This Healthcare Management System is designed to manage patient records, doctor information, appointments, and a High Dependency Unit (HDU) within a healthcare facility. The system utilizes a SQLite database to store and retrieve data, ensuring efficient and organized healthcare management.

### System Components

#### 1. Database
The system uses a SQLite database named `healthcare_management.db` to store data. The database includes the following tables:
- **patients**: Stores patient information.
- **doctors**: Stores doctor information.
- **appointments**: Stores appointment details.
- **hdu**: Stores data related to the High Dependency Unit.

#### 2. Tables Structure

```sql
CREATE TABLE patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    gender TEXT NOT NULL,
    contact TEXT NOT NULL,
    doctor_name TEXT NOT NULL,
    disease TEXT NOT NULL
);

CREATE TABLE doctors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    specialty TEXT NOT NULL
);

CREATE TABLE appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    doctor_id INTEGER NOT NULL,
    appointment_date TEXT NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES patients (id),
    FOREIGN KEY (doctor_id) REFERENCES doctors (id)
);

CREATE TABLE hdu (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    admission_date TEXT NOT NULL,
    discharge_date TEXT,
    reason_for_admission TEXT NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES patients (id)
);
```

### Functions and Operations

#### 1. Create Tables
The `create_tables` function initializes the database by creating the necessary tables.

#### 2. Insert Data
The `insert_data` function populates the tables with sample data.

#### 3. HDU Management
- **Admit Patient**: The `admit_patient` function allows admitting a patient to the HDU.
- **Update HDU Status**: The `update_hdu_status` function updates the discharge date of a patient in the HDU.
- **Retrieve HDU Patient**: The `retrieve_hdu_patient` function retrieves the HDU record of a specific patient.

### Code Structure

The code is structured into several functions for clarity and maintainability:

```python
import sqlite3
from contextlib import closing

def create_tables(connection):
    # Create tables for patients, doctors, appointments, and HDU
    cursor = connection.cursor()
    # SQL queries to create tables
    connection.commit()

def insert_data(connection):
    # Insert sample data into the tables
    cursor = connection.cursor()
    # SQL queries to insert data
    connection.commit()

def admit_patient(connection, patient_id, admission_date, reason_for_admission):
    # Admit a patient to the HDU
    cursor = connection.cursor()
    cursor.execute("INSERT INTO hdu (patient_id, admission_date, reason_for_admission) VALUES (?, ?, ?)", (patient_id, admission_date, reason_for_admission))
    connection.commit()

def update_hdu_status(connection, hdu_id, discharge_date=None):
    # Update the discharge date of a patient in the HDU
    cursor = connection.cursor()
    if discharge_date:
        cursor.execute("UPDATE hdu SET discharge_date = ? WHERE id = ?", (discharge_date, hdu_id))
    connection.commit()

def retrieve_hdu_patient(connection, patient_id):
    # Retrieve the HDU record of a specific patient
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM hdu WHERE patient_id = ?", (patient_id,))
    return cursor.fetchone()

def main():
    try:
        with closing(sqlite3.connect('healthcare_management.db')) as connection:
            create_tables(connection)
            insert_data(connection)
            # Example usage of HDU management functions
            admit_patient(connection, 3, '2024-11-14', 'Post-operative care')
            update_hdu_status(connection, 1, '2024-11-15')
            patient_hdu_data = retrieve_hdu_patient(connection, 1)
            print("Patient HDU Data:", patient_hdu_data)
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if 'connection' in locals() and connection:
            connection.close()
        if 'cursor' in locals() and cursor:
            cursor.close()

if __name__ == "__main__":
    main()
```

### Usage

1. **Run the Script**: Execute the script to create the database and tables.
2. **Insert Data**: Use the `insert_data` function to populate the tables with sample data.
3. **Manage HDU**: Use the `admit_patient`, `update_hdu_status`, and `retrieve_hdu_patient` functions to manage patients in the HDU.


### Future Enhancements

- **User Interface**: Develop a user-friendly interface to interact with the system.
- **Additional Features**: Implement features for managing prescriptions, medical tests, and other healthcare services.
- **Integration**: Integrate with other healthcare systems to enhance data sharing and interoperability.
