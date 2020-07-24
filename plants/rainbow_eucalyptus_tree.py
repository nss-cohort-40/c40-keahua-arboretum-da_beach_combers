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