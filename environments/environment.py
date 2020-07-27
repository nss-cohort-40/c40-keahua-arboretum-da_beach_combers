from .contains_animals import ContainsAnimals
from .contains_plants import ContainsPlants
from characteristics import Identifiable

class Environment(ContainsAnimals, ContainsPlants, Identifiable):

    def __init__(self, name):
      ContainsAnimals.__init__(self)
      ContainsPlants.__init__(self)
      Identifiable.__init__(self)
      self.name = name 