import plant
import organismsNames


class Grass(plant.Plant):

    def __init__(self, _world, arr=None):
        super().__init__(_world, arr)
        self.name = "Grass"
        self.sign = "g"
        if arr == None:
            self.strength = 0

    def whoAmI(self):
        return organismsNames.OrganismsNames.GRASS

    def draw(self):
        self.drawOrg((86, 125, 70))
