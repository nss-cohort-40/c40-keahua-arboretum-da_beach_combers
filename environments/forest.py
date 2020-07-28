# from animals import Aquatic
from .environment import Environment
import time


class Forest(Environment):

    def __init__(self, name):
        super().__init__(name)
        self.animal_capacity = 1
        self.plant_capacity = 1

    def add_animal(self, animal):
        try:
            # if animal.aquatic and animal.cell_type == "hypertonic":
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError("Cannot add non-aquatic, or saltwater animals to a river")

    def add_plant(self, plant):
        if len(self.plants) < 1:
            self.plants.append(plant)
            print(f"{plant.species} lives in th River now")
        else:
            print(f'Sorry {plant.species}, we are full!')
        time.sleep(3)
        input("\n\nPress enter to return to menu...")
