"""
An attribute is turned into a method using the @property decorator
so you can add logic (like validation or computation)
while still using simple attribute-like syntax.

Property decorator allows us to define a method and access it like an attribute.

"""

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):  # method acting like an attribute which is achieved with the use of @property
        print("Accessing name...")
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        print("Setting name...")
        self._name = value

user_1 = Person("Damilare")

#print (user1.name()) will thrown an error because this has been called with @property and no longer a method


print(user_1.name)


"""Using the deletter property"""
class Secret:
    def __init__(self, code):
        self._code = code

    @property
    def code(self):
        return self._code

    @code.deleter
    def code(self):
        print("Deleting code...")
        del self._code

s = Secret("1234")
print(s.code)
del s.code

