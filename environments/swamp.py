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

    def addInhabitant(self, item):
        if not isinstance(item, IStagnant):
            raise TypeError(f"{item} is not of type IStagnant")
        self.inhabitants.append(item)

    def add_plant(self, plant):
        try:
            # if plant.freshwater and plant.requires_current:
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError("Must be swampy plants!!")

    def __str__(self):
        return self.name
