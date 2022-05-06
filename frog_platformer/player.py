import pygame

class Player:
    _GRAVITY = .1
    _JUMP_SPEED = -5
    _SPEED = 8

    def __init__(self, game):
        self._game = game

        self._IMG_SIT = pygame.image.load("assets/frog_sit").convert_alpha()
        self._IMG_SIT = pygame.transform.rotozoom(self._IMG_SIT, 0, .25)

        self._IMG_JUMP = pygame.image.load("assets/frog_jump").convert_alpha()
        self._IMG_JUMP = pygame.transform.rotozoom(self._IMG_JUMP, 0, .18)

        self._img = self._IMG_SIT

        self._rect = self._IMG_SIT.get_rect()
        self._rect.center = (game.SCREEN_WIDTH // 2, game.SCREEN_HEIGHT - 200)

        self._direction = pygame.math.Vector2(0, 0)
        
    
    def set_xdir(self, xdir):
        self._direction.x = xdir

    def jump(self):
        self._direction.y = self._JUMP_SPEED
    
    def check_collide(self, platforms):
        self.apply_gravity()
        on_platform = False
        for platform in platforms:
            if platform.rect.colliderect(self.rect):
                if self.rect.bottom < platform.rect.bottom and \
                    self._direction.y > 0:
                    platform_on = platform
                    on_platform = True
        if on_platform:
            self._img = self._IMG_SIT
            self.rect.bottom = platform_on.rect.top
    
    def apply_gravity(self):
        self._img = self._IMG_JUMP
        self._direction.y += self._GRAVITY
        self._rect.y += self._direction.y
    
    def update_pos(self, platforms):
        self.check_collide(platforms)
        self._rect.x += self._direction.x * self._SPEED

    @property
    def x_pos(self):
        return self._rect.x
    
    @property
    def y_pos(self):
        return self._rect.y
    
    @property
    def img(self):
        return self._img
    


    @property
    def rect(self):
        return self._rect
    