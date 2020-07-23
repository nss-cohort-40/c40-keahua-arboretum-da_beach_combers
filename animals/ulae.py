from animals import Animal
from animals import Swimming
from animals import Identifiable


class Ulae(Animal, Swimming, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Ulae")
        Swimming.__init__(self)
        Identifiable.__init__(self)
        self.__prey = {"reef invertebrate", "Water Bugs"}

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The Ulae ate {prey} for a meal')
        else:
            print(f'The Ulae rejects the {prey}')

    def __str__(self):
        return f'Ulae {self.id}. blub blub blub....!'