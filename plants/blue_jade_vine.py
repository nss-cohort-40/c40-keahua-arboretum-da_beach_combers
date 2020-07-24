from .plant import Plant
from characteristics import Shady 

class Blue_Jade_Vine(Plant, Shady):

    def __init__(self, location, seeds, sunlight, insecticide):
        Plant.__init__(self, "Blue Jade Vine")
        Shady.__init__(self)
        self.sunlight = "Partial"
        self.insecticide = "Low"
        self.location = "Grassland, Swamp"
        self.seeds = 0

    @property 
    def plant(self):
        return self.__plant