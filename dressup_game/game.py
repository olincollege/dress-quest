import pygame

class Game:
    """
    Class for running the dress up game, including pygame setup.

    Attributes:
        SCREEN_WIDTH: an int representing the width of the game screen
        SCREEN_HEIGHT: an int representing the height of the game screen

        running: a boolean representing whether or not the game is running,
            changes to false when the game window is closed
        show_instructions: a boolean representing whether or not the
            full screen dress up game instructions are being displayed
        dress_up_running: a boolean representing whether or not the dress up
            game specifically is running, used to transition to the platformer
        item: an int representing which item (hat, top, or bottom) is being
            changed, will always be 0, 1, or 2
    """
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 668

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, \
            self.SCREEN_HEIGHT))

        self.running = True
        self.show_instructions = True
        self.dress_up_running = True
        
        self.item = 0
    
    def update(self):
        """
        Check for pygame events to transition between game states.

        If the window is closed, quit the game.
        If the space bar is pressed, hide the instructions.
        If the return key is pressed, transition from dress up to platformer.
        """
        self.events = pygame.event.get()
        for event in self.events:
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.show_instructions = False
                if event.key == pygame.K_RETURN:
                    self.dress_up_running = False
