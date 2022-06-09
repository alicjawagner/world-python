import plant
import organismsNames


class Dandelion(plant.Plant):

    def __init__(self, _world, arr=None):
        super().__init__(_world, arr)
        self.name = "Dandelion"
        self.sign = "d"
        if arr == None:
            self.strength = 0

    def action(self):
        for i in range(3):
            super().action()

    def whoAmI(self):
        return organismsNames.OrganismsNames.DANDELION

    def draw(self):
        self.drawOrg((245, 187, 0))
