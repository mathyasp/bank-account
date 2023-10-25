"""
    As per stretch challenge #4:

    4. Create a Bank class. This class will store a list of BackAccounts. 
       It should implement the following methods:
        - create_account() - creates a new account.
        - deposit() - deposits an amount into an account with an account number
        - withdraw() - removes an amount from an account with an account number
        - transfer() - withdraws an amount from an account with an account number 
          and deposits the same amount to an account with another number.
        - statement() - prints an statement for an account with an account number.
"""

# Import library and the BankAccount class
import random
from BankAccount import BankAccount


class Bank:
    """
    The BankAccount class stores a list of BankAccount instances.
    It has 5 methods to interact with that list.
    """

    def __init__(self):
        self.bank = []

    def create_account(self):
        """
        This helper function prompts the user for account details.
        It then creates an instance of the BankAccount class using those account details.
        It uses the user input value for account_name as the variable name of the instance.
        It then appends that instance to the bank list, clears the console, and reminds the user
        not to forget their account #.
        """
        account_name = input("What's your name on the account?\n")
        account_type = input(
            "What type of account would you like to open? Checking or Savings?:\n"
        )
        account_number = input(
            "Please enter an 8-digit account number. Enter 'r' for a random account number:\n"
        )
        initial_account_balance = input("Please enter your initial balance:\n")

        if account_number.lower() == "r":
            account_number = random.randint(00000000, 99999999)

        # Use globals() to instantiate BankAccount class using account_name as the instance name
        globals()[account_name] = BankAccount(
            account_name,
            account_type=account_type,
            account_number=account_number,
            balance=initial_account_balance,
        )
        self.bank.append(globals()[account_name])
        print(
            f"Your account number is {account_number}. Remember this number for future access."
        )

    def deposit(self, amount=None):
        """
            This method takes in an amount and adds the float value to the balance.
            It then prints a message to the user.
        """
        input_account_number = input("Please enter your 8-digit account number:\n")
        amount = (
            amount
            if amount
            else float(input("Please enter how much you would like to deposit:\n"))
        )

        for x in self.bank:
            if x.account_number == input_account_number:
                x.balance += float(amount)
                print(f"Amount deposited: ${amount} new balance ${x.balance}")

    def withdraw(self, amount=None):
        """
            This method takes in an amount or prompts the user for an amount 
            and checks if the amount is greater than the balance.
            If not, it subtracts the float value from the balance.
            If it is, it alerts the user and issues a $10 overdraft fee, 
            subtracted from the balance.
            It then prints a message to the user.
        """
        input_account_number = input("Please enter your 8-digit account number:\n")
        amount = (
            amount
            if amount
            else float(input("Please enter how much you would like to withdraw:\n"))
        )

        for x in self.bank:
            if x.account_number == input_account_number:
                if amount > x.balance:
                    print("Insufficient funds. There will be a $10 overdraft fee.")
                    x.balance -= 10
                else:
                    x.balance -= float(amount)
                    print(f"Amount withdrawn: ${amount} new balance ${x.balance}")

    def transfer(self):
        """
            This method prompts the user for 2 account numbers (transfer_from & transfer_to).
            It also prompts the user for the transfer amount.
            It then withdraws that amount from transfer_from and deposits the amount to
            transfer_to.
        """
        transfer_from = input(
            "Please enter the 8-digit account number you wish to transfer from.\n"
        )
        amount = float(input("Please enter the amount you wish to transfer:\n"))
        transfer_to = input(
            "Please enter the 8-digit account number you wish to transfer to.\n"
        )

        for x in self.bank:
            for y in self.bank:
                if (
                    x.account_number == transfer_from
                    and y.account_number == transfer_to
                ):
                    x.withdraw(amount)
                    y.deposit(amount)

    def statement(self):
        """
            This method prints out the account information in a user-friendly format.
        """
        input_account_number = input("Please enter your 8-digit account number:\n")

        for x in self.bank:
            if x.account_number == input_account_number:
                x.print_statement()


# Test code, un-comment to utilize
# newBank = Bank()
# newBank.create_account()
# newBank.create_account()
# newBank.deposit()
# newBank.withdraw()
# newBank.transfer()
# newBank.statement()
# newBank.statement()
