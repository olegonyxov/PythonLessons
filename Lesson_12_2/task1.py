import random
class House:
    peoples = random.randint(1, 100)
    def peoples_count(self, pcount):
        self.peoples += pcount
    def get_peoples_c(self):
        return self.peoples

class Street:
    houses = random.randint(5, 20)
    def houses_count(self, hcount):
        self.houses += hcount
    def get_houses_c(self):
        return self.houses

class City:
    streets = random.randint(1, 5)
    def streets_count(self, scount):
        self.streets += scount
    def get_streets_c(self):
        return self.streets


