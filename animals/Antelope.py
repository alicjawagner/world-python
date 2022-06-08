import Animal
import OrganismsNames
import random
import Point


class Antelope(Animal):

    PROBABILITY_ESCAPING = 50

    def __init__(self, _world, arr=None):
        super().__init__(_world, arr)
        self.name = "Antelope"
        self.initiative = 4
        self.stepRange = 2
        self.sign = "A"
        if arr == None:
            self.strength = 4

    def ifIEscaped(self, attacker):
        if random.randrange(100) < Antelope.PROBABILITY_ESCAPING:
            self.stepRange = 1
            possibleMoves = self.findFieldsToMove()
            self.stepRange = 2
            self.removeOccupiedFields(possibleMoves)

            if len(possibleMoves) == 0:
                return False

            myOld = Point(self.point.x, self.point.y)
            attacker.moveToField(myOld)

            which = random.randrange(len(possibleMoves))
            self.point = Point(possibleMoves[which].x, possibleMoves[which].y)
            self.putOnBoard()

            self.world.text += str(self) + " escaped the fight ;) on field (" + str(
                attacker.point.x) + "," + str(attacker.point.y) + ")\n"
            return True
        return False

    def collision(self, attacked):
        if self.isTheSameSpecies(attacked):
            self.reproduce(attacked)
        elif random.randrange(100) < Antelope.PROBABILITY_ESCAPING:
            myOld = Point(self.point.x, self.point.y)
            self.point = attacked.point
            self.stepRange = 1
            possibleMoves = self.findFieldsToMove()
            self.stepRange = 2
            self.point = myOld
            self.removeOccupiedFields(possibleMoves)
            self.moveToRandField(possibleMoves)
            self.world.text += str(self) + " escaped the fight ;) on field (" + str(
                attacked.point.x) + "," + str(attacked.point.y) + ")\n"
        else:
            super().collision(attacked)

    def whoAmI(self):
        return OrganismsNames.ANTELOPE

    # def draw(Graphics g):
    #    drawOrg(g, new Color(158, 121, 104))
