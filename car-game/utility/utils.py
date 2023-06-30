import pygame
from pygame.transform import scale, rotate


def scale_image(img, factor):
    width = img.get_width()
    height = img.get_height()
    size = (width * factor, height * factor)
    return scale(img, size)


def blit_rotate_center(win, image, top_left, angle):
    rotated_image = rotate(image, angle)
    rotated_rect = rotated_image.get_rect(topleft=top_left)
    center = rotated_rect.center
    new_rect = rotated_image.get_rect(center=center)
    win.blit(rotated_image, new_rect.topleft)


def blit_text_center(win, font, text):
    render = font.render(text, True, (200, 200, 200))
    text_rect = render.get_rect(center=win.get_rect().center)
    win.blit(render, text_rect)


# Initialize Pygame
pygame.init()

# Create the Font object
font = pygame.font.Font(None, 24)

# Example usage
win = pygame.display.set_mode((800, 600))
image = pygame.Surface((100, 100))
top_left = (100, 100)
angle = 45
text = "Hello, World!"

scaled_image = scale_image(image, 1.5)
blit_rotate_center(win, scaled_image, top_left, angle)
blit_text_center(win, font, text)

pygame.display.flip()
