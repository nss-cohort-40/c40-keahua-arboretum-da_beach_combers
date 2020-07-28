# from animals import Aquatic
from .environment import Environment
import time


class Mountain(Environment):

    def __init__(self, name):
        super().__init__(name)

    def add_animal(self, animal):
        if len(self.animals) < 5:
            self.animals.append(animal)
            print(f"{animal.species} lives on the Mountain now")
        else:
            print(f'Sorry {animal.species}, we are full!')

        time.sleep(2)

    def add_plant(self, plant):
        try:
            # if plant.freshwater and plant.requires_current:
            self.plants.append(plant)
        except AttributeError:
            raise AttributeError(
                "Cannot add plants that require brackish water or stagnant water to a river biome")
