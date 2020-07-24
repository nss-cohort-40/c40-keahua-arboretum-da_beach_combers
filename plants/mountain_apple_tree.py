from .plant import Plant
from characteristics import Shady 

class Mountain_Apple_Tree(Plant, Shady):

    def __init__(self):
        Plant.__init__(self, "Mountain Apple Tree")
        Shady.__init__(self)

    @property 
    def plant(self):
        return self.__plant