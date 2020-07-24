
class Silversword(Plant):

    def __init__(self, name, location, species, sunlight, seeds, insecticide):
        super().__init__(name, species, sunlight, seeds, insecticide)
        self.species = species
        self.sunlight = sunlight
        self.seeds = seeds
        self.insecticide = insecticide

    def plant(self):
        print(f'Plant in {environment}')
     
    def add_plant(self, plant):
        self.plants.append(plant)

    def remove_plant(self, plant):