import pygame

class Player:
    """
    Player sprite for the platformer game.

    Attributes:
        GRAVITY: an int representing the acceleration due to gravity
        JUMP_SPEED: an int representing the speed at which the player jumps
        SPEED: the speed at which the player moves left and right

        IMG_SIT: a pygame surface representing the loaded frog sitting image
        IMG_JUMP: a pygame surface representing the loaded frog jumping image

        _img: a pygame surface representing the current image to display
            for the frog, based on its state
        
        _rect: a pygame rect representing the position of the player, also
            used for collision detection
        
        _jump_hitbox: a pygame rect used as the player's hitbox when they are
            jumping to ensure the platform collision is accurate to the
            image being displayed

        _direction: a pygame vector representing the x and y speed of the frog

        _on_platform: a boolean representing whether or not the frog is on a
            platform
    """
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
        """
        Set the x direction of the player.

        Args:
            xdir: the x direction for the player to move in
        """
        self._direction.x = xdir

    def jump(self):
        """
        Set the y direction of the player based on the jump speed when
        the player jumps.
        """
        self._direction.y = self.JUMP_SPEED
    
    def check_collide(self, platforms):
        """
        Check for collisions between the player and the platforms and
        update the player movement to reflect that.

        Args:
            platforms: a pygame sprite group that holds all the instances
                of the platform class
        """
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
        """
        Apply gravity to the frog and change the image to be jumping/falling.
        """
        self._img = self.IMG_JUMP
        self._direction.y += self.GRAVITY
        self._rect.y += self._direction.y
    
    def update_jump_hitbox(self):
        """
        Update the jump hitbox to match the location of the player based on the
        player rect position.
        """
        self._jump_hitbox.center = (self._rect.centerx, self._rect.centery + 25)
    
    def update_pos(self, platforms):
        """
        Update the position of the player based on platform collisions,
        gravity, and controller input.
        """
        self.check_collide(platforms)
        self._rect.x += self._direction.x * self.SPEED
        self.update_jump_hitbox()

    @property
    def x_pos(self):
        """
        Return the x position of the player
        """
        return self._rect.x
    
    @property
    def y_pos(self):
        """
        Return the y position of the player
        """
        return self._rect.y
    
    @property
    def img(self):
        """
        Return the image of the player
        """
        return self._img
    
    @property
    def on_platform(self):
        """
        Return whether or not the player is on a platform
        """
        return self._on_platform
    