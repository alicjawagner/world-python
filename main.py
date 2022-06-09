import pygame
from game import Game


pygame.init()
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("The World")
g = Game(screen)
g.startGame()