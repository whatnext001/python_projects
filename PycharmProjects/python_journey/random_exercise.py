import random
num = random.randint(1,101)
print(num)

dice = [1,2,3,4,5,6]
ordinals = ["first", "second", "third", "fourth", "fifth",
            "sixth", "seventh", "eighth", "ninth", "tenth"]
for items in range(0,10):
    roll = random.choice(dice)
    print(f" Roll {ordinals[items]} value is {roll} ")




