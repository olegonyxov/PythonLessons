import uuid
from datetime import datetime


class BankAcc:
    account_name = ""
    UID = uuid.uuid1()
    balance = 0.00
    fee = 0.01
    transactions = []
    pass

    def __repr__(self):
        return "Банковский счет"

    def deposit(self, amount):
        self.balance += (amount + amount * self.fee)
        actions = (amount, "deposit", datetime.now().strftime('%Y-%m-%d'))
        self.transactions.append(actions)

    def withdraw(self, amount):
        self.balance -= (amount + amount * self.fee)
        actions = (amount, "withdraw", datetime.now().strftime('%Y-%m-%d'))
        self.transactions.append(actions)

    def get_balance(self):
        return print(self.balance)

    def get_transactions(self):
        return print(self.transactions)


# if __name__ == "__main__":
#     this_bank = BankAcc()
#     this_bank.deposit(23)
#     this_bank.withdraw(5)
#     this_bank.get_balance()
#     this_bank.get_transactions()
#     print(this_bank.UID)
