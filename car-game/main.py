import pygame
import logging
import psutil
from client.game import Game

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

pygame.font.init()

WIDTH = 1080
HEIGHT = 1080
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Come and Race It!")

# Log system metrics
logging.info("System Metrics:")
logging.info(f"CPU Usage: {psutil.cpu_percent()}%")
logging.info(f"Memory Usage: {psutil.virtual_memory().percent}%")


game = Game(WIN, WIDTH, HEIGHT)
game.run()

pygame.quit()
