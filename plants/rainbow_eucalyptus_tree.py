from .plant import Plant
from characteristics import Shady 

class Rainbow_Eucalyptus_Tree(Plant, Shady):

    def __init__(self):
        Plant.__init__(self, "Rainbow Eucalyptus Tree")
        Shady.__init__(self)

    @property 
    def plant(self):
        return self.__plant