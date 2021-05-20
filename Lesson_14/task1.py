import csv
from datetime import datetime

selldate = datetime.now().strftime('%Y-%m-%d')
filename = 'C:\\tr1\\inventory.csv'
dictlist = []


class Store:
    balanse = 0
    storagelist = []

    def getfile(self):

        with open(filename, "r", encoding='utf-8') as file1:
            reader = csv.DictReader(file1, delimiter=",")
            for item in reader:
                dict1 = {"Наименование": item["Наименование"], "Тип": item["Тип"], "Цена": int(item["Цена"]), "Количество": 5}
                self.storagelist.append(dict1)
        return self.storagelist

    def get_ptype_list(self, ptype):
        ptypelist = []
        for pdict in self.getfile():
            if pdict['Тип'] == ptype or ptype == "all":
                ptypelist.append(pdict)
        return ptypelist

    def get_remains_price(self):
        remains_price = 0
        for pdict in self.getfile():
            remains_price += int(pdict["Цена"]) * int(pdict['Количество'])
        return remains_price

    def sell_item(self, pname, pcount):
        for pdict in self.getfile():
            if pdict["Наименование"] == pname and pdict["Количество"] > pcount:
                pdict["Количество"] -= int(pcount)
                self.balanse += pdict["Цена"] * int(pcount)
            else:
                print("Incorrect input")


class Product(Store):

    def __init__(self, pname="", ptype="", pprice=""):
        self.pname = pname
        self.ptype = ptype
        self.pprice = pprice

    def __repr__(self):
        examp = self.getfile()[1]
        return print(str({examp["Тип"]: examp["Наименование"], "Ценв": examp["Цена"]}))


kofeita = Store()
print(kofeita.getfile())
print(kofeita.get_remains_price())
print(kofeita.get_ptype_list("coffee"))
pempa = Product()
print(pempa)
