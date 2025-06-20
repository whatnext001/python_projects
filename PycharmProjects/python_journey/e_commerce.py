class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_details(self):
        return f"The Item picked is {self.name} and the price is {self.price}."


class Book(Product):
    def __init__(self, name, price, author, isbn):
        super().__init__(name, price)
        self.author = author
        self.isbn = isbn


    def display_details(self):
        return f"The author's name is {self.author} with {self.isbn} number"

class Electronics(Product):
    def __init__(self, name, price, brand, warranty_years):
        super().__init__(name, price)
        self.brand = brand
        self.warranty_years = warranty_years

    def display_details(self):
        return f"The brand's name is {self.brand}, which has a warranty of {self.warranty_years} years"


class Clothing(Product):
    def __init__(self, name, price, size, material):
        super().__init__(name, price)
        self.size = size
        self.material = material

    def display_details(self):
        return f"The clothe size is {self.size}, with a material called {self.material}"



cart = [

    Book("Awaking The Giant Within",500,"Tonny Robbins","12345"),
    Electronics("Smart TV",8800,"Samsung",5),
    Clothing("Burberry",9000,32,"silk")
]

print("Shopping Cart Details:\n" + "-"*25)

for items in cart:
    print(items.display_details())
    print("-" * 50)

total_price = sum(item.price for item in cart)
print(f"Total Price: ${total_price:.2f}")