"""
A decorator is a function that takes another function as input, adds some functionality to it, and returns it —
without changing the original function's code.
Think of it as a wrapper around a function.

"""


def outer_func():
    msg = "this is outer function"

    def inner_func():
        print(msg)
    return inner_func()

outer_func()