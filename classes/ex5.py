"""Create a bank account class that has attributes owner,
balance and two methods deposit and withdraw.
Withdrawals may not exceed the available balance.
Instantiate your class, make several deposits and withdrawals,
and test to make sure the account can't be overdrawn."""
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of ${amount:.2f} successful. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds! Available balance: ${self.balance:.2f}")
        else:
            self.balance -= amount
            print(f"Withdrawal of ${amount:.2f} successful. New balance: ${self.balance:.2f}")

    def __str__(self):
        return f"Account Owner: {self.owner}\nAccount Balance: ${self.balance:.2f}"

# Example usage
acct = Account("Alice", 100)
print(acct)

acct.deposit(50)
acct.withdraw(30)
acct.withdraw(150)
acct.deposit(200)
acct.withdraw(100)
