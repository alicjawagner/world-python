import Plant
import OrganismsNames


class Grass(Plant):

    def __init__(self, _world, arr=None):
        super().__init__(_world, arr)
        self.name = "Grass"
        self.sign = "g"
        if arr == None:
            self.strength = 0

    def whoAmI(self):
        return OrganismsNames.GRASS

    # def draw(Graphics g):
    #    drawOrg(g, new Color(86, 125, 70))