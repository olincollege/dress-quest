import pygame

class Game:
    SCREEN_WIDTH = 400
    SCREEN_HEIGHT = 500

    FPS = 60

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, \
            self.SCREEN_HEIGHT))
        pygame.display.set_caption("Dress Quest")

        self.clock = pygame.time.Clock()
        self.running = True

    def update(self):
        self.clock.tick(self.FPS)

        self.events = pygame.event.get()

        for event in self.events:
            if event.type == pygame.QUIT:
                self.running = False
