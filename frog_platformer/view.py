import pygame

class View():
    def __init__(self, game, player):
        self._game = game
        self._player = player
        self._BG_IMG = pygame.image.load("assets/bg.jpg").convert_alpha()
    
    def draw_bg(self):
        self._game.screen.blit(self._BG_IMG, (0, 0))
    
    def draw_player(self):
        self._game.screen.blit(self._player.img, self._player.rect)

    def update(self):
        pygame.display.update()

    
