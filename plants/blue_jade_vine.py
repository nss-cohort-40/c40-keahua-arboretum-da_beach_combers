from .plant import Plant
from characteristics import Shady 

class Blue_Jade_Vine(Plant, Shady):

    def __init__(self):
        Plant.__init__(self, "Blue Jade Vine")
        Shady.__init__(self)

    @property 
    def plant(self):
        return self.__plant