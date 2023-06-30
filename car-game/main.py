import pygame
from client.game import Game

pygame.font.init()

WIDTH = 1080
HEIGHT = 1080
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Come and Race It!")

game = Game(WIN, WIDTH, HEIGHT)
game.run()

pygame.quit()
