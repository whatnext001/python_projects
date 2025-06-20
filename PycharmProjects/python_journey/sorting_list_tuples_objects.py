list_items = [5,6,7,8,5,6,2,5,64,89,78]

sort_list = sorted(list_items) #sorted is a built-in function to sort a list
invert_sort = sorted(list_items, reverse=True) #the reverse will invert the list
key_sorting = sorted(list_items, key=abs) #the key value can be use to sort based on a preferred criteria

print(sort_list)
print(invert_sort)
print(key_sorting)

tuple_items = (7.8,7,5,90,89,0,75,64,36)

sort_tuple = sorted(tuple_items)

print(sort_tuple)


dict_items = {
    "name":"Dammy",
     "age": 5,
    "occupation": "cyberguy"
}

sort_dict = sorted(dict_items, reverse=True)

print(sort_dict)