from .plant import Plant
from characteristics import Shady 

class silversword(Plant, Shady):

    def __init__(self, location, seeds, sunlight, insecticide):
        Plant.__init__(self, "Blue Jade Vine")
        Shady.__init__(self)
        self.sunlight = "Full"
        self.insecticide = "High"
        self.location = "Grassland"
        self.seeds = 22