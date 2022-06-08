import Organism
import random


class Plant(Organism):

    PROBABILITY_OF_SPREADING = 15

    def __init__(self, _world, arr=None):
        super().__init__(_world, arr)
        self.initiative = 0

    def action(self):
        if random.randrange(100) < Plant.PROBABILITY_OF_SPREADING:
            possibleMoves = self.findFieldsToMove()
            self.removeOccupiedFields(possibleMoves)

            if len(possibleMoves) == 0:
                return

            self.makeChild(possibleMoves)

    def writeIDie(self):
        self.world.text += self.name + " was eaten :(\n"

    # def drawShapeOrg(Graphics g, Color color):
    #    g.setColor(color)
    #    g.fillRect(point.x * FIELD_SIZE, point.y * FIELD_SIZE, FIELD_SIZE, FIELD_SIZE)
