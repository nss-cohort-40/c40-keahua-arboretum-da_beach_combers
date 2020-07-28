from .environment import Environment

class River(Environment):

    def __init__(self, name):
        super().__init__(name)

    def add_animal(self, animal):
          
        try:
            # if len(self.animals) < 1:
                self.animals.append(animal)
        except ValueError:
            print("Biome Full")
            input('>> please hit enter')
        except AttributeError:
            print("Only Freshwater aquatic animals allowed")

    def add_plant(self, plant):
        try:
            # if plant.freshwater and plant.requires_current:
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError("Cannot add plants that require brackish water or stagnant water to a river biome")
