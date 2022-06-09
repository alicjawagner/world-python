import organism
import random


class Animal(organism.Organism):

    def __init__(self, _world, arr=None):
        super().__init__(_world, arr)

    def isTheSameSpecies(self, other):
        if other == None:
            return False
        return self.name == other.name

    def action(self):
        self.moveToRandField(self.findFieldsToMove())

    def moveToRandField(self, possibleMoves):
        if len(possibleMoves) == 0:
            return
        self.makeMoveOrCollision(
            possibleMoves[random.randrange(len(possibleMoves))])

    def makeMoveOrCollision(self, field):
        if self.world.isFieldUnoccupied(field):
            self.moveToField(field)
        else:
            self.collision(self.world.findOnField(field))

    def collision(self, attacked):
        if self.isTheSameSpecies(attacked):
            self.reproduce(attacked)
        elif attacked.ifIRepelledTheAttack(self):
            self.world.text += self.name + " returned :/\n"
        elif attacked.ifIEscaped(self):
            return
        elif attacked.ifILostTheFight(self):
            self.world.clearTheField(self.point)
            self.point = attacked.point
            self.writeIWon()
            attacked.die()
            self.putOnBoard()
        else:
            attacked.writeIWon()
            self.die()

    def reproduce(self, attacked):
        forChild = self.findFieldsToMove()
        forChild = forChild + attacked.findFieldsToMove()

        self.removeOccupiedFields(forChild)
        if len(forChild) == 0:
            return

        self.makeChild(forChild)
        self.world.text += self.name + " child - parents: (" + str(self.point.x) + "," + str(
            self.point.y) + ") & (" + str(attacked.point.x) + "," + str(attacked.point.y) + ")\n"

    """
    def drawShapeOrg(Graphics g, Color color):
        g.setColor(color)
        g.fillOval(point.x * FIELD_SIZE, point.y * FIELD_SIZE, FIELD_SIZE, FIELD_SIZE)
    """
