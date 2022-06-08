import Plant
import OrganismsNames


class DeadlyNightshade(Plant):

    def __init__(self, _world, arr=None):
        super().__init__(_world, arr)
        self.name = "Deadly Nightshade"
        self.sign = "n"
        if arr == None:
            self.strength = 99

    def whoAmI(self):
        return OrganismsNames.DEADLY_NIGHTSHADE

    def writeIWon(self):
        self.world.text += str(self) + " poison: "

    # def draw(Graphics g):
    #    drawOrg(g, new Color(33, 37, 77))
