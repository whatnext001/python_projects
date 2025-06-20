from colorama import init, Fore
init(autoreset=True)
class Ticket:
    def __init__(self, passenger_name, flight_number, base_price):
        self.passenger_name = passenger_name
        self.flight_number = flight_number
        self.base_price = base_price

    def calculate_final_price(self):
        return self.base_price

    def ticket_summary(self):
        print(Fore.GREEN + "Welcome To What_Next Airline...Your flight summary is stated below:")
        print(f"Name: {self.passenger_name}")
        print(f"Flight Number: {self.flight_number}")
        print(f"Base Price: {self.base_price}")
        print(f"Final Price: {self.calculate_final_price()}")
        print()
class EconomyTicket(Ticket):
    def __init__(self, passenger_name, flight_number, base_price, baggage_allowance):
        super().__init__(passenger_name, flight_number, base_price)
        self.baggage_allowance = baggage_allowance

    def calculate_final_price(self):
        initial_fee = 0
        if self.baggage_allowance > 20:
            initial_fee = self.baggage_allowance * 1000
        return self.base_price + initial_fee

    def ticket_summary(self):
        super().ticket_summary()
        return f"You're flying an economy class and your fee is {self.calculate_final_price()}"


class BusinessTicket(Ticket):
    def __init__(self, passenger_name, flight_number, base_price, lounge_access, meal_choice):
        super().__init__(passenger_name, flight_number, base_price)
        self.lounge_access = lounge_access
        self.meal_choice = meal_choice

    def calculate_final_price(self):
        perk_fee = 500000
        lounge_access = True
        if lounge_access:
            amount = self.base_price + perk_fee
            return amount

    def ticket_summary(self):
        super().ticket_summary()
        return f"You're flying a business class and your fee is {self.calculate_final_price()}"


def customers():
    onboard_passengers = [
        Ticket("Damilare", "WHAT001",2),
        EconomyTicket("Samuel","WHAT005",40,30),
        BusinessTicket("Semilore","WHAT007",800,True,"Non-Veg")
    ]

    for details in onboard_passengers:
        print(details.ticket_summary())

customers()