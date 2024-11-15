class HealthDataRepository:
    def __init__(self):
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, data):
        for observer in self.observers:
            observer.update(data)

class Observer:
    def update(self, data):
        pass

class MedicalTeam(Observer):
    def update(self, data):
        print("Medical Team received update:", data)

# Usage
repository = HealthDataRepository()
medical_team = MedicalTeam()
repository.register_observer(medical_team)
repository.notify_observers("Patient's health data updated")