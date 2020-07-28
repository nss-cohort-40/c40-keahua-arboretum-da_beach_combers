import time
from .environment import Environment


class River(Environment):

    def __init__(self, name):
        super().__init__(name)
        self.animal_capacity = 12
        self.plant_capacity = 6

    def add_animal(self, animal):
        if len(self.animals) < 12:
            self.animals.append(animal)
            print(f"{animal.species} lives in the River now")
        else:
            print(f'Sorry {animal.species}, we are full!')

        time.sleep(2)

    def add_plant(self, plant):
        if len(self.plants) < 6:
            self.plants.append(plant)
            print(f"{plant.species} lives in the River now")
        else:
            print(f'Sorry {plant.species}, we are full!')
        time.sleep(3)
