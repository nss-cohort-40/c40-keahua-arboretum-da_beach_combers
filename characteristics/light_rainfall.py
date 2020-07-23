from .terrestrial import Terrestrial

class LightRainfall(Terrestrial):

    def __init__(self):
        super().__init__()
        self.light_rainfall = True