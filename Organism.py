import random
import world
import point
import organismsNames
from abc import ABC, abstractmethod


class Organism(ABC):

    DELIMITER = " "
    STRONGER = 1
    EQUAL = 0
    WEAKER = -1

    def __init__(self, _world, arr=None):
        self.world = _world
        self.isAlive = True
        self.stepRange = 1
        self.initiative = -1
        self.name = ""
        self.sign = ""

        if arr == None:
            self.strength = -1
            self.birthTime = self.world.numberOfBornOrganisms + 1

            fields = world.World.FIELDS_NUMBER
            while True:
                x = random.randint(0, fields - 1)
                y = random.randint(0, fields - 1)
                if self.world.board[x][y] == None:
                    break
            self.point = point.Point(x, y)
        else:
            self.point = point.Point(int(arr[1]), int(arr[2]))
            self.birthTime = int(arr[3])
            self.strength = int(arr[4])

    @abstractmethod
    def whoAmI(self):
        pass

    @abstractmethod
    def action(self):
        pass

    @abstractmethod
    def draw(sellf):
        pass

    def amIStronger(self, other):
        if self.strength > other.strength:
            return Organism.STRONGER
        elif self.strength == other.strength:
            return Organism.EQUAL
        else:
            return Organism.WEAKER

    def ifIRepelledTheAttack(self, attacker):
        return False

    def ifIEscaped(self, attacker):
        return False

    def ifILostTheFight(self, attacker):
        return self.amIStronger(attacker) != Organism.STRONGER

    def isAnimal(self):
        me = self.whoAmI()
        if me == organismsNames.OrganismsNames.GRASS or me == organismsNames.OrganismsNames.GUARANA or me == organismsNames.OrganismsNames.DANDELION or (
                me == organismsNames.OrganismsNames.DEADLY_NIGHTSHADE or me == organismsNames.OrganismsNames.PINE_BORSCHT or me == organismsNames.OrganismsNames.CYBERSHEEP):
            return False
        return True

    def findFieldsToMove(self):
        current = self.point

        possibleMoves = []
        for i in range(-1 * self.stepRange, self.stepRange + 1, self.stepRange):
            for j in range(-1 * self.stepRange, self.stepRange + 1, self.stepRange):
                if i == 0 and j == 0:
                    continue

                possibleMove = point.Point(current.x + i, current.y + j)
                if self.world.isFieldInBoard(possibleMove):
                    possibleMoves.append(possibleMove)

        return possibleMoves

    def removeOccupiedFields(self, possibleMoves):
        possibleMoves[:] = [
            move for move in possibleMoves if self.world.isFieldUnoccupied(move)]

    def putOnBoard(self):
        self.world.board[self.point.x][self.point.y] = self

    def moveToField(self, newPoint):
        self.world.clearTheField(self.point)
        self.point = newPoint
        self.putOnBoard()

    def writeIWon(self):
        self.world.text += str(self) + " won the fight: "

    def writeIDie(self):
        self.world.text += self.name + " is dead :(\n"

    def die(self):
        self.isAlive = False
        self.world.clearTheField(self.point)
        self.writeIDie()

    def makeChild(self, possibleFields):
        child = self.world.createOrganism(self.whoAmI())

        which = random.randrange(len(possibleFields))
        child.moveToField(possibleFields[which])
        self.world.insertIntoToAdd(child)

    def __str__(self) -> str:
        return self.name + " (" + str(self.point.x) + "," + str(self.point.y) + ")"

    
    @abstractmethod
    def drawShapeOrg(self, color):
        pass

    def drawOrg(self, color):
        self.drawShapeOrg(color)

        textSur = self.world.textFont.render(self.sign, True, (255, 255, 255))
        self.world.screen.blit(textSur, (self.point.x * self.world.FIELD_SIZE + 10, self.point.y * self.world.FIELD_SIZE + 2))

    def writeMeToFile(self, f):
        f.write(self.sign + self.DELIMITER + str(self.point.x) +
                self.DELIMITER + str(self.point.y) + self.DELIMITER + str(self.birthTime) + self.DELIMITER + str(self.strength))
        self.myOwnFieldsToFile(f)
        f.write("\n")

    def myOwnFieldsToFile(self, f):
        pass
