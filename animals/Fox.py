import animal
import organismsNames


class Fox(animal.Animal):

    def __init__(self, _world, arr=None):
        super().__init__(_world, arr)
        self.name = "Fox"
        self.initiative = 7
        self.sign = "F"
        if arr == None:
            self.strength = 3

    def findFieldsToMove(self):
        possibleMoves = super().findFieldsToMove()

        if len(possibleMoves) == 0:
            return possibleMoves

        possibleMoves[:] = [field for field in possibleMoves if self.world.findOnField(field) == None or (
            self.world.findOnField(field) != None and self.world.findOnField(field).strength <= self.strength)]
        return possibleMoves

    def whoAmI(self):
        return organismsNames.OrganismsNames.FOX

    def draw(self):
        self.drawOrg((255, 124, 5))
