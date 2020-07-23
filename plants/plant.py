class Plant:

    def __init__(self, sunlight, seeds, insecticide):
      self.name = name
      self.species = species
      self.sunlight = sunlight
      self.seeds = seeds
      self.insecticide = insecticide

    def add_plant(self, plant):
        self.plants.append(plant)

    def remove_plant(self, plant):


class Mountain_Apple_Tree(Plant):

    def __init__(self, name, location, species, sunlight, seeds, insecticide):
        super().__init__(name, species, sunlight, seeds, insecticide)
        self.species = species
        self.sunlight = sunlight
        self.seeds = seeds
        self.insecticide = insecticide


    def add_plant(self, plant):
        self.plants.append(plant)

    def remove_plant(self, plant):


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

class Rainbow_Eucalyptus_Tree(Plant):

    # Remove redundant properties from Llama's initialization, and set their values via Animal
    def __init__(self, name, location, species, sunlight, seeds, insecticide):
        super().__init__(name, species, sunlight, seeds, insecticide)
        self.species = species
        self.sunlight = sunlight
        self.seeds = seeds
        self.insecticide = insecticide


    def add_plant(self, plant):
        self.plants.append(plant)

    def remove_plant(self, plant):


class Blue_Jade_Vine(Animal):

    # Remove redundant properties from Llama's initialization, and set their values via Animal
    def __init__(self, name, location, species, sunlight, seeds, insecticide):
        super().__init__(name, species, sunlight, seeds, insecticide)
        self.species = species
        self.sunlight = sunlight
        self.seeds = seeds
        self.insecticide = insecticide

    def add_plant(self, plant):
        self.plants.append(plant)

    def remove_plant(self, plant):