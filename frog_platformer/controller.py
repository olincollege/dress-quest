import pygame

class Controller():
    def __init__(self, game, player):
        self._game = game
        self._player = player
    
    def move_x(self):
        dx = 0

        # process keypresses
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            dx = -10
        if key[pygame.K_d]:
            dx = 10

        # check screen edge
        if self._player.rect.left + dx < 0:
            dx = -self._player.rect.left
        if self._player.rect.right + dx > 400:
            dx = 400 - self._player.rect.right
        
        # update player position
        self._player.move_x(dx)