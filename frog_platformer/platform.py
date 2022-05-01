import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self._IMG = pygame.image.load("assets/rect.png").convert_alpha()
        self._IMG = pygame.transform.scale(self._IMG, (75, 10))
        
        self.rect = self._IMG.get_rect()
        self.rect.x = x
        self.rect.y = y

    