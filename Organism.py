import random
import World
import Point
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

            fields = World.FIELDS_NUMBER
            while True:
                x = random.randint(0, fields - 1)
                y = random.randint(0, fields - 1)
                if self.world.board[x][y] == None:
                    break
            self.point = Point(x, y)
        else:
            self.point = Point(int(arr[1]), int(arr[2]))
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

    def findFieldsToMove(self):
        current = self.point

        possibleMoves = []
        for i in range(-1 * self.stepRange, self.stepRange + 1, self.stepRange):
            for j in range(-1 * self.stepRange, self.stepRange + 1, self.stepRange):
                if i == 0 and j == 0:
                    continue

                possibleMove = Point(current.x + i, current.y + j)
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

    """
    @abstractmethod
    def drawShapeOrg(Graphics g, Color color):

    protected void drawOrg(Graphics g, Color color) {
        drawShapeOrg(g, color)

        g.setColor(Color.white)
        g.setFont(new Font("Helvetica", Font.BOLD, 25))
        FontMetrics metrics = world.getFontMetrics(g.getFont())
        double x = ((double)(2 * point.x + 1) * FIELD_SIZE) / 2
        double y = ((double)(2 * point.y + 2) * FIELD_SIZE) / 2
        g.drawString(sign, (int)(x - (metrics.stringWidth(sign) / 2)),
                     (int)(y - (g.getFont().getSize() / 2)) + 4)
    }

    public void writeMeToFile(BufferedWriter writer) throws IOException {
        writer.write(sign + DELIMITER + point.x + DELIMITER +
                     point.y + DELIMITER + birthTime + DELIMITER + strength)
        myOwnFieldsToFile(writer)
        writer.newLine()
    }

    protected void myOwnFieldsToFile(BufferedWriter writer) throws IOException {
    }
    """
