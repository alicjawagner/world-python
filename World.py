from animals import Fox
from animals import Human
from animals import Antelope
from animals import Sheep
from animals import Turtle
from animals import Wolf
from plants import Dandelion
from plants import DeadlyNightshade
from plants import Grass
from plants import Guarana
from plants import PineBorscht
#import Organism
#import Point
import OrganismsNames


class World:

    TEXT_FIELD_WIDTH = 303
    BOARD_SIZE = 700
    FIELD_SIZE = 35
    # 20 - how many fields each dimension
    FIELDS_NUMBER = (BOARD_SIZE / FIELD_SIZE)
    SCREEN_WIDTH = BOARD_SIZE + TEXT_FIELD_WIDTH
    SCREEN_HEIGHT = BOARD_SIZE
    INITIAL_NUMBER_OF_ORGANISMS_OF_SPECIES = 3
    PATH_TO_SAVES = ".\\src\\game\\saves\\"
    INSTRUCTIONS = """MOVEMENT: arrows
    MAGIC POTION (strength +5): P
    NEW ROUND:  N
    SAVE:       S
    LOAD:       L\n"""

    def __init__(self):
        self.text = World.INSTRUCTIONS
        self.board = [[None for x in range(World.FIELDS_NUMBER)]
                      for y in range(World.FIELDS_NUMBER)]
        self.organisms = []
        self.toAdd = []
        self.numberOfBornOrganisms = 0
        self.human = None
        self.startGame()

    def isFieldInBoard(point):
        return point.x >= 0 and point.x < World.FIELDS_NUMBER and point.y >= 0 and point.y < World.FIELDS_NUMBER

    def isFieldUnoccupied(self, point):
        return self.board[point.x][point.y] == None

    def clearTheField(self, point):
        self.board[point.x][point.y] = None

    def findOnField(self, point):
        return self.board[point.x][point.y]

    def whatIsOnBoard(self, where):
        who = self.board[where.x][where.y]
        if who == None:
            return None
        return who.whoAmI()

    def removeDead(self):
        if len(self.organisms) != 0:
            self.organisms[:] = [org for org in self.organisms if org.isAlive]
        if len(self.toAdd) != 0:
            self.toAdd[:] = [org for org in self.toAdd if org.isAlive]
        if self.human != None and self.human.isAlive == False:
            self.human = None

    # returns index, at which newOrg should be added; if at the end: -1
    def findPlaceInOrganisms(self, newOrg):
        for i in range(len(self.organisms)):
            if self.organisms[i].initiative < newOrg.initiative:
                return i
        return -1

    def insertIntoToAdd(self, newOrg):
        self.toAdd.append(newOrg)

    def createOrganism(self, which):
        if which == OrganismsNames.FOX:
            o = Fox(self)
        elif which == OrganismsNames.WOLF:
            o = Wolf(self)
        elif which == OrganismsNames.SHEEP:
            o = Sheep(self)
        elif which == OrganismsNames.ANTELOPE:
            o = Antelope(self)
        elif which == OrganismsNames.HUMAN:
            if self.human == None:
                o = Human(self)
                self.human = o
        elif which == OrganismsNames.TURTLE:
            o = Turtle(self)
        elif which == OrganismsNames.GRASS:
            o = Grass(self)
        elif which == OrganismsNames.DANDELION:
            o = Dandelion(self)
        elif which == OrganismsNames.GUARANA:
            o = Guarana(self)
        elif which == OrganismsNames.DEADLY_NIGHTSHADE:
            o = DeadlyNightshade(self)
        elif which == OrganismsNames.PINE_BORSCHT:
            o = PineBorscht(self)
        return o

    def addOrganism(self, newOrg):
        if (newOrg == None):
            return

        beforeThat = self.findPlaceInOrganisms(newOrg)
        if (beforeThat == -1):
            self.organisms.append(newOrg)
        else:
            self.organisms.insert(beforeThat, newOrg)

        newOrg.putOnBoard()
        self.numberOfBornOrganisms += 1

    def createAndAddOrganism(self, which):
        self.addOrganism(self.createOrganism(which))

    def startGame(self):
        for org in OrganismsNames:
            for i in range(World.INITIAL_NUMBER_OF_ORGANISMS_OF_SPECIES):
                if (org == OrganismsNames.HUMAN):
                    self.createAndAddOrganism(OrganismsNames.HUMAN)
                    break
                self.createAndAddOrganism(org)

    def nextRound(self):
        self.text = World.INSTRUCTIONS
        if self.human != None:
            self.human.resetPotionText()

        for o in self.organisms:
            if o.isAlive:
                o.action()

        self.removeDead()

        # add waiting organisms to main List
        for o in self.toAdd:
            self.addOrganism(o)
            o.birthTime = self.numberOfBornOrganisms
        self.toAdd.clear()

    """
    def drawWorld(Graphics g) {

        for(int i=0; i < SCREEN_HEIGHT/FIELD_SIZE; i++) {
            g.drawLine(i * FIELD_SIZE, 0, i * FIELD_SIZE, SCREEN_HEIGHT);
            g.drawLine(0, i * FIELD_SIZE, SCREEN_WIDTH, i * FIELD_SIZE); }

        for (Organism o: organisms) {
            o.draw(g); }

        drawComments(g);

        if(human == null) {
            gameOver(g); }
        repaint(); }

    private void drawTextWithNewLines(Graphics g, String text, int x, int y) {
        g.setColor(Color.white);
        for (String line: text.split("\n"))
        g.drawString(line, x, y += g.getFontMetrics().getHeight());}

    private void drawComments(Graphics g) {
        g.setColor(new Color(13, 15, 17))
        int x = SCREEN_WIDTH - TEXT_FIELD_WIDTH
        g.fillRect(x, 0, TEXT_FIELD_WIDTH, SCREEN_HEIGHT)

        g.setFont(new Font("Helvetica", Font.PLAIN, 12))
        drawTextWithNewLines(g, text, x + 5, 3)

        if (human != null) {
            String humanText = human.getPotionText()
            if (!Objects.equals(humanText, ""))
            g.drawString(humanText, x + 5, SCREEN_HEIGHT - 20)
        }
    }

    private void gameOver(Graphics g) {
        String gameOver = "Game Over"
        g.setFont(new Font("Times New Roman", Font.BOLD, 55))
        FontMetrics metrics2 = getFontMetrics(g.getFont())

        g.setColor(new Color(0, 0, 0, 170))
        g.fillRect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

        g.setColor(Color.red)
        g.drawString(gameOver, (SCREEN_WIDTH -
                     metrics2.stringWidth(gameOver))/2, SCREEN_HEIGHT/2)
    }

    @ Override
    public void paintComponent(Graphics g) {
        super.paintComponent(g)
        drawWorld(g)
    }
    """
