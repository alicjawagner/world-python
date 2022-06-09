import plant
import organismsNames


class Guarana(plant.Plant):

    def __init__(self, _world, arr=None):
        super().__init__(_world, arr)
        self.name = "Guarana"
        self.sign = "u"
        if arr == None:
            self.strength = 0

    def ifILostTheFight(self, attacker):
        if super().ifILostTheFight(attacker):
            attacker.strength += 3
            return True
        return False

    def writeIDie(self):
        self.world.text += self.name + " is dead :( (+3)\n"

    def whoAmI(self):
        return organismsNames.OrganismsNames.GUARANA

    # def draw(Graphics g):
    #    drawOrg(g, new Color(126, 200, 80))
