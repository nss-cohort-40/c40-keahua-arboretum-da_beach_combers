from .plant import Plant
from characteristics import Shady 

class silversword(Plant, Shady):

    def __init__(self):
        Plant.__init__(self, "silversword")
        Shady.__init__(self)

    @property 
    def plant(self):
        return self.__plant