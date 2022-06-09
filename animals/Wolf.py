import animal
import organismsNames


class Wolf(animal.Animal):

    def __init__(self, _world, arr=None):
        super().__init__(_world, arr)
        self.name = "Wolf"
        self.initiative = 5
        self.sign = "W"
        if arr == None:
            self.strength = 9

    def whoAmI(self):
        return organismsNames.OrganismsNames.WOLF

    # def draw(Graphics g):
    #    drawOrg(g, new Color(43, 45, 47))
