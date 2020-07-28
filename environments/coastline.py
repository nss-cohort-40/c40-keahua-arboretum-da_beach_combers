# from animals import Aquatic
from .environment import Environment
import time


class Coastline(Environment):

    def __init__(self, name):
        super().__init__(name)
        self.animal_capacity = 15
        self.plant_capacity = 3

    def add_animal(self, animal):
        if len(self.animals) < 14:
            self.animals.append(animal)
            print(f"{animal.species} lives on the Coastline now")
        else:
            print(f'Sorry {animal.species}, we are full!')

        time.sleep(2)

    def add_plant(self, plant):
        if len(self.plants) < 3:
            self.plants.append(plant)
            print(f"{plant.species} lives in th River now")
        else:
            print(f'Sorry {plant.species}, we are full!')
        time.sleep(3)
