'''
2. Bank Account Simulation
Objective: Practice encapsulation and class-level methods.

Create a class BankAccount with the following:

Attributes: account_number, holder_name, balance.
Methods:
deposit(amount): Add money to the balance.
withdraw(amount): Deduct money if the balance is sufficient.
check_balance(): Display the current balance.
Ensure that balance is private and can only be modified using methods.
'''

class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        self.__balance -= amount
    
    def check_balance(self):
        print("Balance is : ", self.__balance)

saving_account = BankAccount(123456789, "Mohd Sameer", 9585.33)

saving_account.check_balance()