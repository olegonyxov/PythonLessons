
import csv


class Product:
    def __init__(self, pname, ptype, pprice):
        self.pname = pname
        self.ptype = ptype
        self.pprice = pprice

    def __str__(self):
        sstr = {self.ptype: self.pname, "Цена": self.pprice}
        return str(sstr)

    # def __repr__(self):
    #     repres = (self.pname, self.ptype, self.pprice)
    #     return str(repres)


class Store:
    __balanse = 0
    __storagelist = []

    def getfile(self, quantity=5):
        with open(filename, "r", encoding='utf-8') as file1:
            reader = csv.DictReader(file1)
            for item in reader:
                for a in range(quantity):
                    self.__storagelist.append(Product(item["Наименование"], item["Тип"], item["Цена"]))
        return self.__storagelist

    def get_ptype_list(self, ptype=""):
        ptypelist = []
        for p in self.__storagelist:
            if p.ptype == ptype or ptype == "":
                ptypelist.append([p.pname, p.ptype, p.pprice])
        return ptypelist

    def get_remains_price(self):
        remains_price = 0
        for p in self.__storagelist:
            remains_price += int(p.pprice)
        return remains_price

    def sell_item(self, pname):
        for p in self.__storagelist:
            if p.pname == pname:
                self.__balanse += int(p.pprice)
                self.__storagelist.remove(p)
                break

    def get_balance(self):
        return self.__balanse

    def add_product(self, pname, ptype, pprice):
        if ptype == "tea" or ptype == "coffee":
            self.__storagelist.append(Product(pname, ptype, pprice))
            return "product added to storage"
        else:
            return print("only tea or coffee")


if __name__ == "__main__":
    filename = 'C:\\tr1\\inventory.csv'
    # kofeita = Store()
    # kofeita.getfile()
    # print(kofeita.get_balance())
    # print(kofeita.get_ptype_list("coffee"))
    # print(kofeita.get_remains_price())
    # kofeita.sell_item("Эспрессо")
    # print(kofeita.get_ptype_list("coffee"))
    # print(kofeita.get_balance())
    # print(Product("1", "2", "3"))