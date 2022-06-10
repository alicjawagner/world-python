import pygame, sys
import world


class Game:

    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.world = world.World()
        self.world.screen = pygame.display.set_mode((self.world.SCREEN_WIDTH, self.world.SCREEN_HEIGHT))
        self.world.textFont = pygame.font.SysFont('Helvetica', 25)
        pygame.display.set_caption("The World")


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

            self.drawWorld()
            pygame.display.update()

    """ case KeyEvent.VK_S:
            saving.saveGameState()
            break
        case KeyEvent.VK_L:
            loading.loadGameState()
    """

    
    def drawWorld(self):
        self.world.screen.fill((0, 0, 0))
        for org in self.world.organisms:
            org.draw()

        self.drawComments()

        if self.world.human == None:
            self.gameOver()


    def drawTextWithNewLines(self, text, x, y):
        textFont = pygame.font.SysFont('Helvetica', 15)
        lines = text.split("\n")
        for line in lines:
            textSurface = textFont.render(line, False, (255, 255, 255))
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
                textSurface = textFont.render(self.world.human.potionText, False, (255, 255, 255))
                self.world.screen.blit(textSurface, (x + 5, self.world.SCREEN_HEIGHT - 20))


    def gameOver(self):
        alphaRect = pygame.Surface((self.world.SCREEN_WIDTH, self.world.SCREEN_HEIGHT), pygame.SRCALPHA)
        color = (0, 0, 0, 170)
        pygame.draw.rect(alphaRect, color, (0, 0, self.world.SCREEN_WIDTH, self.world.SCREEN_HEIGHT))
        self.world.screen.blit(alphaRect, (0, 0))

        gameOver = "Game Over"
        textFont = pygame.font.SysFont('Times New Roman', 55, True)
        textSurface = textFont.render(gameOver, False, (255, 0, 0))
        self.world.screen.blit(textSurface, (self.world.SCREEN_WIDTH/2 - 140, self.world.SCREEN_HEIGHT/2 - 45))
