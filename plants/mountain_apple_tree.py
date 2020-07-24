from .plant import Plant
from characteristics import Shady 

class Mountain_Apple_Tree(Plant, Shady):

    def __init__(self, location, seeds, sunlight, insecticide):
        Plant.__init__(self, "Blue Jade Vine")
        Shady.__init__(self)
        self.sunlight = "Partial"
        self.insecticide = "High"
        self.location = "Mountain"
        self.seeds = 17

    @property 
    def plant(self):
        return self.__plant