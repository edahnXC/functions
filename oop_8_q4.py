class Country:
    def init(self, name, population):
        self.__name = name
        self.__population = population
    def set_name(self, name):
        self.__name = name

def get_name(self):
    return self.__name

def set_population(self, population):
    self.__population = population

def get_population(self):
    return self.__population

country = Country("India", 1300000000)
print("Name:", country.get_name())
print("Population:", country.get_population())

country.set_name("China")
country.set_population(1400000000)
print("\nAfter modifying")
print("Name:", country.get_name())
print("Population:", country.get_population())