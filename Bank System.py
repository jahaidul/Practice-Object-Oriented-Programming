class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, name, balance=0.0):
        self.accounts[name] = balance

    def deposit(self, name, amount):
        self.accounts[name] += amount

    def withdraw(self, name, amount):
        if self.accounts[name] < amount:
            print("Insufficient funds")
        else:
            self.accounts[name] -= amount

    def check_balance(self, name):
        return self.accounts[name]

bank = Bank()
bank.add_account("Alice")
bank.deposit("Alice", 100)
print(bank.check_balance("Alice"))  # Output: 100
bank.withdraw("Alice", 50)
print(bank.check_balance("Alice"))  # Output: 50
bank.withdraw("Alice", 60)  # Insufficient funds
