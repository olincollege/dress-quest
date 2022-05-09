"""
Contains classes for the players of both the dress up and platformer games.
"""

import pygame
from clothing import hats, tops, bottoms


class DgPlayer:
    """
    Player for the dress up game, holds info on outfit being worn.

    Attributes:
        i_hat: the index of the hat being worn in the hat list
        i_top: the index of the top being worn in the top list
        i_bottom: the index of the bottom being worn in the bottom list

        _hat_img: the image of the hat being worn
        _top_img: the image of the top being worn
        _bottom_img: the image of the bottom being worn

        _hat_coords: the coordinates of the hat being worn
        _top_coords: the coordinates of the top being worn
        _bottom_coords: the coordinates of the bottom being worn
    """

    def __init__(self):
        self.i_hat = 0
        self.i_top = 0
        self.i_bottom = 0

        self.update_outfit()
        self.update_coords()

    def change_outfit(self, item, direction):
        """
        Change which article of clothing is being worn.

        Args:
            item: an int representing the item of clothing being changed,
                0 for the hat, 1 for the top, and 2 for the bottom
            dir: the direction in which to move within the item list to
                get the next article of clothing based on which arrow key
                is pressed
        """
        if item == 0:
            self.i_hat += direction
            self.i_hat %= len(hats)
        elif item == 1:
            self.i_top += direction
            self.i_top %= len(tops)
        else:
            self.i_bottom += direction
            self.i_bottom %= len(bottoms)

        self.update_outfit()
        self.update_coords()

    def update_outfit(self):
        """
        Update the images to correctly show the outfit being worn.
        """
        self._hat_img = pygame.image.load(hats[self.i_hat][0])
        self._top_img = pygame.image.load(tops[self.i_top][0])
        self._bottom_img = pygame.image.load(bottoms[self.i_bottom][0])

    def update_coords(self):
        """
        Update the coordinates to correctly show the outfit being worn.
        """
        self._hat_coords = hats[self.i_hat][1]
        self._top_coords = tops[self.i_top][1]
        self._bottom_coords = bottoms[self.i_bottom][1]

    @property
    def images(self):
        """
        Returns a list of the images for the clothing items being worn.
        """
        return [self._hat_img, self._top_img, self._bottom_img]

    @property
    def coords(self):
        """
        Returns a list of the coordinates for the clothing items being worn.
        """
        return [self._hat_coords, self._top_coords, self._bottom_coords]


class FpPlayer:
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
    GRAVITY = .125
    JUMP_SPEED = -5
    SPEED = 8

    def __init__(self, game):
        self._game = game

        self.IMG_SIT = pygame.image.load("assets/frog_sit").convert_alpha()
        self.IMG_SIT = pygame.transform.rotozoom(self.IMG_SIT, 0, .25)

        self.IMG_JUMP = pygame.image.load("assets/frog_jump").convert_alpha()
        self.IMG_JUMP = pygame.transform.rotozoom(self.IMG_JUMP, 0, .18)

        self._img = self.IMG_SIT

        self.rect = self.IMG_SIT.get_rect()
        self.rect.center = (game.SCREEN_WIDTH // 2, game.SCREEN_HEIGHT - 200)

        self._jump_hitbox = self.IMG_JUMP.get_rect()
        self._jump_hitbox.center = (self.rect.centerx,
                                    self.rect.centery + 25)

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
            hitbox = self.rect
        self.apply_gravity()
        for platform in platforms:
            if platform.rect.colliderect(hitbox):
                if self.rect.bottom <= platform.rect.bottom and \
                        self._direction.y > 0:
                    platform_on = platform
                    self._on_platform = True
        if self._on_platform:
            self._img = self.IMG_SIT
            self.rect.bottom = platform_on.rect.top + 3

    def apply_gravity(self):
        """
        Apply gravity to the frog and change the image to be jumping/falling.
        """
        self._img = self.IMG_JUMP
        self._direction.y += self.GRAVITY
        self.rect.y += self._direction.y

    def update_jump_hitbox(self):
        """
        Update the jump hitbox to match the location of the player based on the
        player rect position.
        """
        self._jump_hitbox.center = (self.rect.centerx, self.rect.centery + 25)

    def update_pos(self, platforms):
        """
        Update the position of the player based on platform collisions,
        gravity, and controller input.
        """
        self.check_collide(platforms)
        self.rect.x += self._direction.x * self.SPEED
        self.update_jump_hitbox()
        self._check_death()

    def _check_death(self):
        """
        Check if the player has gone off the screen and reset if so.
        """
        if self.rect.top > self._game.SCREEN_HEIGHT:
            self.rect.center = (self._game.SCREEN_WIDTH // 2,
                                self._game.SCREEN_HEIGHT - 600)
            self.update_jump_hitbox()
            self._direction.y = self.GRAVITY

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
