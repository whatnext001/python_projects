class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    pass


dog_spec = Dog()

print(dog_spec.speak())


class Animal:
    def speak(self):
        return "Some sound"

class Cat(Animal):
    def speak(self):
        return "Meow"

cat_spec = Cat()
anime = Animal()
print(cat_spec.speak())
print(anime.speak())



class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        # Initialize parent class
        super().__init__(brand)
        self.model = model

object_1 = Car("toyota","corolla")
print(object_1.brand)
print(object_1.model)