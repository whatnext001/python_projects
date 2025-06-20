#dictionary allows us to work with key value pairs

student_info = {
    "name":"john",
    "age":25,
    "courses":['ecn102','com102','pol104','mth701'],
    "department":"electrical engineering",
    "set":("2005/2006")
}

add_student = student_info["phone number"] = "888-9000"
delete_student = student_info.__delitem__("age") #to delete an item in the dictionary
update_student = student_info.update({"name":"anthony","age":35})#the .update method can be use to add new items to the dictionary
keys_student = student_info.keys() #the .keys method print out the keys
value_student = student_info.values() #the .values print out the values
items_student = student_info.items() #to print both keys and values


#this loops through the dictionary and prints out the keys and values by passing the key, items into the .items() method
for keys, items in items_student:
    print(f"{keys}:{items}")


print(student_info.get("name")) #the .get method can be use to get the key in a dictionary,
                                # this also helps when trying to access a key that doesn't in a dict because it
                                #will return a none value instead of throwing an error
print(student_info)
print(student_info["courses"])
print(keys_student)
print(value_student)
print(items_student)