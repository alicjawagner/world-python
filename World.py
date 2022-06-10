import animals.fox as fox
import animals.human as human
import animals.antelope as antelope
import animals.sheep as sheep
import animals.cyberSheep as cyberSheep
import animals.turtle as turtle
import animals.wolf as wolf
import plants.dandelion as dandelion
import plants.deadlyNightshade as deadlyNightshade
import plants.grass as grass
import plants.guarana as guarana
import plants.pineBorscht as pineBorscht
import organismsNames as organismsNames


class World:

    TEXT_FIELD_WIDTH = 303
    BOARD_SIZE = 700
    FIELD_SIZE = 35
    # 20 - how many fields each dimension
    FIELDS_NUMBER = int(BOARD_SIZE / FIELD_SIZE)
    SCREEN_WIDTH = BOARD_SIZE + TEXT_FIELD_WIDTH
    SCREEN_HEIGHT = BOARD_SIZE
    INITIAL_NUMBER_OF_ORGANISMS_OF_SPECIES = 3
    PATH_TO_SAVES = ".\\src\\game\\saves\\"
    INSTRUCTIONS = "MOVEMENT: arrows\nMAGIC POTION (strength +5): P\nNEW ROUND: N\nSAVE: S\nLOAD: L\n\n"

    def __init__(self):
        self.text = World.INSTRUCTIONS
        self.board = [[None for x in range(World.FIELDS_NUMBER)]
                      for y in range(World.FIELDS_NUMBER)]
        self.organisms = []
        self.toAdd = []
        self.numberOfBornOrganisms = 0
        self.human = None
        self.screen = None
        self.textFont = None
        self.prepareWorld()

    def isFieldInBoard(self, point):
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
        if which == organismsNames.OrganismsNames.FOX:
            o = fox.Fox(self)
        elif which == organismsNames.OrganismsNames.WOLF:
            o = wolf.Wolf(self)
        elif which == organismsNames.OrganismsNames.SHEEP:
            o = sheep.Sheep(self)
        elif which == organismsNames.OrganismsNames.ANTELOPE:
            o = antelope.Antelope(self)
        elif which == organismsNames.OrganismsNames.HUMAN:
            if self.human == None:
                o = human.Human(self)
                self.human = o
        elif which == organismsNames.OrganismsNames.TURTLE:
            o = turtle.Turtle(self)
        elif which == organismsNames.OrganismsNames.GRASS:
            o = grass.Grass(self)
        elif which == organismsNames.OrganismsNames.DANDELION:
            o = dandelion.Dandelion(self)
        elif which == organismsNames.OrganismsNames.GUARANA:
            o = guarana.Guarana(self)
        elif which == organismsNames.OrganismsNames.DEADLY_NIGHTSHADE:
            o = deadlyNightshade.DeadlyNightshade(self)
        elif which == organismsNames.OrganismsNames.PINE_BORSCHT:
            o = pineBorscht.PineBorscht(self)
        elif which == organismsNames.OrganismsNames.CYBERSHEEP:
            o = cyberSheep.CyberSheep(self)
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

    def prepareWorld(self):
        for org in organismsNames.OrganismsNames:
            for i in range(World.INITIAL_NUMBER_OF_ORGANISMS_OF_SPECIES):
                if (org == organismsNames.OrganismsNames.HUMAN):
                    self.createAndAddOrganism(
                        organismsNames.OrganismsNames.HUMAN)
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
