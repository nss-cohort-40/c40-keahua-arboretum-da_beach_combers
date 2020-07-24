from .environment import Environment

class Plant:

    def __init__(self, species,  sunlight, seeds, insecticide):
      self.species = species
      self.sunlight = sunlight
      self.seeds = seeds
      self.insecticide = insecticide

    def plant(self, plant):
        try:
            if environment.capacity > -1:
                self.plants.append(plant)
                print(f"{plant}  cultivated in {self.location}")
        except AttributeError as ex:
            print(f'{plant} could not be added due to lack  of capacity at {self.name}.')









