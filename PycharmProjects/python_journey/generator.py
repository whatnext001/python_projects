"""
Generators are special functions in Python that allow you to iterate over data lazily — that is,
they generate values one at a time only when needed.
This is more memory-efficient than storing everything in a list.
Generators are written like regular functions but use the **yield** keyword instead of return.

Iterating over large datasets/files
Instead of reading all lines into memory:

def read_lines(filepath):
    with open(filepath) as f:
        for line in f:
            yield line


"""
list_value = [1,2,3,4,5]

def square_root():
    output = [num * num for num in list_value]

    print(output)

square_root()



gen = (x * x for x in range(5)) #Just like list comprehensions, but with **()instead of[]`.
for val in gen:
    print(val)



count_up_to = (nums for nums in range(1,4))

print(next(count_up_to)) #next prints out the next items to be displayed
print(next(count_up_to))
print(next(count_up_to))