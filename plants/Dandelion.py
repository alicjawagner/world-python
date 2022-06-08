import Plant
import OrganismsNames


class Dandelion(Plant):

    def __init__(self, _world, arr=None):
        super().__init__(_world, arr)
        self.name = "Dandelion"
        self.sign = "d"
        if arr == None:
            self.strength = 0

    def action(self):
        for i in range(3):
            super().action()

    def whoAmI(self):
        return OrganismsNames.DANDELION

    # def draw(Graphics g):
    #    drawOrg(g, new Color(245, 187, 0))