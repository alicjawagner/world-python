import Plant
import OrganismsNames
import Point


class PineBorscht(Plant):

    def __init__(self, _world, arr=None):
        super().__init__(_world, arr)
        self.name = "Pine Borscht"
        self.sign = "b"
        if arr == None:
            self.strength = 10

    def whoAmI(self):
        return OrganismsNames.PINE_BORSCHT

    def action(self):
        # kills all the nearest animals
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue

                toKill = Point(self.point.x + i, self.point.y + j)
                if self.world.isFieldInBoard(toKill) == False or self.world.isFieldUnoccupied(toKill):
                    continue

                if self.world.whatIsOnBoard(toKill).isAnimal():
                    self.world.text += str(self) + " has no mercy: "
                    self.world.findOnField(toKill).die()
        super().action()

    #def draw(Graphics g):
    #    drawOrg(g, new Color(204, 235, 68))
