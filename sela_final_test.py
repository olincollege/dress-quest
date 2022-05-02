
# Import and initialize the pygame library
import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    KEYDOWN,
)

pygame.init()

bottoms = ['sela_test_images/invisible.png', 'clothes/black_bottom.png', 'clothes/blue_bottom.png', 'clothes/creep_bottom.png', 'clothes/fish_bottom.png', 'clothes/flannel_bottom.png', \
'clothes/grey_bottom.png', 'clothes/net_bottom.png', 'clothes/rainbow_bottom.png', 'clothes/red_bottom.png', 'clothes/thigh_bottom.png', 'clothes/yellow_bottom.png']
bottom_coords = [(0,0), (10,500), (20,100), (30,0), (40,0), (50,0), (60,0), (70,0), (80,0), (90,0), (10,0), (100,0)]
tops = ['sela_test_images/invisible.png', 'clothes/blue_top.png', 'clothes/flag_top.png', 'clothes/flannel_top.png', 'clothes/ocean_top.png', 'clothes/pearl_top.png', 'clothes/rainbow_top.png', \
'clothes/red_top.png', 'clothes/tank_top.png', 'clothes/tie_top.png']
top_coords = [(0,0), (10,500), (20,100), (30,0), (40,0), (50,0), (60,0), (70,0), (80,0), (90,0), (10,0), (100,0)]
hats = ['sela_test_images/invisible.png', 'clothes/cap_hat.png', 'clothes/cat_hat.png', 'clothes/cow_hat.png', 'clothes/horn_hat.png', 'clothes/straw_hat.png', 'clothes/sun_hat.png', \
'clothes/unicorn_hat.png']
hat_coords = [(0,0), (10,500), (20,100), (30,0), (40,0), (50,0), (60,0), (70,0), (80,0), (90,0), (10,0), (100,0)]


i_hat = 0
i_top = 0
i_bottom = 0
selector_list = [hats, tops, bottoms]

selector = 0
arrow_list = ['sela_test_images/top_select.png', 'sela_test_images/mid_select.png', 'sela_test_images/bottom_select.png']
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)

class Outfit():
    """
    """


    def __init__(self):
        self.bottom = bottoms[0]
        self.top = tops[0]
        self.hat = hats[0]
        self.bottom_coords_index = 0
        self.top_coords_index = 0
        self.hat_coords_index = 0

    def change_right(self, index, clothes_type):
        self.clothes_list = clothes_type
        if clothes_type == hats:
            new_index = outfit.set_change_right(index)
            self.hat = self.clothes_list[index]
            self.hat_coords_index = new_index
        if clothes_type == tops:
            new_index = outfit.set_change_right(index)
            self.top = self.clothes_list[index]
            self.top_coords_index = new_index
        if clothes_type == bottoms:
            new_index = outfit.set_change_right(index)
            self.bottom = self.clothes_list[index]
            self.bottom_coords_index = new_index
        return new_index

    def set_change_right(self, index):
        if index + 1 >= len(self.clothes_list):
            index = 0
        else: index += 1
        return index

    def change_left(self, index, clothes_type):
        self.clothes_list = clothes_type
        if clothes_type == hats: 
            new_index = outfit.set_change_left(index)
            self.hat = self.clothes_list[index]
            self.hat_coords_index = new_index
        if clothes_type == tops:
            new_index = outfit.set_change_left(index)
            self.top = self.clothes_list[index]
            self.top_coords_index = new_index
        if clothes_type == bottoms: 
            new_index = outfit.set_change_left(index)
            self.bottom = self.clothes_list[index]
            self.bottom_coords_index = new_index
        return new_index

    def set_change_left(self, index):
        if index == 0:
            index = len(self.clothes_list) - 1
        else: index -= 1
        return index

    def show_clothes(self):
        bottom_image = pygame.image.load(self.bottom)
        top_image = pygame.image.load(self.top)
        hat_image = pygame.image.load(self.hat)
        # screen.blit(bottom_image, bottom_coords[self.bottom_coords_index])
        screen.blit(bottom_image, (0,0))
        screen.blit(top_image, top_coords[self.top_coords_index])
        screen.blit(hat_image, hat_coords[self.hat_coords_index])



# Set up the drawing window
screen = pygame.display.set_mode([500, 668])
background = pygame.image.load('sela_test_images/back_bg_layer.png')
foreground = pygame.image.load('sela_test_images/front_bg_layer.png')

outfit = Outfit()

# Run until the user asks to quit
running = True
while running:
    
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        outfit.show_clothes()
        if event.type == KEYDOWN:
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_UP]:
                if selector == 0: selector = 2
                else: selector -= 1
            if pressed_keys[K_DOWN]:
                if selector == 2: selector = 0
                else: selector += 1
            clothing = selector_list[selector]
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_RIGHT]:
                if selector == 2: i_bottom = outfit.change_right(i_bottom, clothing)
                if selector == 1: i_top = outfit.change_right(i_top, clothing)
                if selector == 0: i_hat = outfit.change_right(i_hat, clothing)
            if pressed_keys[K_LEFT]:
                if selector == 2: i_bottom = outfit.change_left(i_bottom, clothing)
                if selector == 1: i_top = outfit.change_left(i_top, clothing)
                if selector == 0: i_hat = outfit.change_left(i_hat, clothing)
            #selector_list[selector[1]] = i

            print(selector)
            print(i_hat, i_bottom, i_top)
    
    screen.blit(background, (0,0))
    screen.blit(foreground, (0,0))
    screen.blit(pygame.image.load(arrow_list[selector]), (0,0))
    #print(outfit.bottom)

    outfit.show_clothes()
    
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
