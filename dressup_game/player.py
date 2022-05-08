import pygame
from clothing import hats, tops, bottoms

class Player:
    def __init__(self):
        self.i_hat = 0
        self.i_top = 0
        self.i_bottom = 0

        self.update_outfit()
        self.update_coords()
    
    def change_outfit(self, item, dir):
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
        self._hat_img = pygame.image.load(hats[self.i_hat][0])
        self._top_img = pygame.image.load(tops[self.i_top][0])
        self._bottom_img = pygame.image.load(bottoms[self.i_bottom][0])
    
    def update_coords(self):
        self._hat_coords = hats[self.i_hat][1]
        self._top_coords = tops[self.i_top][1]
        self._bottom_coords = bottoms[self.i_bottom][1]
    
    @property
    def images(self):
        return [self._hat_img, self._top_img, self._bottom_img]
    
    @property
    def coords(self):
        return [self._hat_coords, self._top_coords, self._bottom_coords]
