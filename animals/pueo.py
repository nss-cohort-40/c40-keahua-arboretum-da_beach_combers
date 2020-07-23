from animals import Animal
from animals import Flying
from animals import Identifiable


class Pueo(Animal, Flying, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Pueo")
        Flying.__init__(self)
        Identifiable.__init__(self)
        self.__prey = {"mice", "insects"}

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The Pueo ate {prey} for a meal')
        else:
            print(f'The Pueo rejects the {prey}')

    def __str__(self):
        return f'Pueo {self.id}. Screeecchh'
