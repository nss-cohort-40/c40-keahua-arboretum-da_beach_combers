# from animals import Aquatic
from .environment import Environment


class Mountain(Environment):

    def __init__(self):
        super().__init__()

    # def add_animal(self, animal):
    #     try:
    #         if animal.aquatic and animal.cell_type == "hypertonic":
    #             self.animals.append(animal)
    #     except AttributeError:
    #         raise AttributeError("Cannot add non-aquatic, or saltwater animals to a river")

    # def add_plant(self, plant):
    #     try:
    #         if plant.freshwater and plant.requires_current:
    #             self.plants.append(plant)
    #     except AttributeError:
    #         raise AttributeError("Cannot add plants that require brackish water or stagnant water to a river biome")
