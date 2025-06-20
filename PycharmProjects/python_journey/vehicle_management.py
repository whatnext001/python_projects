"""You're building a transport management system."""

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"This vehicle details are {self.make} maker,{self.model} model,{self.year} year"

    def start_engine(self):
        print("Starting engine...")


"""The sub classes are defined below"""


class Car(Vehicle):  # subclass car
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):  # This calls the display_info() method of the parent class (Vehicle).
        super().display_info()
        print(f"the car has a number of {self.num_doors} doors ")

    def start_engine(self):
        print("The car is now starting....")



class Truck(Vehicle):  # subclass vehicle
    def __init__(self, make, model, year, load_capacity):
        super().__init__(make, model, year)
        self.load_capacity = load_capacity

    def display_info(self):
        super().display_info()
        print(f"the model of this car is {self.model}")

    def start_engine(self):
        print("The Truck key has been inserted...")


class Motorcycle(Vehicle):  # subclass motorcycle
    def __init__(self, make, model, year, has_sidecar):
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar

    def display_info(self):
        super().display_info()
        print(f"The motorcycle is of the year {self.year}")

    def start_engine(self):
        print("The Motorcycle is now in motion...")


# object instances
obj_car = Car("Toyota","siena","2023",4)
obj_truck = Truck("Nissan","new","2024",500)
obj_motor = Motorcycle("Bajaj","china","2018","yes")

# creating a list
vehicle = [obj_car,obj_truck,obj_motor]

for items in vehicle:
    items.display_info()
    items.start_engine()
    print("***" * 12)



