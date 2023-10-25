from BankAccount import BankAccount
import random
import os

bank = []

## Get input from the user
def user_input(prompt):
    user_input = input(prompt)
    return user_input


## Create a new account
def create_account():
    account_name = input("What's your name on the account?\n")
    account_type = input("What type of account would you like to open? Checking or Savings?:\n")
    account_number = input("Please enter an 8-digit account number. Enter 'r' for a random account number:\n")
    initial_account_balance = input("Please enter your initial balance:\n")

    if account_number.lower() == 'r':
        account_number = random.randint(00000000, 99999999)

    # Use globals() to instantiate BankAccount class using account_name as the instance name
    globals()[account_name] = BankAccount(account_name, account_type=account_type, account_number=account_number, balance=initial_account_balance)
    bank.append(globals()[account_name])
    os.system('clear')
    print(f"Your account number is {account_number}. Remember this number for future account access.")


## Deposit or withdraw money into/from account
def deposit_withdraw_money(entry):
    input_account_number = input("Please enter your 8-digit account number:\n")

    for x in bank:
        if x.account_number == input_account_number:
            if entry == "D":
                action = "deposit"
                amount = float(input(f"Please enter how much you would like to {action}:\n"))
                x.deposit(amount)
            else:
                action = "withdraw"
                amount = float(input(f"Please enter how much you would like to {action}:\n"))
                x.withdraw(amount)
            os.system('clear')
            x.get_balance()
    

## Get bank statement
def statement():
    input_account_number = input("Please enter your 8-digit account number:\n")   
    os.system('clear')

    for x in bank:
        if x.account_number == input_account_number:
            x.print_statement()


## Application
def bank_application(function_code):
    # Create item
    if function_code == "C":
        os.system('clear')
        create_account()

    # Deposit money
    elif function_code == "D":
        deposit_withdraw_money("D")

    # Withdraw money
    elif function_code == "W":
        deposit_withdraw_money("W")

    # Statement balance
    elif function_code == "S":
        os.system('clear')
        statement()

    # Stop the loop
    elif function_code == "Q":
        os.system('clear')
        return False

    # Catch all
    else:
        print("Unknown Option")

    return True

running = True
print("Welcome to ACS-1111 National Bank!")
while running:
    print()
    selection = user_input("Press:\nC to create a new account,\nD to deposit money into your account,\nW to withdraw money from your account,\nS to see your statement on a current account,\nPress Q to quit:\n").upper()
    running = bank_application(selection)