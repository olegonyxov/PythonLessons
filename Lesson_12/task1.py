from datetime import datetime


class Bank:
    accunt_name = str
    uuid = 1
    balance = 0
    transactions = []
    pass

    def deposit(self, amount):
        self.balance += (amount + amount * 0.1)
        actions = (amount, "deposit", datetime.now().strftime('%Y-%m-%d'))
        self.transactions.append(actions)

    def withdraw(self, amount):
        self.balance -= (amount + amount * 0.1)
        actions = (amount, "withdraw", datetime.now().strftime('%Y-%m-%d'))
        self.transactions.append(actions)

    def showbalance(self):
        return print(self.balance)

    def showtrans(self):
        return print(self.transactions)


this_bank = Bank()

this_bank.deposit(23)
this_bank.withdraw(5)
this_bank.showbalance()
this_bank.showtrans()
