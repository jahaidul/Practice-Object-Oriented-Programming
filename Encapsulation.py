class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute
    
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Error: Invalid balance")

account = BankAccount(1000)
print(account.get_balance())  # 1000
account.set_balance(500)
print(account.get_balance())  # 500
account.set_balance(-100)    # Error: Invalid balance
