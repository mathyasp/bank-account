"""
    This file is for the BankAccount class. 
    This class simulates the interaction with a bank for a personal bank account.
"""

# Import libraries
import random


class BankAccount:
    """
    The BankAccount class has 3 attributes.
    account_type is set to Checking by default. (Stretch challenge #1)
    account_number is set to None which takes either a user input,
    or generates a random 8-digit #.
    balance is set to 0 by default if the user doesn't input a value.
    """

    def __init__(
        self, full_name, account_type="Checking", account_number=None, balance=0
    ):
        self.full_name = full_name
        self.account_type = account_type
        self.account_number = (
            account_number if account_number else random.randint(00000000, 99999999)
        )
        self.balance = float(balance)

    def deposit(self, amount):
        """
            This method takes in an amount and adds the float value to the balance.
            It then prints a message to the user.
        """
        self.balance += float(amount)
        print(f"Amount deposited: ${amount} new balance: ${self.balance}")

    def withdraw(self, amount):
        """
            This method takes in an amount and checks if the amount is greater than the balance.
            If not, it subtracts the float value from the balance.
            If it is, it alerts the user and issues a $10 overdraft fee, 
            subtracted from the balance.
            It then prints a message to the user.
        """
        if amount > self.balance:
            print("Insufficient funds. There will be a $10 overdraft fee.")
            self.balance -= 10
            print(f"Your new balance is: ${self.balance}")
        else:
            self.balance -= amount
            print(f"Amount withdrawn: ${amount}\nYour new balance is: ${self.balance}")

    def get_balance(self):
        """
            This method prints the current balance to the user and returns the balance.
        """
        print(f"Your current and available balance is ${self.balance}")
        return self.balance

    def add_interest(self):
        """
            This method checks if the account is checking or savings.
            It then calculates the interest and adds it to the balance accordingly
        """
        if self.account_type.lower() == "checking":
            interest = self.balance * 0.00083
            self.balance += interest
        elif self.account_type.lower() == "savings":
            interest = self.balance * 0.01
            self.balance += interest

    def print_statement(self):
        """
            This method prints out the account information in a user-friendly format.
        """
        print(self.full_name)
        print(f"{self.account_type} account")
        print(f"Account No.: {self.account_number}")
        print(f"Balance: ${self.balance}")
