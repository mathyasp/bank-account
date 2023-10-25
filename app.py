"""
    As per stretch challenge #3:

    3. Create an "application". Use a loop to prompt us for an action. Actions can be:
        - Create account
        - Prompt for name, number, and balance.
        - Statement - prompts for the account number and prints the statement for that account.
        - Deposit - prompts for account number and amount. Then makes a deposit.
        - Withdraw - prompts for account number and amount. Then makes a withdrawl
"""

# Import libraries and the BankAccount class
import random
import os
from BankAccount import BankAccount


# Initialize empty list
bank = []


def user_input(prompt):
    """
    This helper function prompts the user for input.
    It then returns the variable containing the value of the input.
    """
    user_input = input(prompt)
    return user_input


def create_account():
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

    # Generate random account number if user desires
    if account_number.lower() == "r":
        account_number = random.randint(00000000, 99999999)

    # Use globals() to instantiate BankAccount class using account_name as the instance name
    globals()[account_name] = BankAccount(
        account_name,
        account_type=account_type,
        account_number=account_number,
        balance=initial_account_balance,
    )
    # Add to list
    bank.append(globals()[account_name])
    os.system("clear")
    print(
        f"Your account number is {account_number}. Remember this number for future access."
    )


def deposit_withdraw_money(entry):
    """
    This helper function takes in an argument called 'entry'.
    It prompts the user for an account number.
    If entry is D, it prompts the user for an amount and deposits it.
    If entry is W, it prompts the used for an amount and withdraws it.
    """
    input_account_number = input("Please enter your 8-digit account number:\n")

    for x in bank:
        if x.account_number == input_account_number:
            if entry == "D":
                action = "deposit"
                amount = float(
                    input(f"Please enter how much you would like to {action}:\n")
                )
                x.deposit(amount)
            else:
                action = "withdraw"
                amount = float(
                    input(f"Please enter how much you would like to {action}:\n")
                )
                x.withdraw(amount)


## Get bank statement
def statement():
    """
    This helper function prompts the user for an account number.
    It then prints the account information.
    """
    input_account_number = input("Please enter your 8-digit account number:\n")
    os.system("clear")

    for x in bank:
        if x.account_number == input_account_number:
            x.print_statement()


## Application
def bank_application(function_code):
    """
    This function serves as the actual application.
    It takes in an argument function_code which determines the function's behavior.
    If function_code is C, it calls on the create_account function.
    If function_code is D, it calls on the deposit_withdraw_money function with "D" as the arg
    If function_code is W, it calls on the deposit_withdraw_money function with "W" as the arg
    If function_code is S, is calls on the statement function
    And if function_code is Q, it quits the program.
    It displays an error message if the input isn't recognized
    """
    # Create item
    if function_code == "C":
        os.system("clear")
        create_account()

    # Deposit money
    elif function_code == "D":
        os.system("clear")
        deposit_withdraw_money("D")

    # Withdraw money
    elif function_code == "W":
        os.system("clear")
        deposit_withdraw_money("W")

    # Statement balance
    elif function_code == "S":
        os.system("clear")
        statement()

    # Stop the loop
    elif function_code == "Q":
        os.system("clear")
        return False

    # Catch all
    else:
        print("Unknown Option")

    return True


# Initialize application/prompting loop
RUNNING = True
print("Welcome to ACS-1111 National Bank!")
while RUNNING:
    print()
    # Get user input to determine app behavior
    selection = user_input("""Press:
C to create a new account,
D to deposit money into your account,
W to withdraw money from your account,
S to see your statement on a current account,
Press Q to quit:\n"""
    ).upper()
    # Call on bank_application function, passing in the selection as the argument
    RUNNING = bank_application(selection)
