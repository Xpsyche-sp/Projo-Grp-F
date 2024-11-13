# Class to represent a Patient
class Patient:
    def __init__(self, patient_id, name, age, gender, medical_history):
        # Initialize the patient with the given attributes
        self.patient_id = patient_id          # Unique identifier for the patient
        self.name = name                      # Patient's name
        self.age = age                        # Patient's age
        self.gender = gender                  # Patient's gender
        self.medical_history = medical_history # Patient's medical history

    def __str__(self):
        # String representation of the patient object
        return f"ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Medical History: {self.medical_history}"


# Class to manage the health records
class HealthManagementSystem:
    def __init__(self):
        # Initialize a dictionary to store patients, using patient_id as the key
        self.patients = {}

    def add_patient(self, patient):
        # Add a new patient to the system
        self.patients[patient.patient_id] = patient
        print(f"Patient {patient.name} added successfully.")

    def view_patient(self, patient_id):
        # View the details of a specific patient by their ID
        patient = self.patients.get(patient_id)  # Retrieve patient from dictionary
        if patient:
            print(patient)  # Print patient details if found
        else:
            print("Patient not found.")  # Inform if the patient does not exist

    def update_patient(self, patient_id, name=None, age=None, gender=None, medical_history=None):
        # Update the details of an existing patient
        patient = self.patients.get(patient_id)  # Retrieve patient from dictionary
        if patient:
            # Update attributes only if new values are provided
            if name:
                patient.name = name
            if age:
                patient.age = age
            if gender:
                patient.gender = gender
            if medical_history:
                patient.medical_history = medical_history
            print(f"Patient {patient_id} updated successfully.")
        else:
            print("Patient not found.")  # Inform if the patient does not exist

    def delete_patient(self, patient_id):
        # Delete a patient from the system
        if patient_id in self.patients:
            del self.patients[patient_id]  # Remove the patient from the dictionary
            print(f"Patient {patient_id} deleted successfully.")
        else:
            print("Patient not found.")  # Inform if the patient does not exist

    def list_patients(self):
        # List all patients in the system
        if not self.patients:
            print("No patients found.")  # Inform if there are no patients
        else:
            for patient in self.patients.values():
                print(patient)  # Print details of each patient


def main():
    # Create an instance of the health management system
    hms = HealthManagementSystem()

    while True:
        # Display the menu options to the user
        print("\nHealth Management System")
        print("1. Add Patient")
        print("2. View Patient")
        print("3. Update Patient")
        print("4. Delete Patient")
        print("5. List Patients")
        print("6. Exit")

        # Get user choice
        choice = input("Enter your choice: ")

        if choice == '1':
            # Add a new patient
            patient_id = input("Enter Patient ID: ")
            name = input("Enter Patient Name: ")
            age = input("Enter Patient Age: ")
            gender = input("Enter Patient Gender: ")
            medical_history = input("Enter Medical History: ")
            patient = Patient(patient_id, name, age, gender, medical_history)  # Create a new Patient object
            hms.add_patient(patient)  # Add the patient to the system

        elif choice == '2':
            # View details of a patient
            patient_id = input("Enter Patient ID to view: ")
            hms.view_patient(patient_id)  # Call method to view patient details

        elif choice == '3':
            # Update an existing patient's details
            patient_id = input("Enter Patient ID to update: ")
            name = input("Enter new name (leave blank to keep current): ")
            age = input("Enter new age (leave blank to keep current): ")
            gender = input("Enter new gender (leave blank to keep current): ")
            medical_history = input("Enter new medical history (leave blank to keep current): ")
            # Call method to update patient details, using None for blank inputs
            hms.update_patient(patient_id, name or None, age or None, gender or None, medical_history)
