import random

class BankAccount:
    def __init__(self, full_name, account_number = random.randint(00000000, 99999999), balance = 0):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited: ${amount} new balance: ${self.balance}")
    
    def withdraw(self, amount):  
        if amount > self.balance:
            print("Insufficient funds. There will be 1 $10 overdraft fee.")
            self.balance -= 10
        else:
            self.balance -= amount
            print(f"Amount withdrawn: ${amount} new balance ${self.balance}")

    def get_balance(self):
        print(f"Your current and available balance is ${self.balance}")
        return self.balance

    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest

    def print_statement(self):
        print(self.full_name)
        print(f"Account No.: {self.account_number}")
        print(f"Balance: ${self.balance}")


mitchell_bank_account = BankAccount("Mitchell", "03141592")
mitchell_bank_account.deposit(400000)
mitchell_bank_account.print_statement()
mitchell_bank_account.add_interest()
mitchell_bank_account.print_statement()
mitchell_bank_account.withdraw(150)
mitchell_bank_account.print_statement()