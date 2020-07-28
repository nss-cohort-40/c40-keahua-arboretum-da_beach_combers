from .environment import Environment


class River(Environment):

    def __init__(self, name):
        super().__init__(name)
        self.animal_capacity = 1
        self.plant_capacity = 1

    def add_animal(self, animal):
        try:
            if len(self.animals) < 1:
                self.animals.append(animal)
                print(f' {animal.species} lives here!')
        except ValueError:
            # raise ValueError("Biome Full")
            print(f' {animal.species} cant go here')

        input("\n\nPress any key to continue...")
