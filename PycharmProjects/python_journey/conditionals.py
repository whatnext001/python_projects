#is...used to check for object identity, test if two object have the same id which means same object in memory

a = [1,2,3]
b= [1,2,3]
c = 5
d = 5

print(a == b)
print(a is b)
print(id(a))
print(id(b))

print(c == d)
print(c is d)
print(id(c))
print(id(d))

test_var = "i am sunny ☀️"

print(test_var)

#tenary operator is a one liner if-else statement,
#Print or assign two values based on a condition
#X if condition else Y

user_role = "admin"
permision = "Log in" if user_role == "admin" else "you're not allowed to log in"

print(permision)