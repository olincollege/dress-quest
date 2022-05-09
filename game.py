"""
Contains code for the Game class, which is used to run both the dress up
and platformer games.
"""

import pygame

class Game:
    """
    Class for running the dress up and platformer games, with pygame setup.

    Attributes:
        SCREEN_WIDTH: an int representing the width of the game screen
        SCREEN_HEIGHT: an int representing the height of the game screen
        FPS: an int representing the frames per second

        game_state: a string representing whether the game is in the dress
            up portion or the platformer portion
        running: a boolean representing whether or not the game is running,
            changes to false when the game window is closed
        clock: a pygame Clock used to control the frame rate
        show_instructions: a boolean representing whether or not the
            full screen dress up game instructions are being displayed
        item: an int representing which item (hat, top, or bottom) is being
            changed, will always be 0, 1, or 2
    """
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 668

    FPS = 60

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH,
                                               self.SCREEN_HEIGHT))

        self.running = True
        self.show_instructions = True
        self.game_state = "dressup"
        self.clock = pygame.time.Clock()
        self.item = 0
        self.events = []

    def update(self):
        """
        Check for pygame events to transition between game states and control
        the frame rate.

        If the window is closed, quit the game.
        If the space bar is pressed, hide the instructions.
        If the return key is pressed, transition from dress up to platformer.
        """

        if self.game_state == "platformer":
            self.clock.tick(self.FPS)

        self.events = pygame.event.get()
        for event in self.events:
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.show_instructions = False
                if event.key == pygame.K_RETURN:
                    self.game_state = "platformer"
