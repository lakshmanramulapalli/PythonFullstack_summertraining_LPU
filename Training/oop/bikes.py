class Bikes:
    def __init__(self,brand, bkname, rent):
        self.brandname = brand
        self.bikename = bkname
        self.rentperday = rent

    @property
    def bikename(self):
        return self.__bikename

    @bikename.setter
    def bikename(self, value):
        self.__bikename = value

    def calculate_rent(self, days):
        return self.rentperday * days


