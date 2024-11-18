# Class representing the subject being observed.
# In this case, it is a HealthDataRepository.
class HealthDataRepository:
    def __init__(self):
        # Initialize an empty list to store observers.
        self.observers = []

    def register_observer(self, observer):
        # Method to add an observer to the list.
        # Check if the observer is not already in the list to avoid duplicates.
        if observer not in self.observers:
            self.observers.append(observer)

    def notify_observers(self, data):
        # Method to notify all registered observers about a change.
        # Iterate through the list of observers and call their update method.
        for observer in self.observers:
            observer.update(data)


# Base class for observers.
# This class defines the interface that all observers must implement.
class Observer:
    def update(self, data):
        # This method must be implemented by any concrete observer.
        # It is called by the subject when there is an update.
        pass


# Concrete observer class.
# This class represents a specific observer, in this case, a MedicalTeam.
class MedicalTeam(Observer):
    def update(self, data):
        # Implementation of the update method for MedicalTeam.
        # Here, it simply prints the received update.
        print("Medical Team received update:", data)


# Usage example
if __name__ == "__main__":
    # Create an instance of the HealthDataRepository (the subject).
    repository = HealthDataRepository()
    
    # Create an instance of the MedicalTeam (the observer).
    medical_team = MedicalTeam()
    
    # Register the MedicalTeam as an observer of the HealthDataRepository.
    repository.register_observer(medical_team)
    
    # Notify all observers about a change in the health data.
    repository.notify_observers("Patient's health data updated")
