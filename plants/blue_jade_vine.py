from .plant import Plant
from characteristics import Shady 
from characteristics import Identifiable

class Blue_Jade_Vine(Plant, Shady, Identifiable):

    def __init__(self):
        Plant.__init__(self, "Blue Jade Vine")
        Shady.__init__(self)
        Identifiable.__init__(self)
        self.insecticide_resistance = "Low"
        self.seeds = 0
