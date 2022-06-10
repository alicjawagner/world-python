import pygame, sys
from organismsNames import OrganismsNames
import world
import organism
import point
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


class Game:

    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.world = world.World()
        self.world.screen = pygame.display.set_mode((self.world.SCREEN_WIDTH, self.world.SCREEN_HEIGHT))
        self.world.textFont = pygame.font.SysFont('Helvetica', 25)
        pygame.display.set_caption("The World")
        self.savesPath = "./saves/"


    def startGame(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif self.world.human != None and event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.world.human.startElixir()
                        self.world.human.nextMove = self.world.human.STAY
                    elif event.key == pygame.K_LEFT:
                        self.world.human.nextMove = self.world.human.LEFT
                    elif event.key == pygame.K_RIGHT:
                        self.world.human.nextMove = self.world.human.RIGHT
                    elif event.key == pygame.K_UP:
                        self.world.human.nextMove = self.world.human.UP
                    elif event.key == pygame.K_DOWN:
                        self.world.human.nextMove = self.world.human.DOWN
                    elif event.key == pygame.K_n:
                        self.world.nextRound()
                    elif event.key == pygame.K_s:
                        self.saveGameState()
                    elif event.key == pygame.K_l:
                        self.loadGameState()
                elif self.world.human != None and event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    self.handleMouseClick(pos)
            self.drawWorld()
            pygame.display.update()

    
    def drawWorld(self):
        self.world.screen.fill((0, 0, 0))
        for org in self.world.organisms:
            org.draw()
        self.drawComments()
        if self.world.human == None:
            self.gameOver()


    def drawTextWithNewLines(self, text, x, y):
        textFont = pygame.font.SysFont('Helvetica', 14)
        lines = text.split("\n")
        for line in lines:
            textSurface = textFont.render(line, True, (255, 255, 255))
            self.world.screen.blit(textSurface, (x, y))
            y += 18


    def drawComments(self):
        x = self.world.SCREEN_WIDTH - self.world.TEXT_FIELD_WIDTH
        pygame.draw.rect(self.world.screen, (13, 15, 17), pygame.Rect(x, 0,
                        self.world.TEXT_FIELD_WIDTH, self.world.SCREEN_HEIGHT))
        self.drawTextWithNewLines(self.world.text, x + 5, 3)

        if self.world.human != None:
            textFont = pygame.font.SysFont('Helvetica', 16)
            if self.world.human.potionText != "":
                textSurface = textFont.render(self.world.human.potionText, True, (255, 255, 255))
                self.world.screen.blit(textSurface, (x + 5, self.world.SCREEN_HEIGHT - 20))


    def gameOver(self):
        alphaRect = pygame.Surface((self.world.SCREEN_WIDTH, self.world.SCREEN_HEIGHT), pygame.SRCALPHA)
        color = (0, 0, 0, 170)
        pygame.draw.rect(alphaRect, color, (0, 0, self.world.SCREEN_WIDTH, self.world.SCREEN_HEIGHT))
        self.world.screen.blit(alphaRect, (0, 0))

        gameOver = "Game Over"
        textFont = pygame.font.SysFont('Times New Roman', 55, True)
        textSurface = textFont.render(gameOver, True, (255, 0, 0))
        self.world.screen.blit(textSurface, (self.world.SCREEN_WIDTH/2 - 140, self.world.SCREEN_HEIGHT/2 - 45))

    def showInputBox(self, text):
        color = (13, 15, 17)
        w = 300
        h = 80
        x = self.world.SCREEN_WIDTH/2 - w/2
        y = self.world.SCREEN_HEIGHT/2 - 80
        
        pygame.draw.rect(self.world.screen, color, pygame.Rect(x, y, w, h))
        textFont = pygame.font.SysFont('Helvetica', 16)
        textSurface = textFont.render(text, True, (255, 255, 255))
        self.world.screen.blit(textSurface, (x + 20, y + 10))
        inputText = ""

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        inputText = inputText[:-1]
                        pygame.draw.rect(self.world.screen, color, pygame.Rect(x, y + h/2, w, h/2))
                    elif event.key == pygame.K_RETURN:
                        return inputText
                    else:
                        inputText += event.unicode
            inputFont = pygame.font.Font(None, 32)
            inputSurface = inputFont.render(inputText, True, (255, 255, 255))
            self.world.screen.blit(inputSurface, (x + 25, y + 40))
            pygame.display.update()


    def saveGameState(self):
        fileName = self.showInputBox("Saving: enter file name and hit enter")
        self.saveToFile(fileName)

    def saveToFile(self, fileName):
        try:
            f = open(self.savesPath + fileName, "w")
            f.write(str(self.world.numberOfBornOrganisms) + organism.Organism.DELIMITER + str(len(self.world.organisms)) + "\n")
            for org in self.world.organisms:
                org.writeMeToFile(f)
            f.close()
            self.world.text = "Game state saved"
        except:
            self.world.text = "Problem with opening/writing to file"

    def loadGameState(self):
        fileName = self.showInputBox("Loading: enter file name and hit enter")
        self.loadFromFile(fileName)

    def loadFromFile(self, fileName):
        try:
            f = open(self.savesPath + fileName, "r")
            self.world.board = None
            self.world.board = [[None for x in range(self.world.FIELDS_NUMBER)]
                                for y in range(self.world.FIELDS_NUMBER)]
            self.world.human = None
            self.world.organisms.clear()
            self.world.toAdd.clear()

            firstLine = f.readline().strip()
            elements = firstLine.split(organism.Organism.DELIMITER)
            self.world.numberOfBornOrganisms = int(elements[0])

            for line in f:
                line = line.strip().split(organism.Organism.DELIMITER)
                if line[0] == "F":
                    o = fox.Fox(self.world, line)
                elif line[0] == "W":
                    o = wolf.Wolf(self.world, line)
                elif line[0] == "S":
                    o = sheep.Sheep(self.world, line)
                elif line[0] == "C":
                    o = cyberSheep.CyberSheep(self.world, line)
                elif line[0] == "A":
                    o = antelope.Antelope(self.world, line)
                elif line[0] == "H":
                    o = human.Human(self.world, line)
                    self.world.human = o
                elif line[0] == "T":
                    o = turtle.Turtle(self.world, line)
                elif line[0] == "g":
                    o = grass.Grass(self.world, line)
                elif line[0] == "d":
                    o = dandelion.Dandelion(self.world, line)
                elif line[0] == "u":
                    o = guarana.Guarana(self.world, line)
                elif line[0] == "n":
                    o = deadlyNightshade.DeadlyNightshade(self.world, line)
                elif line[0] == "b":
                    o = pineBorscht.PineBorscht(self.world, line)

                self.world.organisms.append(o)
                o.putOnBoard()
            f.close()
            self.world.text = "Game state loaded"
        except:
            self.world.text = "File not found"


    def handleMouseClick(self, pos):
        field = self.getMouseField(pos)
        if field == None:
            return
        if self.world.findOnField(field) == None:
            self.showMenuAndAddOrg(field)

    def getMouseField(self, mouseLocation):
        x = int(mouseLocation[0] / self.world.FIELD_SIZE)
        y = int(mouseLocation[1] / self.world.FIELD_SIZE)
        if x >= self.world.FIELDS_NUMBER or y >= self.world.FIELDS_NUMBER:
            return None
        return point.Point(x, y)

    def showMenuAndAddOrg(self, field):
        buttons = self.createButtons()
        pygame.display.update()
        click = False
        while True:
            mousePos = pygame.mouse.get_pos()
            for key in buttons:
                if buttons[key].collidepoint(mousePos):
                    if click:
                        o = self.world.createOrganism(key)
                        self.world.addOrganism(o)
                        o.moveToField(field)
                        return

            click = False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True


    def createButtons(self):
        color = (13, 15, 17)
        w = 160
        h = 20
        x = self.world.SCREEN_WIDTH/2 - w/2
        y = self.world.SCREEN_HEIGHT/2 - 11*h/2
        textFont = pygame.font.SysFont('Helvetica', 16)
        buttons = {}
        for org in OrganismsNames:
            if (org == OrganismsNames.HUMAN):
                pass
            else:
                buttons[org] = pygame.Rect(x, y, w, h)
                pygame.draw.rect(self.world.screen, color, buttons[org])
                text = str(org).split(".")[1]
                textSurface = textFont.render(text, True, (255, 255, 255))
                self.world.screen.blit(textSurface, (x + 10, y + 2))
                y += h
        return buttons
