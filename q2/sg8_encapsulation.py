class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = 0.0
        self.set_balance(balance)

    def set_account_number(self, account_number):
        self.__account_number = account_number
    @property
    def get_account_number(self):
        return self.__account_number

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("The balance should not be a negative number.")
    @property
    def get_balance(self):
        return self.__balance
acc = BankAccount("12345", 500.0)
print("Account Number:", acc.get_account_number)  
print("Balance:", acc.get_balance)  

acc.set_balance(-100)  
print("Balance after invalid update:", acc.get_balance)  