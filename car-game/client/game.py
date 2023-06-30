import pygame
from utility.utils import scale_image, blit_rotate_center, blit_text_center
from views.car import PlayerCar, ComputerCar
from core.game_info import GameInfo
from Resource.loading import show_loading_screen

pygame.font.init()

class Game:
    def __init__(self, win, width, height):
        self.win = win
        self.width = width
        self.height = height
        self.clock = pygame.time.Clock()
        self.images = []
        self.player_car = None
        self.computer_car = None
        self.game_info = None
        self.TRACK_BORDER_MASK = None
        self.FINISH_MASK = None
        self.FINISH_POSITION = (130, 250)  # Add this line

        self.setup()

    def setup(self):
        GRASS = scale_image(pygame.image.load("imgs/grass.jpg"), 2.5)
        TRACK = scale_image(pygame.image.load("imgs/track.png"), 0.9)
        TRACK_BORDER = scale_image(pygame.image.load("imgs/track-border.png"), 0.9)
        FINISH = pygame.image.load("imgs/finish.png")
        PATH = [(175, 119), (110, 70), (56, 133), (70, 481), (318, 731), (404, 680), (418, 521), (507, 475), (600, 551), (613, 715), (736, 713),
        (734, 399), (611, 357), (409, 343), (433, 257), (697, 258), (738, 123), (581, 71), (303, 78), (275, 377), (176, 388), (178, 260)]

        self.images = [(GRASS, (0, 0)), (TRACK, (0, 0)), (FINISH, self.FINISH_POSITION), (TRACK_BORDER, (0, 0))]
        self.TRACK_BORDER_MASK = pygame.mask.from_surface(TRACK_BORDER)
        self.FINISH_MASK = pygame.mask.from_surface(FINISH)
        self.player_car = PlayerCar(4, 4)
        self.computer_car = ComputerCar(2, 4, PATH)
        self.game_info = GameInfo()

    def draw(self):
        for img, pos in self.images:
            self.win.blit(img, pos)

        level_text = pygame.font.SysFont("comicsans", 44).render(f"Level {self.game_info.level}", 1, (255, 255, 255))
        self.win.blit(level_text, (10, self.height - level_text.get_height() - 70))

        time_text = pygame.font.SysFont("comicsans", 44).render(f"Time: {self.game_info.level_time}s", 1, (255, 255, 255))

        self.win.blit(time_text, (10, self.height - time_text.get_height() - 40))

        vel_text = pygame.font.SysFont("comicsans", 44).render(f"Vel: {round(self.player_car.vel, 1)}px/s", 1, (255, 255, 255))
        self.win.blit(vel_text, (10, self.height - vel_text.get_height() - 10))

        self.player_car.draw(self.win)
        self.computer_car.draw(self.win)
        pygame.display.update()

    def move_player(self):
        keys = pygame.key.get_pressed()
        moved = False

        if keys[pygame.K_a]:
            self.player_car.rotate(left=True)
        if keys[pygame.K_d]:
            self.player_car.rotate(right=True)
        if keys[pygame.K_w]:
            moved = True
            self.player_car.move_forward()
        if keys[pygame.K_s]:
            moved = True
            self.player_car.move_backward()

        if not moved:
            self.player_car.reduce_speed()

    def handle_collision(self):
        if self.player_car.collide(self.TRACK_BORDER_MASK) is not None:
            self.player_car.bounce()

        computer_finish_poi_collide = self.computer_car.collide(self.FINISH_MASK, *self.FINISH_POSITION)
        if computer_finish_poi_collide is not None:
            blit_text_center(self.win, pygame.font.SysFont("comicsans", 44), "You lost!")
            pygame.display.update()
            pygame.time.wait(5000)
            self.game_info.reset()
            self.player_car.reset()
            self.computer_car.reset()

        player_finish_poi_collide = self.player_car.collide(self.FINISH_MASK, *self.FINISH_POSITION)
        if player_finish_poi_collide is not None:
            if player_finish_poi_collide[1] == 0:
                self.player_car.bounce()
            else:
                self.game_info.next_level()
                self.player_car.reset()
                self.computer_car.next_level(self.game_info.level)

    def run(self):
        self.setup()

        show_loading_screen(self.win, self.width, self.height)  # Show the loading screen
        pygame.display.update()  # Update the display to show the loading screen

        # Delay for a short time to allow the loading screen to be visible
        pygame.time.delay(1000)

        run = True
        while run:
            self.clock.tick(60)
            self.draw()

            while not self.game_info.started:
                blit_text_center(self.win, pygame.font.SysFont("comicsans", 44),
                                f"Press any key to start level {self.game_info.level}!")
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        break

                    if event.type == pygame.KEYDOWN:
                        self.game_info.start_level()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            self.move_player()
            self.computer_car.move()
            self.handle_collision()

            if self.game_info.game_finished:
                blit_text_center(self.win, pygame.font.SysFont("comicsans", 44), "You won the game!")
                pygame.time.wait(5000)
                self.game_info.reset()
                self.player_car.reset()
                self.computer_car.reset()
