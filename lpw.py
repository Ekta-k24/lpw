
#patient class
class Patient:
    def __init__(self, patient_id, name, age, gender):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender

    def display_patient_details(self):
        print(f"Patient ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print("\n")


#hms class
class HospitalManagementSystem:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)
        print(f"Patient {patient.name} added successfully.\n")

    def view_all_patients(self):
        if not self.patients:
            print("No Patients.\n")
        else:
            print("Displaying all patients:\n")
            for patient in self.patients:
                patient.display_patient_details()

    def search_patient_by_id(self, patient_id):
        found = False
        for patient in self.patients:
            if patient.patient_id == patient_id:
                patient.display_patient_details()
                found = True
                break
        if not found:
            print(f"Patient with ID {patient_id} not found.\n")

    def Main():
        hms = HospitalManagementSystem()
        

        while True:
            print("Hospital Management System")
            print("1. Add Patient")
            print("2. View All Patients")
            print("3. Search Patient by ID")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                patient_id = input("Enter Patient ID: ")
                name = input("Enter Patient Name: ")
                age = int(input("Enter Patient Age: "))
                gender = input("Enter Patient Gender: ")
                diagnosis = input("Enter Patient Diagnosis: ")

                new_patient = Patient(patient_id, name, age, gender, diagnosis)
                hms.add_patient(new_patient)

            elif choice == "2":
                hms.view_all_patients()

            elif choice == "3":
                patient_id = input("Enter Patient ID to search: ")
                hms.search_patient_by_id(patient_id)

            elif choice == "4":
                print("Exiting the system...")
                break

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__Main__":
    Main()






# docker commands
#  docker build -t lpw
#  docker run -p 5000:5000 lpw
#  docker ps -a
#  docker stop <conatiner_id>


#git commands
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Ekta-k24/lpw.git
git push -u origin main
