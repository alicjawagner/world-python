import plant
import organismsNames


class DeadlyNightshade(plant.Plant):

    def __init__(self, _world, arr=None):
        super().__init__(_world, arr)
        self.name = "Deadly Nightshade"
        self.sign = "n"
        if arr == None:
            self.strength = 99

    def whoAmI(self):
        return organismsNames.OrganismsNames.DEADLY_NIGHTSHADE

    def writeIWon(self):
        self.world.text += str(self) + " poison: "

    def draw(self):
        self.drawOrg((33, 37, 77))
