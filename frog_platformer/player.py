import pygame

class Player:
    _GRAVITY = 0.7
    _JUMP_SPEED = -17
    _SPEED = 8

    def __init__(self, game):
        self._game = game

        self._IMG_SIT = pygame.image.load("assets/frog_sit").convert_alpha()
        self._IMG_SIT = pygame.transform.rotozoom(self._IMG_SIT, 0, .25)

        self._IMG_JUMP = pygame.image.load("assets/frog_jump").convert_alpha()

        self._img = self._IMG_SIT

        self._rect = self._IMG_SIT.get_rect()
        self._rect.center = (game.SCREEN_WIDTH // 2, game.SCREEN_HEIGHT - 150)

        self._direction = pygame.math.Vector2(0, 0)
        
    
    def set_xdir(self, xdir):
        self._direction.x = xdir

    def jump(self):
        self._direction.y = self._JUMP_SPEED
    
    def apply_gravity(self):
        self._direction.y += self._GRAVITY
        self._rect.y += self._direction.y

        # REPLACE THIS IF STATEMENT FOR CHECKING PLATFORM COLLISIONS
        if self._rect.bottom < 300: 
            self._img = self._IMG_JUMP
            self._img = pygame.transform.rotozoom(self._img,0,.18)
      
        else:
            self._img = self._IMG_SIT
        
        #delete line below for platform game
        if self._rect.bottom >= 300: self._rect.bottom = 300
    
    def update_pos(self):
        self.apply_gravity()
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
    