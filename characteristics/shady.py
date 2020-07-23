from .terrestrial import Terrestrial

class Shady(Terrestrial):

    def __init__(self):
        super().__init__()
        self.shady = True