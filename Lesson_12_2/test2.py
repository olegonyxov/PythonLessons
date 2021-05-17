class House:
    housenumber = int
    peoples = int
    def peoples_count(self,pcount):
        self.peoples += pcount
    def get_peoples_c(self):
        return self.peoples

class Street:
    streetnumber = int
    houses = []
    def houses_count(self,hcount):
        self.houses += hcount



class City:
    City_name = ""
    streets = []
    def streets_count(self,scount):
        self.streets += scount
