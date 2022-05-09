'''
Contains the classes for creating and controlling game platforms.
'''

import random
import pygame


class Platform(pygame.sprite.Sprite):
    """
    Platform to be jumped on within the platformer.

    Attributes:
        _IMG: a pygame surface representing the image for the platform
        width: an int representing the width of the platform
        height: an int representing the height of the platform
        rect: a pygame rect that holds the platform's location and controls
            collisions with it
    """

    def __init__(self, x_init, y_init):
        pygame.sprite.Sprite.__init__(self)
        self.IMG = pygame.image.load("assets/platform.png").convert_alpha()

        self.width = 100
        self.height = 20
        self.IMG = pygame.transform.scale(
            self.IMG, (self.width, self.height))

        self.rect = self.IMG.get_rect()
        self.rect.x = x_init
        self.rect.y = y_init

    def move(self, speed):
        """
        Move the platform down the screen.

        Args:
            speed: the amount the platform should move
        """
        self.rect.y += speed

    def check_remove(self, screen_height):
        """
        Check if the platform has left the screen and kill it if it has.

        Args:
            screen_height: an int representing the height of the screen, which
                is the point at which the platform needs to be killed
        """
        if self.rect.top > screen_height:
            self.kill()

    @property
    def image(self):
        """
        Returns a pygame surface representing the image for the platform.
        """
        return self.IMG


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
        platform = Platform(self._game.SCREEN_WIDTH // 2,
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
            p_x = random.randint(0,
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
