class Human:
    def __init__(self,color,race,language):
        self.color = color
        self.race = race
        self.language = language

    def african(self):
        return f"The human race differs based on {self.color},{self.race},{self.language}"

    def european(self):
        return f"The human race differs based on {self.color},{self.race},{self.language}"

    def asian(self):
        return f"The human race differs based on {self.color},{self.race},{self.language}"

afric_human = Human("black", "human","efik")

print(afric_human.european())

class Company:
    def __init__(self,name,email,department,salary):
        self.name = name
        self.email = email + "@gmail.com"
        self.department = department
        self.salary = salary
    def dep_finance(self):
        return f"{self.name}  with email id {self.email} belongs to the {self.department} and earns {self.salary}"

    def dep_logistics(self):
        return f"{self.name} belongs to the {self.department} and earns {self.salary}"

class Offsite_company(Company):
    def __init__(self,name,email,department,salary,location):
        super().__init__(name,email,department,salary)
        self.location = location


    def off_location(self):
        return f"{self.name} is a staff from {self.location} and earns {self.salary}"

user_1 = Company("Adeleke","adamilare206","security","$500,000")
user_2 = Offsite_company("new","user","account","#300,000,000","USA")

print(user_1.dep_finance())
print(user_2.off_location())
