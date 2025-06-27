class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number
    def get_holder_name(self):
        return self.__holder_name
    def get_balance(self):
        return self.__balance

    def set_account_number(self, account_number):
        self.__account_number = account_number
    def set_holder_name(self, holder_name):
        self.__holder_name = holder_name
    def set_balance(self, balance):
        self.__balance = balance

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}. New balance is ₹{self.__balance}")
        else:
            print("Deposit amount must be positive")

    # Withdraw method
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ₹{amount}. Remaining balance is ₹{self.__balance}")
        else:
            print("Insufficient balance or invalid amount")

    def display_info(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Account Holder: {self.__holder_name}")
        print(f"Balance: ₹{self.__balance}")


# Demonstration
account1 = BankAccount("1234567890", "Priya Sharma", 5000)
account1.display_info()
account1.deposit(1500)
account1.withdraw(2000)
account1.display_info()