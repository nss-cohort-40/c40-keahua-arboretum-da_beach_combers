# from animals import Aquatic
from .environment import Environment
import time


class Mountain(Environment):

    def __init__(self, name):
        super().__init__(name)
        self.animal_capacity = 6
        self.plant_capacity = 4

    def add_animal(self, animal):
        if len(self.animals) < 5:
            self.animals.append(animal)
            print(f"{animal.species} lives on the Mountain now")
        else:
            print(f'Sorry {animal.species}, we are full!')

        time.sleep(2)

    def add_plant(self, plant):
        if len(self.plants) < 4:
            self.plants.append(plant)
            print(f"{plant.species} lives in th River now")
        else:
            print(f'Sorry {plant.species}, we are full!')
        time.sleep(3)
