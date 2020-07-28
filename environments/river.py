import time
from .environment import Environment

class River(Environment):

    def __init__(self, name):
        super().__init__(name)
        self.animal_capacity = 1
        self.plant_capacity = 1

    def add_animal(self, animal):
        if len(self.animals) < 1:
            self.animals.append(animal)
            print(f"{animal.species} lives in th River now")
        else:
            print(f'Sorry {animal.species}, we are full!')
        time.sleep(2)

    def add_plant(self, plant):
        if len(self.plants) < 1:
            self.plants.append(plant)
            print(f"{plant.species} lives in th River now")
        else:
            print(f'Sorry {plant.species}, we are full!')
        time.sleep(3)
        input("\n\nPress enter to return to menu...")
