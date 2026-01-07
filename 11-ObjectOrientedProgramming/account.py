class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds on the account")

    def display_info(self):
        formatted_number = ""
        for i, digit in enumerate(self.account_number.replace(" ", "")):
            if i > 0 and (i == 2 or (i - 2) % 4 == 0):
                formatted_number += " "
            formatted_number += digit
            
        print(f"Bank Account No: {formatted_number}")
        print(f"Balance: PLN {self.balance:.2f}".replace(".", ","))