# ACS-1111 Bank Account Assignment:

## Description

This assignment is an exploration of the OOP concept of Classes using Python

### Files included and brief overview
1. BankAccount.py
    * This file contains the BankAccount class:
        - Attributes:
            - `account_type` is set to Checking by default.
            - `account_number` is set to None and either takes in a user input, or generates a random 8-digit #.
            - `balance` is set to 0 by default if the user doesn't input a value.
        - Methods:
            - `deposit()`
            - `withdraw()`
            - `get_balance()`
            - `add_interest`
            - `print_statement()`
2. account_examples.py
    * This file serves as a place holder for code that tests the BankAccount class. 
        - Each chunk attempts to display the functionality of the class.
        - It also features the first 2 stretch challenges.
3. app.py
    * This file contains an "application". Based on stretch challenge #3
        - Use a loop to prompt us for an action. Actions can be:
            - Create account
            - Prompt for name, number, and balance.
            - Statement - prompts for the account number and prints the statement for that account.
            - Deposit - prompts for account number and amount. Then makes a deposit.
            - Withdraw - prompts for account number and amount. Then makes a withdrawl
4. Bank.py
    * This file contains the `Bank` class. Based on stretch challenge #4
        - Create a Bank class. This class will store a list of BackAccounts. It should implement the following methods: 
            - `create_account()` - creates a new account. 
            - `deposit()` - deposits an amount into an account with an account number
            - `withdraw()` - removes an amount from an account with an account number
            - `transfer()` - withdraws an amount from an account with an account number and deposits the same amount to an account with another number. 
            - `statement()` - prints an statement for an account with an account number. 
