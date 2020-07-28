import time
from .environment import Environment
import sys
sys.path.append('../')
# from characteristics import Stagnant

# from animals.


class Swamp(Environment):

    def __init__(self, name):
        super().__init__(name)
        self.animal_capacity = 8
        # self.name = name
        # self.inhabitants = []

    def animal_count(self):
        return "This place has a bunch of animals in it"

    def add_animal(self, animal):
        if len(self.animals) < 7:
            self.animals.append(animal)
            print(f"{animal.species} lives in the Swamp now")
        else:
            print(f'Sorry {animal.species}, we are full!')

        time.sleep(2)

    def add_plant(self, plant):
        try:
            # if plant.freshwater and plant.requires_current:
            self.plants.append(plant)
        except AttributeError:
            raise AttributeError("Must be swampy plants!!")

    def __str__(self):
        return self.name
