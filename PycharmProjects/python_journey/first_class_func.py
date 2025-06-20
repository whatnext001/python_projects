"""
A first-class function means that functions in Python are treated like any other variable.
You can:
Assign a function to a variable
Pass a function as an argument
Return a function from another function
📌 Key point: In Python, functions are objects.
"""

def funcky_func (i):
    return i * 3

assign_func = funcky_func

print(assign_func(5))