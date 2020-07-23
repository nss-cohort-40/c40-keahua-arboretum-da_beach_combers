from .terrestrial import Terrestrial

class HighElevation(Terrestrial):

    def __init__(self):
        super().__init__()
        self.high_elevation = True