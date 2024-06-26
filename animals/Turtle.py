import animal
import organismsNames
import random


class Turtle(animal.Animal):

    PROBABILITY_NOT_MOVING = 75

    def __init__(self, _world, arr=None):
        super().__init__(_world, arr)
        self.name = "Turtle"
        self.initiative = 1
        self.sign = "T"
        if arr == None:
            self.strength = 2

    def ifIRepelledTheAttack(self, attacker):
        if attacker.strength < 5:
            self.world.text += str(self) + " repelled the attack: "
            return True
        return False

    def action(self):
        if random.randrange(100) < Turtle.PROBABILITY_NOT_MOVING:
            return
        super().action()

    def whoAmI(self):
        return organismsNames.OrganismsNames.TURTLE

    def draw(self):
        self.drawOrg((138, 154, 91))
