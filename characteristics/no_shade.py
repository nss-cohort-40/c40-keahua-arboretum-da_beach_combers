from .terrestrial import Terrestrial

class NoShade(Terrestrial):

    def __init__(self):
        super().__init__()
        self.no_shade = True