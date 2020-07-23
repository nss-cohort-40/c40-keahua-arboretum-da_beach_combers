from animals import Animal
from animals import Walking
from animals import Identifiable
from animals import Terrestrial


class GoldDustDayGecko(Animal, Walking, Terrestrial, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Gold Dust Day Gecko")
        Walking.__init__(self)
        Identifiable.__init__(self)
        self.__prey = {"Silkworms", "Hornworms", "Crickets", "Roaches"}

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The gecko ate {prey} for a meal')
        else:
            print(f'The gecko rejects the {prey}')

    def __str__(self):
        return f'Gecko {self.id}. creeky noise via mouth....!'
