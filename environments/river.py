from .environment import Environment

class River(Environment):

    def __init__(self, name):
        super().__init__(name)

    def add_animal(self, animal):
        try:
            if animal.aquatic and animal.cell_type == "hypertonic":
                try:
                    if len(self.animals) < 12:
                        self.animals.append(animal)
                except ValueError:
                    print("Biome Full")
        except AttributeError:
            print("Only Freshwater aquatic animals allowed")

    def add_plant(self, plant):
        try:
            if plant.freshwater and plant.requires_current:
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError("Cannot add plants ")
