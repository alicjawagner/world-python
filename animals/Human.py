import Animal
import OrganismsNames
import Point


class Human(Animal):

    START_POTION = 5
    COUNTDOWN_POTION = 10
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4
    STAY = 5

    def __init__(self, _world, arr=None):
        super().__init__(_world, arr)
        self.name = "Human"
        self.initiative = 4
        self.sign = "H"
        self.nextMove = Human.STAY
        self.potionText = ""
        if arr == None:
            self.strength = 5
            self.potionWorking = 0
            self.potionCountdown = 0
        else:
            self.potionWorking = int(arr[5])
            self.potionCountdown = int(arr[6])

    def setNextMove(self, _nextMove):
        self.nextMove = _nextMove

    def startElixir(self):
        if self.potionCountdown == 0:
            self.potionText = "Magic potion increased your strength by 5!"
            self.potionWorking = Human.START_POTION
            self.potionCountdown = Human.COUNTDOWN_POTION
            self.strength += 5
        else:
            self.potionText = "You can't drink the potion yet."

    def countDownPotion(self):
        if self.potionWorking > 0:
            self.potionWorking -= 1
            self.potionCountdown -= 1
            self.strength -= 1
        elif self.potionCountdown > 0:
            self.potionCountdown -= 1

    def action(self):
        if self.isAlive == False:
            return

        if self.potionCountdown > 0:
            self.countDownPotion()

        newPoint = Point(self.point.x, self.point.y)
        if self.nextMove == Human.UP:
            newPoint.y = self.point.y - 1
        elif self.nextMove == Human.DOWN:
            newPoint.y = self.point.y + 1
        elif self.nextMove == Human.LEFT:
            newPoint.x = self.point.x - 1
        elif self.nextMove == Human.RIGHT:
            newPoint.x = self.point.x + 1
        elif self.nextMove == Human.STAY:
            return

        if self.world.isFieldInBoard(newPoint):
            self.makeMoveOrCollision(newPoint)

    def whoAmI(self):
        return OrganismsNames.HUMAN

    def resetPotionText(self):
        self.potionText = ""

    """
    def draw(Graphics g):
        drawShapeOrg(g, Color.red)

        g.setColor(Color.black)
        g.setFont(new Font("Helvetica", Font.BOLD, 31))
        FontMetrics metrics = world.getFontMetrics(g.getFont())
        double x = ((double)(2 * point.x + 1) * FIELD_SIZE) / 2
        double y = ((double)(2 * point.y + 2) * FIELD_SIZE) / 2
        g.drawString(String.valueOf(sign), (int)(
            x - (metrics.stringWidth(String.valueOf(sign)) / 2)) + 1, (int)(y - (g.getFont().getSize() / 2)) + 9)

    def myOwnFieldsToFile(BufferedWriter writer) throws IOException {
        writer.write(DELIMITER + potionWorking + DELIMITER + potionCountdown)
    }
    """
