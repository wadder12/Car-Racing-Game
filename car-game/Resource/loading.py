import pygame

def show_loading_screen(win, width, height):
    loading_text = pygame.font.SysFont("comicsans", 44).render("Loading...", True, (255, 255, 255))
    text_rect = loading_text.get_rect(center=(width // 2, height // 2))

    win.fill((0, 0, 0))
    win.blit(loading_text, text_rect)
    pygame.display.update()
