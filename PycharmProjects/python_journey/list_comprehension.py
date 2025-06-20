
list_file = [5,5,6,5,4,2,4,6,5]

string_file = ['5','5','6','5','4','2','4','6','5']

empty_list = []

empty_list.append(string_file)

print(list_file)
print(string_file)
print(empty_list)


for index,items in enumerate(list_file):
    print(f"The value of index {index} is {items}")

"""
List comprehension is explained below:
List comprehension is a concise way to create a new list by performing 
an operation on each item in an existing iterable (like a list, range, or string), in a single line of code.
Like I want 'items' for each items in the 'list'
"""
# Basic_syntax:
# new_list = [expression for item in iterable if condition]
# expression: what you want to do with each item (can be just the item itself or some transformation of it)
#item: a variable that takes each value from the iterable
#iterable: the collection you’re looping through
#condition (optional): a filter to include only certain items

new_list = [items for items in string_file]
update_list = [(letter,items) for letter in string_file for items in range(4)]


print(new_list)
print(update_list)


#Dictionary comprehension

names = ["Bruce","Jackie","Morgan","Will","Leonardo"]
heroes = ["kung fu","Chinese","Latin","American","British"]

comb =  zip(names,heroes)

print(list(comb))

combined_dict = {name:hero for name,hero in zip(names,heroes)} # the zip function joins the two list
print(combined_dict)

