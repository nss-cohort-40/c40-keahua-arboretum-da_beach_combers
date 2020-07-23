from .animal import Animal
from characteristics import Flying
from characteristics import Identifiable


class NeneGoose(Animal, Flying, Terrestrial, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Nene Goose")
        Flying.__init__(self)
        Identifiable.__init__(self)
        self.__prey = {"Seeds", "Grass", "Mollusk", "Bugs"}

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The goose ate {prey} for a meal')
        else:
            print(f'The goose rejects the {prey}')

    def __str__(self):
        return f'Goose {self.id}. Sqqqaawkkkk!'
