# For this challenge, create a bank account class that has two attributes:

# owner
# balance
# and two methods:

# deposit
# withdraw
# As an added requirement, withdrawals may not exceed the available balance.

# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: {self.balance}"

    def deposit(self, quantity):
        self.balance += quantity
        print(f"Deposit accepted. Current balance: ${self.balance}")

    def withdraw(self, quantity):
        if self.balance >= quantity:
            self.balance -= quantity
            print(f"Withdrawal accepted. Current balance: ${self.balance}")
        else:
            print(f"Funds Unavailable! Current balance: ${self.balance}")

acct1 = Account("Jose", 100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)