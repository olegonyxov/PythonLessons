import csv


class Product:

    def __init__(self, pname, ptype, pprice):
        self.pname = pname
        self.ptype = ptype
        self.pprice = pprice

    def __repr__(self):
        repres = {self.ptype: self.pname, "Цена": self.pprice}
        return str(repres)


class Store:
    balanse = 0
    storagelist = []

    def add_product(self, pname, ptype, pprice):
        if ptype == "tea" or ptype == "coffee":
            self.storagelist.append(Product(pname, ptype, pprice))
            return "product added to storage"
        else:
            return print("only tea and coffee")

    def getfile(self):
        with open(filename, "r", encoding='utf-8') as file1:
            reader = csv.DictReader(file1)
            bycond = 5
            for item in reader:
                for a in range(bycond):
                    self.storagelist.append(Product(item["Наименование"], item["Тип"], item["Цена"]))
        return self.storagelist

    def get_ptype_list(self, ptype=""):
        ptypelist = []
        for p in self.storagelist:
            if p.ptype == ptype or ptype == "":
                ptypelist.append([p.pname, p.ptype, p.pprice])
        return ptypelist

    def get_remains_price(self):
        remains_price = 0
        for p in self.storagelist:
            remains_price += int(p.pprice)
        return remains_price

    def sell_item(self, pname):
        for p in self.storagelist:
            if p.pname == pname:
                self.storagelist.remove(p)
                self.balanse += int(p.pprice)
                break


if __name__ == "__main__":
    filename = 'C:\\tr1\\inventory.csv'
    kofeita = Store()
    kofeita.getfile()
    print(kofeita.balanse)
    print(kofeita.get_ptype_list("coffee"))
    print(kofeita.get_remains_price())
    kofeita.sell_item("Эспрессо")
    print(kofeita.get_ptype_list("coffee"))
    print(kofeita.balanse)
