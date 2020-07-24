from .plant import Plant
from characteristics import Shady 
from characteristics import Identifiable

class Rainbow_Eucalyptus_Tree(Plant, Shady, Identifiable):

    def __init__(self):
        Plant.__init__(self, "Rainbow Eucalyptus Tree")
        Shady.__init__(self)
        Identifiable.__init__(self)
        self.insecticide_resistance = "Low"
        self.seeds = 8