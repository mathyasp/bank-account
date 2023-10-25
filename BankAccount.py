import random

class BankAccount:
    def __init__(self, full_name, account_type = "Checking", account_number = None, balance = 0):
        self.full_name = full_name
        self.account_type = account_type
        self.account_number = account_number if account_number else random.randint(00000000, 99999999)
        self.balance = float(balance)

    def deposit(self, amount):
        self.balance += float(amount)
        print(f"Amount deposited: ${amount} new balance: ${self.balance}")
    
    def withdraw(self, amount):  
        if amount > self.balance:
            print("Insufficient funds. There will be a $10 overdraft fee.")
            self.balance -= 10
        else:
            self.balance -= amount
            print(f"Amount withdrawn: ${amount} new balance ${self.balance}")

    def get_balance(self):
        print(f"Your current and available balance is ${self.balance}")
        return self.balance

    def add_interest(self):
        if self.account_type.lower() == "checking":
            interest = self.balance * 0.00083
            self.balance += interest
        elif self.account_type.lower() == "savings":
            interest = self.balance * 0.01
            self.balance += interest

    def print_statement(self):
        print(self.full_name)
        print(f"{self.account_type} account")
        print(f"Account No.: {self.account_number}")
        print(f"Balance: ${self.balance}")
