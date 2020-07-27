from .animal import Animal
from characteristics import Terrestrial
from characteristics import Walking
from characteristics import Identifiable


class HappyFaceSpider(Animal, Terrestrial, Walking):

    def __init__(self):
        Animal.__init__(self, "Happy Face Spider")
        Terrestrial.__init__(self)
        Walking.__init__(self)
        self.__prey = ["grasshopper", "fruit flies"]

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The Happy-Face Spider ate {prey} for a meal')
        else:
            print(f'The Happy-Face Spider rejects the {prey}')
        input("\n\nPress enter to continue...")

    def __str__(self):
        return f'Happy-Face Spider {self.id}. skitter skatter!'
