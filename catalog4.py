class Child:
    def __init__(self, name, age):  # Corrected __init__ method
        self.name = name
        self.age = age
        self.vaccinations = []

    def add_vaccination(self, vaccination):
        self.vaccinations.append(vaccination)

    def get_vaccinations(self):
        return self.vaccinations


class Vaccination:
    def __init__(self, vaccine, date):  # Corrected __init__ method
        self.vaccine = vaccine
        self.date = date


class Appointment:
    def __init__(self, name, date, vaccine):  # Corrected __init__ method
        self.name = name
        self.date = date
        self.vaccine = vaccine


class VaccinationManagementSystem:
    def __init__(self):  # Corrected __init__ method
        self.records = {}
        self.appointments = []

    def add_child(self, name, age):
        if name in self.records:
            print(f"Record for {name} already exists.")
        else:
            self.records[name] = Child(name, age)
            print(f"Record for {name} added.")

    def schedule_vaccination(self, name, date, vaccine):
        if name not in self.records:
            print(f"No record for {name}. Add the child first.")
        else:
            self.appointments.append(Appointment(name, date, vaccine))
            print(f"Appointment for {name} scheduled on {date} for {vaccine}.")

    def view_appointments(self):
        if not self.appointments:
            print("No upcoming appointments.")
        else:
            for app in self.appointments:
                print(f"{app.name} - {app.vaccine} on {app.date}")

    def update_vaccination_record(self, name, vaccine, date):
        if name in self.records:
            self.records[name].add_vaccination(Vaccination(vaccine, date))
            print(f"Record updated for {name} with {vaccine} on {date}.")
        else:
            print(f"No record found for {name}.")

    def view_vaccination_record(self, name):
        if name in self.records:
            vaccinations = self.records[name].get_vaccinations()
            if not vaccinations:
                print("No vaccinations recorded.")
            else:
                for v in vaccinations:
                    print(f"{v.vaccine} on {v.date}")
        else:
            print(f"No record found for {name}.")


def main():
    system = VaccinationManagementSystem()

    while True:
        print("\nChild Vaccination Management System")
        print("1. Add Child\n2. Schedule Vaccination\n3. View Appointments\n4. Update Record\n5. View Record\n6. Exit")
        choice = int(input("Select an option: "))

        if choice == 1:
            name = input("Enter child's name: ")
            age = int(input("Enter child's age: "))
            system.add_child(name, age)
        elif choice == 2:
            name = input("Enter child's name: ")
            date = input("Enter vaccination date (YYYY-MM-DD): ")
            vaccine = input("Enter vaccine name: ")
            system.schedule_vaccination(name, date, vaccine)
        elif choice == 3:
            system.view_appointments()
        elif choice == 4:
            name = input("Enter child's name: ")
            vaccine = input("Enter vaccine name: ")
            date = input("Enter vaccination date (YYYY-MM-DD): ")
            system.update_vaccination_record(name, vaccine, date)
        elif choice == 5:
            name = input("Enter child's name: ")
            system.view_vaccination_record(name)
        elif choice == 6:
            print("Exiting the system.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
