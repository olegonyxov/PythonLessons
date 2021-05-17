import random


class House:
    peoples = random.randint(1, 99)

    def peoples_count(self, pcount):
        self.peoples += pcount

    def get_peoples_c(self):
        return self.peoples


class Street:
    houses = random.randint(5, 20)
    houselist = list(range(1, houses))

    def houses_count(self, hcount):
        self.houses += hcount

    def get_houses_c(self):
        return self.houses


class City:
    streets = random.randint(1, 5)
    streetlist = list(range(1, streets))

    def streets_count(self, scount):
        self.streets += scount

    def get_streets_c(self):
        return self.streets


def nachepatat_poshitat():
    peoplelist = []
    population = 0
    for i in range(1, House.peoples):
        peoplelist.append(random.randrange(1, 99))
    print("Улица", 'Дом', 'Населенме', )
    for street in City.streetlist:
        for house in Street.houselist:
            for peoples in peoplelist:
                print(street, "\t", house, "\t", peoples)
                population += peoples
    print("Количество населения :", population, "человек")


nachepatat_poshitat()
