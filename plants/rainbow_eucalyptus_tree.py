from .plant import Plant
from characteristics import Shady 

class Rainbow_Eucalyptus_Tree(Plant, Shady):

    def __init__(self, location, seeds, sunlight, insecticide):
        Plant.__init__(self, "Blue Jade Vine")
        Shady.__init__(self)
        self.sunlight = "Shade"
        self.insecticide_resistance = "Low"
        self.location = "Forest"
        self.seeds = 8