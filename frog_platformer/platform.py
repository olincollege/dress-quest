import pygame

class Platform(pygame.sprite.Sprite):
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
        self.rect.y += speed
    
    def check_remove(self, screen_height):
        if self.rect.top > screen_height:
            self.kill()

    @property
    def image(self):
        return self._IMG
