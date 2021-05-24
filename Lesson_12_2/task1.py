
import random
from pprint import pprint


class House:
    people = int

    def peoples_count(self, pcount):
        self.people += pcount

    def get_peoples_c(self):
        return self.people


class Street:
    houses = int

    def houses_count(self, hcount):
        self.houses += hcount

    def get_houses_c(self):
        return print(self.houses)


class City:
    peoplelist = []
    streets = int

    def streets_count(self, scount):
        self.streets += scount

    def get_streets_c(self):
        return print(self.streets)

    def full_em(self):
        finlist = []
        for street in range(1, random.randint(1, 5)):  #
            for house in range(1, random.randint(1, 20)):
                Street.houses = house
                self.streets = street
                people = random.randint(1, 99)
                self.peoplelist.append(people)
                finlist.append([street, house, people])
        return finlist

    def get_population(self):
        population = sum(pep for pep in self.peoplelist)
        return print(population)

    def print_it(self):
        print("Улица", 'Дом', 'Население')
        for result in self.full_em():
            print(result[0], "\t", result[1], " ", result[2])


# newCity = City()
# newCity.print_it()
# newCity.get_population()
# newCity.get_streets_c()