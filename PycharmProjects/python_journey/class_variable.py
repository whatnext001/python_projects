"""
A class variable is a variable that is shared by all instances (objects) of a class.
It is defined inside the class but outside of any methods.

"""


class Dog:
    # This is a class variable
    species = "Canis familiaris"

    def __init__(self, name):
        self.name = name  # This is an instance variable


# Creating instances
dog1 = Dog("Buddy")
dog2 = Dog("Bella")

print(dog1.species)  # Canis familiaris
print(dog2.species)  # Canis familiaris
