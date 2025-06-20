#to generate a random value between 0 and 1
import random
value = random.random()
print(value)

#to generate a random floating value

value_f = random.uniform(1,10)
print(value_f)

#to generate a random interger
value_i = random.randint(1,2)
print(value_i)

#to generate a random greetings from a list
greetings = ["hello","holla","hey","what's-up", "welcome"]
user_greet = random.choice(greetings)
print(user_greet + ",new user")

"""to make use of the method (choices)- 
it takes in some arguments e.g k-to specify the to number of the size, 
weight- the number of times you want an item to appear
"""
color_samples = ['red','yellow','blue']
result = random.choices(color_samples, weights=[12,5,6],k=10)
print(result)

#to shuffle a card
deck = list(range(1,53))
lets_shuf = random.shuffle(deck)
print(deck)

#to get a few number from our decks of card, you can use the .sample methods, and passing the argument k
new_card = random.sample(deck, k=5)
print(new_card)


