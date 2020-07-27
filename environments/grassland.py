from .environment import Environment
from characteristics.shady import Shady


class Grassland(Environment):

    def __init__(self):
        super().__init__()

    # def add_animal(self, animal):
    #     try:
    #         if animal.aquatic and animal.cell_type == "hypertonic":
    #             self.animals.append(animal)
    #     except AttributeError:
    #         raise AttributeError("Cannot add non-aquatic, or saltwater animals to a river")

    def add_plant(self, plant):
        try:
            if plant.shady and plant.requires_current:
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError("Can only add plants that require shade to the grassland biome")
