import animal
import organismsNames


class Sheep(animal.Animal):

    def __init__(self, _world, arr=None):
        super().__init__(_world, arr)
        self.name = "Sheep"
        self.initiative = 4
        self.sign = "S"
        if arr == None:
            self.strength = 4

    def whoAmI(self):
        return organismsNames.OrganismsNames.SHEEP

    # def draw(Graphics g):
    #    drawOrg(g, new Color(211, 211, 211))
