import random
from pprint import pprint


class House:
    people = ""

    def peoples_count(self, pcount):
        self.people += pcount

    def get_peoples_c(self):
        return self.people


class Street:
    houses = random.randint(5, 20)
    houselist = list(range(1, houses))

    def houses_count(self, hcount):
        self.houses += hcount

    def get_houses_c(self):
        return print(self.houses)


class City:
    streets = random.randint(1, 5)
    streetlist = list(range(1, streets))

    def streets_count(self, scount):
        self.streets += scount

    def get_streets_c(self):
        return self.streets


def full_em():
    finlist = []
    for street in City.streetlist:
        for house in Street.houselist:
            people = random.randint(1, 99)
            finlist.append([street, house, people])
    return finlist


if __name__ == "__main__":
    print("Улица", 'Дом', 'Население')
    for result in full_em():
        print(*result)
