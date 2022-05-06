import pygame
import random
from platform import Platform

class Platforms:
    _MAX_PLATFORMS = 10
    _PLATFORM_WIDTH = 100
    _PLATFORM_SPEED = 5

    def __init__(self, game):
        self._game = game
        self._group = pygame.sprite.Group()

        # create starting platform
        platform = Platform(self._game.SCREEN_WIDTH // 2, \
            self._game.SCREEN_HEIGHT - 100)
        
        self._group.add(platform)

        '''for p in range(self._MAX_PLATFORMS):
            p_x = random.randint(0, self._game.SCREEN_WIDTH - self._PLATFORM_WIDTH)
            p_y = p * random.randint(80, 120)

            platform = Platform(p_x, p_y)
            self._platform_group.add(platform)'''
    
    def scroll(self):
        for platform in self._group:
            platform.move(self._PLATFORM_SPEED)
            platform.check_remove(self._game.SCREEN_HEIGHT)
    
    def generate(self):
        if len(self._group) < self._MAX_PLATFORMS:
            p_x = random.randint(0, \
                self._game.SCREEN_WIDTH - self._PLATFORM_WIDTH)
            p_y = self._group.sprites()[-1].rect.y - random.randint(80, 120)
            platform = Platform(p_x, p_y)
            self._group.add(platform)

    @property
    def group(self):
        return self._group
