
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.account_holder} brought an amount of {amount} to deposit: Current Bal is {self.balance}")
        else:
            print("Kindly make a deposit")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.account_holder} made a withdrawal of {amount}: Current Bal is {self.balance}")
        else:
            print("Insufficient balance")

    def display_info(self):
        print(f"Customer Name:{self.account_holder}: Current Balance:{self.balance}")



# subclass savings account
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance = 0, interest_rate = 0.05):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        pass


# subclass checking account
class CheckingAccount(BankAccount):
    def __init__(self, account_holder, balance, overdraft_limit):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def over_withdraw(self):
        pass


customer_1 = BankAccount("Damilare", 0)
(customer_1.deposit(1000))
(customer_1.withdraw(6000))
(customer_1.display_info())

