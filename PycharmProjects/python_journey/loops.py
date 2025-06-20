#while loop
"""A while loop will continuously execute code depending on the value of a condition.
It begins with the keyword while, followed by a comparison to be evaluated, then a colon.
On the next line is the code block to be executed, indented to the right. Similar to an if statement,
the code in the body will only be executed if the comparison is evaluated to be true.
What sets a while loop apart, however, is that this code block will keep executing as long as
the evaluation statement is true. Once the statement is no longer true,
the loop exits and the next line of code will be executed."""

x = 0
while x < 5:
    print("Not there yet, x=" + str(x))
    x = x + 1
print("x=" + str(x))


num = 1
while num <= 10:
    print(num)
    num = num + 1


value = 0
sum = 0
while value < 5:
    value += 1
    sum = value + sum
    print(sum)

index = 0
add = 0
for index in range(0,6):
    add = index + add
    print(add)

secret_num = 8
guess = None
while secret_num != 8:
    if secret_num < 8:
        print("the number is close")
    elif secret_num > 8:
        print("the number is above")
    else:
        print("you guess right")


string = "welcome"
for char in string:
    print(char)

teams = [ 'Dragons', 'Wolves']

for i in teams:
    print(i)
    for b in teams:
        print(b)
