import uuid
from datetime import datetime


class Bank:
    account_name = ""
    UID = uuid.uuid1()
    balance = 0.00
    fee = 0.01
    transactions = []
    pass

    def __repr__(self):
        print("Банковский счет")

    def deposit(self, amount):
        self.balance += (amount + amount * self.fee)
        actions = (amount, "deposit", datetime.now().strftime('%Y-%m-%d'))
        self.transactions.append(actions)

    def withdraw(self, amount):
        self.balance -= (amount + amount * self.fee)
        actions = (amount, "withdraw", datetime.now().strftime('%Y-%m-%d'))
        self.transactions.append(actions)

    def show_balance(self):
        return print(self.balance)

    def show_transactions(self):
        return print(self.transactions)


# if __name__ == "__main__":
#     this_bank = Bank()
#     this_bank.deposit(23)
#     this_bank.withdraw(5)
#     this_bank.show_balance()
#     this_bank.show_transactions()
#     print(this_bank.UID)
