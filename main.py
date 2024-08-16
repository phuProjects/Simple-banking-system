class Account:
    def __init__(self, account_number, holder_name, inital_balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = inital_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else: 
            print(f"You have withdrawed ${amount}")
            self.balance -= amount
    def get_balance(self):
        return self.balance

account = Account("12345", "John", 0)

account.deposit(500.0)

account.withdraw(300.0)
print(f"{account.holder_name}'s account balance: ${account.get_balance()}")