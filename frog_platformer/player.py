import pygame

class Player:
    GRAVITY = .1
    JUMP_SPEED = -5
    SPEED = 8

    def __init__(self, game):
        self._game = game

        self.IMG_SIT = pygame.image.load("assets/frog_sit").convert_alpha()
        self.IMG_SIT = pygame.transform.rotozoom(self.IMG_SIT, 0, .25)

        self.IMG_JUMP = pygame.image.load("assets/frog_jump").convert_alpha()
        self.IMG_JUMP = pygame.transform.rotozoom(self.IMG_JUMP, 0, .18)

        self._img = self.IMG_SIT

        self._rect = self.IMG_SIT.get_rect()
        self._rect.center = (game.SCREEN_WIDTH // 2, game.SCREEN_HEIGHT - 200)

        self._jump_hitbox = self.IMG_JUMP.get_rect()
        self._jump_hitbox.center = (self._rect.centerx, \
            self._rect.centery + 25)

        self._direction = pygame.math.Vector2(0, 0)
        self._on_platform = False
        
    
    def set_xdir(self, xdir):
        self._direction.x = xdir

    def jump(self):
        self._direction.y = self.JUMP_SPEED
    
    def check_collide(self, platforms):
        self._on_platform = False
        if self._img == self.IMG_JUMP:
            hitbox = self._jump_hitbox
        else:
            hitbox = self._rect
        self.apply_gravity()
        for platform in platforms:
            if platform.rect.colliderect(hitbox):
                if self._rect.bottom <= platform.rect.bottom and \
                    self._direction.y > 0:
                    platform_on = platform
                    self._on_platform = True
        if self._on_platform:
            self._img = self.IMG_SIT
            self._rect.bottom = platform_on.rect.top + 3
    
    def apply_gravity(self):
        self._img = self.IMG_JUMP
        self._direction.y += self.GRAVITY
        self._rect.y += self._direction.y
    
    def update_jump_hitbox(self):
        self._jump_hitbox.center = (self._rect.centerx, self._rect.centery + 25)
    
    def update_pos(self, platforms):
        self.check_collide(platforms)
        self._rect.x += self._direction.x * self.SPEED
        self.update_jump_hitbox()

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
    
    @property
    def on_platform(self):
        return self._on_platform
    