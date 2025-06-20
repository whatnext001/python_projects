"""
✅ What is a Class?
A class is like a blueprint for creating objects.
Think of it like a recipe for baking a cake—it defines
what a cake is and how to make it, but it’s not a cake itself.

✅ What is an Instance?
An instance is an object created using the class.
It's like the actual cake you bake using the recipe.

✅ The __init__() Method
This special method is called a constructor.
It automatically runs when a new object is created.

 (self)
self refers to the instance of the class that calls the method.

It allows the method to access or modify attributes (variables)
and other methods belonging to the specific object.

You must include self as the first parameter in any method
inside a class (unless it’s a @staticmethod).
"""


class Parent:
    def __init__(self,mum,dad):
        self.mum = mum
        self.dad = dad
    def granny(self,age,hair_color):
        self.age = 100
        self.hair_color = "grey"
        if self.age > 10:
            print("this is an old man")
        else:
            print("not that old enough")


yoruba_parent = Parent("maaami","baaami")
print(yoruba_parent.dad,yoruba_parent.mum)

german_parent = Parent("vatter","mutter")
print(german_parent.mum,german_parent.dad)

yoruba_parent.granny(100,"blue")


class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f"The car brand is {self.brand} and the model is {self.model}, which is build in {self.year} year"
    def update_year(self,new_year):
        self.new_year = new_year
        return f"The latest car year is {self.new_year}"

car_brand_1 = Car("Toyota","RAV4","2023")
car_brand_2 = Car("Minicooper","Min005","2025")

print(car_brand_1.display_info())
print(car_brand_2.display_info())



class Person:
    def __init__(self,name, age=14):
        self.name = name
        self.age = age
    def greet(self):
        return f"Hello, my name is {self.name} and i am {self.age} years old."

human_1 = Person("Olaide", 14)

print(human_1.greet())


class Bank_Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.amount = amount
        return f"{self.owner} has made a deposit of {self.amount}"

    def withdraw(self,w_amount):
        self.w_amount = w_amount
        return f"{self.owner} has withdrawn {self.w_amount}"

    def display_balance(self):
        return f"{self.owner} has a balance of {self.balance} left in his or her account"

customer_1 = Bank_Account("Tomiwa","#500,00")

print(customer_1.deposit(300000))
