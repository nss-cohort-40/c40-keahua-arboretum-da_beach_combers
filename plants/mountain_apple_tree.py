from .plant import Plant
from characteristics import Shady 
from characteristics import Identifiable

class Mountain_Apple_Tree(Plant, Shady, Identifiable):

    def __init__(self):
        Plant.__init__(self, "Mountain Apple Tree")
        Shady.__init__(self)
        Identifiable.__init__(self)
        self.insecticide_resistance = "High"
        self.seeds = 17