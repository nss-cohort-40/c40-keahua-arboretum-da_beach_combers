from .animal import Animal
from characteristics import Terrestrial
from characteristics import Flying
from characteristics import Identifiable


class Pueo(Animal, Terrestrial, Flying):

    def __init__(self):
        Animal.__init__(self, "Pueo")
        Terrestrial.__init__(self)
        Flying.__init__(self)
        self.__prey = ["mice", "insects"]

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The Pueo ate {prey} for a meal')
        else:
            print(f'The Pueo rejects the {prey}')
        input("\n\nPress enter to continue...")

    def __str__(self):
        return f'Pueo {self.id}. Screeecchh'
