import pygame

class Game:
    """
    Class for running the platformer game, including pygame setup.

    Attributes:
        SCREEN_WIDTH: an int representing the width of the game screen
        SCREEN_HEIGHT: an int representing the height of the game screen
        FPS: an int representing the frames per second

        clock: a pygame Clock used to control the frame rate
        running: a boolean representing whether or not the game is running
        events: a list of the pygame events, such as QUIT when the game
            window is closed
    """
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
