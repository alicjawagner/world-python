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
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        print("right pressed")
                    elif event.key == pygame.K_UP:
                        self.world.human = None
                    elif event.key == pygame.K_DOWN:
                        self.world.nextRound()

            self.drawWorld()
            pygame.display.update()
    
    def drawWorld(self):
        self.world.screen.fill((0, 0, 0))
        for org in self.world.organisms:
            org.draw()

        #drawComments(g);

        if self.world.human == None:
            self.gameOver()


    """

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
  """
    def gameOver(self):
        
        alphaRect = pygame.Surface((self.world.SCREEN_WIDTH, self.world.SCREEN_HEIGHT), pygame.SRCALPHA)
        color = (0, 0, 0, 170)
        pygame.draw.rect(alphaRect, color, (0, 0, self.world.SCREEN_WIDTH, self.world.SCREEN_HEIGHT))
        self.world.screen.blit(alphaRect, (0, 0))

        gameOver = "Game Over"
        textFont = pygame.font.SysFont('Times New Roman', 55)
        textSurface = textFont.render(gameOver, False, (255, 0, 0))
        self.world.screen.blit(textSurface, (self.world.SCREEN_WIDTH/2 - 120, self.world.SCREEN_HEIGHT/2 - 60))
