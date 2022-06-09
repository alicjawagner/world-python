import organism
import random
import pygame


class Plant(organism.Organism):

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

    def drawShapeOrg(self, color):
        pygame.draw.rect(self.world.screen, color, pygame.Rect(self.point.x * self.world.FIELD_SIZE,
                         self.point.y * self.world.FIELD_SIZE, self.world.FIELD_SIZE, self.world.FIELD_SIZE))
