import csv
import json
from datetime import datetime

selldate = datetime.now().strftime('%Y-%m-%d')
filename = 'C:\\tr1\\inventory.csv'
storage = []
dictlist =[]
storage = storage*5
with open(filename, "r", encoding='utf-8') as file1:
    reader = csv.DictReader(file1, delimiter=",")
    for row in reader:
        storage.append([row["Наименование"], row["Тип"], row["Цена"]])
        dict2={"Наименование":row["Наименование"],"Тип": row["Тип"],"Цена": row["Цена"]}
        dictlist.append(dict2)
print(storage)
print(dictlist)

# name = (name[1] for name in storage)
# ptype = (tipe[2] for tipe in storage)
# price = (price[3] for price in storage)




class Product():

    def __init__(self, pname, ptype,):
        self.pname = pname
        self.ptype = ptype
        self.price = int
        self.pcount= 5

    def get_price(self):
        print(self.pname,self.ptype)
        for smth in storage:
            if self.pname == smth[0] and self.ptype == smth[1]:
                self.price = int(smth[2])
        return self.price


class Shop():

    tradelist = []
    balance = 0
    goods = storage

    def sellin(self):
        self.balance += int

    def buyin(self):
        self.balance -= ""


a = 'Эспрессо'
b = 'coffee'
espresso=Product(a,b)
print(espresso.get_price())


kaviarnia = Shop()
