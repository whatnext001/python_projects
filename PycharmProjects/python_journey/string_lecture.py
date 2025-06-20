string_var = "I am a string variable"

find_len = len(string_var)
lower_var = string_var.lower()
upper_var = string_var.upper()
count_var = string_var.count('a') #count method do take in an argument
in_string = string_var[0:4] #to print out the index of a character, which can be a single i.e[0] location or range i.e[0:4]
find_string_var = string_var.find("string") #the find method finds the number of character or text in a string
replace_string_var = string_var.replace("am","with")#the replace method takes two argument
rev_string = (string_var[::-1])#this will reverse the string, list[start:end:steps]

print(rev_string)
print(find_len)
print(lower_var)
print(in_string)
print(upper_var)
print(count_var)
print(find_string_var)
print(replace_string_var)

#to know all the method you can use with a variable use dir i.e print(dir(str))
#print(dir(string_var))

#to get help on a method
#print(help(str))