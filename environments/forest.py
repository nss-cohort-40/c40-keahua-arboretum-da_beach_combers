# from animals import Aquatic
from .environment import Environment
import time


class Forest(Environment):

    def __init__(self, name):
        super().__init__(name)
        self.animal_capacity = 20
        self.plant_capacity = 32

    def add_animal(self, animal):
        if len(self.animals) < 19:
            self.animals.append(animal)
            print(f"{animal.species} lives in the Forest now")
        else:
            print(f'Sorry {animal.species}, we are full!')

    def add_plant(self, plant):
        if len(self.plants) < 32:
            self.plants.append(plant)
            print(f"{plant.species} lives in th River now")
        else:
            print(f'Sorry {plant.species}, we are full!')
        time.sleep(3)
        
