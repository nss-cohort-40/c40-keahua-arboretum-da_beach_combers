import time
from .environment import Environment


class River(Environment):

    def __init__(self, name):
        super().__init__(name)
        self.animal_capacity = 12
        # self.plant_capacity = 1

    def add_animal(self, animal):
        if len(self.animals) < 11:
            self.animals.append(animal)
            print(f"{animal.species} lives in the River now")
        else:
            print(f'Sorry {animal.species}, we are full!')

        time.sleep(2)
