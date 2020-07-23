from .terrestrial import Terrestrial

class Rainy(Terrestrial):

    def __init__(self):
        super().__init__()
        self.rainy = True