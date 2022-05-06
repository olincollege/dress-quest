import pygame

class Game:
    SCREEN_WIDTH = 400
    SCREEN_HEIGHT = 500

    FPS = 60
    # SCROLL_THRESH = 200

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, \
            self.SCREEN_HEIGHT))
        pygame.display.set_caption("Dress Quest")

        self.clock = pygame.time.Clock()
        self.running = True
        scroll = 0

    def update(self):
        self.clock.tick(self.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

