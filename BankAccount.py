import random

class BankAccount:
    def __init__(self, full_name, account_type = "Checking", account_number = None, balance = 0):
        self.full_name = full_name
        self.account_type = account_type
        self.account_number = account_number if account_number else random.randint(00000000, 99999999)
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
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


bank = []


mitchell_bank_account = BankAccount("Mitchell", account_number="03141592")
mitchell_bank_account.deposit(400000)
mitchell_bank_account.print_statement()
mitchell_bank_account.add_interest()
mitchell_bank_account.print_statement()
mitchell_bank_account.withdraw(150)
mitchell_bank_account.print_statement()
bank.append(mitchell_bank_account)
print()


john_bank_account = BankAccount("John")
john_bank_account.print_statement()
john_bank_account.deposit(500)
john_bank_account.withdraw(600)
john_bank_account.get_balance()
bank.append(john_bank_account)
print()


jenny_bank_account = BankAccount("Jenny")
jenny_bank_account.deposit(10000)
jenny_bank_account.print_statement()
jenny_bank_account.add_interest()
jenny_bank_account.get_balance()
bank.append(jenny_bank_account)
print()


sarah_savings_account = BankAccount("Sarah", account_type="Savings")
sarah_savings_account.deposit(700)
sarah_savings_account.add_interest()
sarah_savings_account.print_statement()
bank.append(sarah_savings_account)
print()


fred_checking_account = BankAccount("Fred", account_type="Checking")
fred_checking_account.deposit(100)
fred_checking_account.add_interest()
fred_checking_account.print_statement()
bank.append(fred_checking_account)
print()


def bank_interest():
    for x in bank:
        x.add_interest()


bank_interest()