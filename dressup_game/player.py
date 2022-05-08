import pygame
from clothing import hats, tops, bottoms

class Player:
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
    
    def change_outfit(self, item, dir):
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
            self.i_hat += dir
            self.i_hat %= len(hats)
        elif item == 1:
            self.i_top += dir
            self.i_top %= len(tops)
        else:
            self.i_bottom += dir
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
