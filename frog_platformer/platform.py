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
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self._IMG = pygame.image.load("assets/rect.png").convert_alpha()
        
        self.width = 100
        self.height = 20
        self._IMG = pygame.transform.scale(self._IMG, (self.width, self.height))
        
        self.rect = self._IMG.get_rect()
        self.rect.x = x
        self.rect.y = y

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
        return self._IMG
