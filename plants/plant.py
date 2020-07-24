class Plant:

    def __init__(self, species, sunlight, seeds, insecticide):
      self.species = species
      self.sunlight = sunlight
      self.seeds = seeds
      self.insecticide = insecticide

    @property
    def seeds(self):
      return self.__seeds

    @property
    def species(self):
      return self.__species

    @property
    def sunlight(self):
      return self.__sunlight

    @property
    def insecticide(self):
      return self.__insecticide






