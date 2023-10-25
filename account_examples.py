"""
    This file serves as a place holder for code that tests the BankAccount class. 
    Each chunk attempts to display the functionality of the class.

    It also features the first 2 stretch challenges:
    
    1. Add an attribute to set the account type: checking or savings.
        - A savings account gets 1.2% insterest (that's 1% per month)
        - Create a checking and a savings account
        - Add interest to each account
        - Print a statement for each account

    2. Create a list called: bank. Add all of your accounts to bank. 
       Write a function that loops over all accounts in the list and 
       calls the add_interst method of each.
"""

# Import the BankAccount class
from BankAccount import BankAccount


# Initialize empty list (Stretch challenge #2)
bank = []

# As per requirement #6:
# Create a new bank account instance: user: "Mitchell", account number: 03141592.
mitchell_bank_account = BankAccount("Mitchell", account_number="03141592")
# Deposit $400,000 into "Mitchell's" account.
mitchell_bank_account.deposit(400000)
# Print a statement
mitchell_bank_account.print_statement()
# Add interest to the account
mitchell_bank_account.add_interest()
# Print a statement
mitchell_bank_account.print_statement()
# Make a withdrawl of $150 (Mitchell needs some Yeezy's)
mitchell_bank_account.withdraw(150)
# Print a statement
mitchell_bank_account.print_statement()

# Add to the list (Stretch challenge #2) and print empty line for spacing
bank.append(mitchell_bank_account)
print()


# Create another instance of BankAccount, utilize methods
john_bank_account = BankAccount("John")
john_bank_account.print_statement()
john_bank_account.deposit(500)
john_bank_account.withdraw(600)
john_bank_account.get_balance()
# Add to the list (Stretch challenge #2)
bank.append(john_bank_account)
print()


# Create another instance of BankAccount, utilize methods
jenny_bank_account = BankAccount("Jenny")
jenny_bank_account.deposit(10000)
jenny_bank_account.print_statement()
jenny_bank_account.add_interest()
jenny_bank_account.get_balance()
# Add to the list (Stretch challenge #2) and print empty line for spacing
bank.append(jenny_bank_account)
print()


# Demo of savings account (Stretch Challenge #1)
sarah_savings_account = BankAccount("Sarah", account_type="Savings")
sarah_savings_account.deposit(700)
sarah_savings_account.add_interest()
sarah_savings_account.print_statement()
# Add to the list (Stretch challenge #2) and print empty line for spacing
bank.append(sarah_savings_account)
print()


# Demo of checking account (Stretch Challenge #1)
fred_checking_account = BankAccount("Fred", account_type="Checking")
fred_checking_account.deposit(100)
fred_checking_account.add_interest()
fred_checking_account.print_statement()
# Add to the list (Stretch challenge #2) and print empty line for spacing
bank.append(fred_checking_account)
print()


def bank_interest():
    """
        Function that loops over the list of accounts and calls the add_interest method to each
        (Stretch challenge #2)
    """
    for x in bank:
        x.add_interest()

# Call on bank_interest function
bank_interest()
