import pygame

def show_loading_screen(win, width, height):
    pygame.init()
    pygame.display.init()

    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    background_image = pygame.image.load("imgs/game-background-4956017_1280.jpg")
    background_image = pygame.transform.scale(background_image, (width, height))

    loading_text = "Loading..."
    font = pygame.font.SysFont("comicsans", 44)
    loading_text = font.render(loading_text, True, (255, 255, 255))
    text_rect = loading_text.get_rect(center=(width // 2, height // 2))

    win.blit(background_image, (0, 0))
    win.blit(loading_text, text_rect)

    pygame.display.update()

    # Play the audio
    pygame.mixer.init()
    pygame.mixer.music.load("sounds/start-computeraif-14572.mp3")
    pygame.mixer.music.play(-1)

    # Wait for 4 seconds
    start_time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - start_time < 4000:
        clock.tick(60)  # Adjust the frame rate as needed

    pygame.quit()

show_loading_screen(pygame.display.set_mode((800, 600)), 800, 600)
