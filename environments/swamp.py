from .environment import Environment
import sys
sys.path.append('../')
# from characteristics import Stagnant

# from animals.


class Swamp(Environment):

    def __init__(self, name):
        super().__init__(name)
        # self.name = name
        # self.inhabitants = []

    def animal_count(self):
        return "This place has a bunch of animals in it"

    def add_animal(self, animal):
        try:
            # if animal.aquatic and animal.cell_type == "hypertonic":
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError("Cannot add non-aquatic, or saltwater animals to a river")
    def add_plant(self, plant):
        try:
            # if plant.freshwater and plant.requires_current:
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError("Must be swampy plants!!")

    def __str__(self):
        return self.name
