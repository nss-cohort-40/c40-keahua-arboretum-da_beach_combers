from .animal import Animal
from characteristics import Terrestrial
from characteristics import Walking
from characteristics import Identifiable


class GoldDustDayGecko(Animal, Terrestrial, Walking):

    def __init__(self):
        Animal.__init__(self, "Gold Dust Day Gecko")
        Terrestrial.__init__(self)
        Walking.__init__(self)
        self.__prey = ["Silkworms", "Hornworms", "Crickets", "Roaches"]

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The gecko ate {prey} for a meal')
        else:
            print(f'The gecko rejects the {prey}')
        input("\n\nPress enter to continue...")

    def __str__(self):
        return f'Gecko {self.id}. creeky noise via mouth....!'
