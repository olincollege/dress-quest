import pygame

class Player:
    def __init__(self, game):
        self._game = game
        self._IMG = pygame.image.load("assets/ball.png").convert_alpha()
        self._IMG = pygame.transform.scale(self._IMG, (50, 50))

        self._rect = self._IMG.get_rect()
        self._rect.center = (game.SCREEN_WIDTH // 2, game.SCREEN_HEIGHT - 150)
    
    def move_x(self, dx):
        self._rect.x += dx

    @property
    def x_pos(self):
        return self._rect.x
    
    @property
    def y_pos(self):
        return self._rect.y
    
    @property
    def img(self):
        return self._IMG

    @property
    def rect(self):
        return self._rect