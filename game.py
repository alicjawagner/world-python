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

            self.drawWorld()
            pygame.display.update()
    
    def drawWorld(self):
        self.world.screen.fill((0, 0, 0))
        for org in self.world.organisms:
            org.draw()

        #drawComments(g);

        #if(human == null) {
        #    gameOver(g); }


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
        super().paintComponent(g)
        drawWorld(g)
    }
    """
