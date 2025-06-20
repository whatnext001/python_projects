from collections import namedtuple

"""
A namedtuple is a special type of Python object that allows you to create simple classes for storing data. 
It’s similar to a regular tuple, but with named fields that you can access 
using attribute-style access instead of indexing. Namedtuples are immutable, 
meaning their contents cannot be changed once they're created, 
but they are more readable and accessible than regular tuples.
"""

human = namedtuple("person",["name","age"]) #this is creating the tuple with the namedtuple builtin keyword

Person = human(name= "John", age=35)

print(Person.name)
print(Person.age)


