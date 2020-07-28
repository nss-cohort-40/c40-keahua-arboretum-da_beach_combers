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
        self.plant_capacity = 12
        # self.name = name
        # self.inhabitants = []

    def animal_count(self):
        return "This place has a bunch of animals in it"

    def add_animal(self, animal):
        if len(self.animals) < 8:
            self.animals.append(animal)
            print(f"{animal.species} lives in the Swamp now")
        else:
            print(f'Sorry {animal.species}, we are full!')

        time.sleep(2)

    def add_plant(self, plant):
        if len(self.plants) < 12:
            self.plants.append(plant)
            print(f"{plant.species} lives in the Swamp now")
        else:
            print(f'Sorry {plant.species}, we are full!')
        time.sleep(3)
