from .animal import Animal
from characteristics import Aquatic
from characteristics import Swimming
from characteristics import Identifiable


class Opeapea(Animal, Aquatic, Swimming):

    def __init__(self):
        Animal.__init__(self, "Ope'ape'a")
        Aquatic.__init__(self)
        Swimming.__init__(self)
        self.__prey = ["reef invertebrate", "Water Bugs"]

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The Opeapea ate {prey} for a meal')
        else:
            print(f'The Opeapea rejects the {prey}')
        input("\n\nPress enter to continue...")

    def __str__(self):
        return f'Opeapea {self.id}. blub blub blub....!'
