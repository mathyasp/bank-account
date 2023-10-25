from BankAccount import BankAccount

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