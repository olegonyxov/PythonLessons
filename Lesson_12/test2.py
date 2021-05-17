from datetime import datetime


class Bank:
    accunt_name = str
    uuid = 1
    balance = 0
    transactions = dict
    pass

    def deposit(self, amount):
        now = datetime.now().strftime('%Y-%m-%d')
        self.balance += (amount + amount * 0.1)
        actions = ({"amount": amount, "action": "deposit", "date": now})
        self.transactions.update(actions)

    def withdraw(self, amount):
        now = datetime.now().strftime('%Y-%m-%d')
        self.balance -= (amount + amount * 0.1)
        actions = ({"amount": amount, "action": "withdraw", "date": now})
        self.transactions.update(actions)

    def showbalance(self):
        return print(self.balance)

    def showtrans(self):
        return (print(self.transactions))


this_bank = Bank()

this_bank.deposit(23)
this_bank.withdraw(5)
this_bank.showbalance()
this_bank.showtrans()