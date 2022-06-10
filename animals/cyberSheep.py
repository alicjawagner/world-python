import animal
import organismsNames
import math


class CyberSheep(animal.Animal):

    def __init__(self, _world, arr=None):
        super().__init__(_world, arr)
        self.name = "CyberSheep"
        self.initiative = 4
        self.sign = "C"
        if arr == None:
            self.strength = 11

    def collision(self, attacked):
        if attacked.name == "Pine Borscht":
            self.world.clearTheField(self.point)
            self.point = attacked.point
            self.writeIWon()
            attacked.die()
            self.putOnBoard()
        else:
            super().collision(attacked)

    def action(self):
        borschts = self.findAllBorschts()
        if len(borschts) == 0:
            super().action()
            return
        nearestBorscht = self.findSmallestDistance(borschts, self.point)
        possibleMoves = self.findFieldsToMove()
        if len(possibleMoves) == 0:
            return
        bestMove = self.findSmallestDistance(possibleMoves, nearestBorscht)
        self.makeMoveOrCollision(bestMove)

    def findAllBorschts(self):
        borschts = []
        for org in self.world.organisms:
            if org.name == "Pine Borscht":
                borschts.append(org.point)
        return borschts

    def findSmallestDistance(self, listToFind, point):
        nearestPoint = (listToFind[0], 9999999.0)
        for item in listToFind:
            distance = math.hypot(point.x - item.x, point.y - item.y)
            if distance < nearestPoint[1]:
                nearestPoint = (item, distance)
        return nearestPoint[0]

    def whoAmI(self):
        return organismsNames.OrganismsNames.CYBERSHEEP

    def draw(self):
        self.drawOrg((240, 240, 240))
