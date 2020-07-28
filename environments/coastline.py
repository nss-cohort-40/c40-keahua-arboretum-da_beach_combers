# from animals import Aquatic
from .environment import Environment
import time


class Coastline(Environment):

    def __init__(self, name):
        super().__init__(name)
        self.animal_capacity = 12

    def add_animal(self, animal):
        if len(self.animals) < 1:
            # 14
            self.animals.append(animal)
            print(f"{animal.species} lives on the Coastline now")
        else:
            print(f'Sorry {animal.species}, we are full!')

        time.sleep(2)
