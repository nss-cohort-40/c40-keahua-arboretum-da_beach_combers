from .animal import Animal
from characteristics import Aquatic
from characteristics import Swimming
from characteristics import Identifiable


class Kikakapu(Animal, Aquatic, Swimming, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Kīkākapu")
        Aquatic.__init__(self)
        Swimming.__init__(self)
        Identifiable.__init__(self)
        self.__prey = {"reef invertebrate", "Water Bugs"}

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The Kīkākapu ate {prey} for a meal')
        else:
            print(f'The Kīkākapu rejects the {prey}')

    def __str__(self):
        return f'Kīkākapu {self.id}. blub blub blub....!'
