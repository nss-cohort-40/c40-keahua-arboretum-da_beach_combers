from .environment import Environment
import time


class Grassland(Environment):

    def __init__(self, name):
        super().__init__(name)
        self.animal_capacity = 22
        self.plant_capacity = 15

    def add_animal(self, animal):
        if len(self.animals) < 21:
            self.animals.append(animal)
            print(f"{animal.species} lives in the Grasslands now")
        else:
            print(f'Sorry {animal.species}, we are full!')

        time.sleep(2)

    def add_plant(self, plant):
        if len(self.plants) < 15:
            self.plants.append(plant)
            print(f"{plant.species} lives in the Grasslands now")
        else:
            print(f'Sorry {plant.species}, we are full!')
        time.sleep(3)
