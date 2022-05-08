import pygame

class Game:
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 668
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, \
            self.SCREEN_HEIGHT))

        self.running = True
        self.show_instructions = True
        
        self.item = 0
    
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                self.show_instructions = False