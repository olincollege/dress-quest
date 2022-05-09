import pygame
import random
from platform import Platform

class Platforms:
    """
    Controls all the platforms movement around the screen and collisions
    with the player.

    Attributes:
        _MAX_PLATFORMS: the maximum number of platforms to exist at a time
        _PLATFORM_WIDTH: the width of the platforms
        _PLATFORM_SPEED: the speed at which the platforms move down the screen
    """
    _MAX_PLATFORMS = 10
    _PLATFORM_WIDTH = 100
    _PLATFORM_SPEED = 1

    def __init__(self, game):
        self._game = game
        self._group = pygame.sprite.Group()

        # create starting platform
        platform = Platform(self._game.SCREEN_WIDTH // 2, \
            self._game.SCREEN_HEIGHT - 100)
        
        self._group.add(platform)
    
    def scroll(self):
        """
        Scroll by moving all the platforms down the screen.
        """
        for platform in self._group:
            platform.move(self._PLATFORM_SPEED)
            platform.check_remove(self._game.SCREEN_HEIGHT)
    
    def generate(self):
        """
        Generate new platforms as they move off the screen.
        """
        if len(self._group) < self._MAX_PLATFORMS:
            p_x = random.randint(0, \
                self._game.SCREEN_WIDTH - self._PLATFORM_WIDTH)
            p_y = self._group.sprites()[-1].rect.y - random.randint(80, 120)
            platform = Platform(p_x, p_y)
            self._group.add(platform)

    @property
    def group(self):
        """
        Return the platform group.
        """
        return self._group
