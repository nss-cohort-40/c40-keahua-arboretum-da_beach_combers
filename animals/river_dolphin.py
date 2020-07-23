from animals import Animal
from animals import Identifiable
from animals import Swimming
from characteristics import Aquatic
from characteristics import Freshwater
from characteristics import Saltwater


class RiverDolphin(Animal, Freshwater, Saltwater, Swimming, Aquatic, Identifiable):

    def __init__(self):
        Animal.__init__(self, "River dolphin")
        Freshwater.__init__(self)
        Swimming.__init__(self)
        Identifiable.__init__(self)
        Aquatic.__init__(self)
        self.__prey = {"Trout", "Mackarel", "Salmon", "Sardine"}

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The dolphin ate {prey} for a meal')
        else:
            print(f'The dolphin rejects the {prey}')

    def __str__(self):
        return f'Dolphin {self.id}. Eeee EeeEEeeeeEE!'
