from colorama import init, Fore

init(autoreset=True)


class Patient:
    def __init__(self, name, age, id_number):
        self.name = name
        self.age = age
        self.id_number = id_number


class InPatient(Patient):
    def __init__(self, name, age, id_number, room_number, admission_date, discharge_date):
        super().__init__(name, age, id_number)
        self.room_number = room_number
        self.admission_date = admission_date
        self.discharge_date = discharge_date

    def days_admitted(self):
        days = self.discharge_date - self.admission_date
        return f"{Fore.RED}The number of days admitted is {days} days"


class OutPatient(Patient):
    def __init__(self, name, age, id_number, appointment_date, doctor_name):
        super().__init__(name, age, id_number)
        self.appointment_date = appointment_date
        self.doctor_name = doctor_name


patient_1 = InPatient("hammed",25,"PAT101","Room 20", 2,10)

print(patient_1.days_admitted())