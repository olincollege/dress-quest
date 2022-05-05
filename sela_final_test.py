
# Import and initialize the pygame library
from matplotlib.collections import _CollectionWithSizes
import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    KEYDOWN,
)

pygame.init()

#change to dictionary? or a list of tuples?

bottoms = [['sela_test_images/invisible.png', (0,0)], ['clothes/black_bottom.png', (159, 522)], ['clothes/blue_bottom.png', (142,524)], ['clothes/creep_bottom.png', (142,524)], ['clothes/fish_bottom.png', (115,524)], ['clothes/flannel_bottom.png', (142,524)], \
['clothes/grey_bottom.png', (142,524)], ['clothes/net_bottom.png', (126,528)], ['clothes/rainbow_bottom.png', (142,524)], ['clothes/red_bottom.png', (179,529)], ['clothes/thigh_bottom copy.png', (109,526)], ['clothes/yellow_bottom.png', (142,524)]]
tops = [['sela_test_images/invisible.png', (0,0)], ['clothes/blue_top.png', (176,520)], ['clothes/flag_top.png', (192,521)], ['clothes/flannel_top.png', (170,522)], ['clothes/ocean_top.png', (144,523)], ['clothes/pearl_top.png', (198,518)], ['clothes/rainbow_top.png', (177,522)], \
['clothes/red_top.png', (199,537)], ['clothes/tank_top.png', (190,522)], ['clothes/tie_top.png', (240,541)]]
hats = [['sela_test_images/invisible.png', (0,0)], ['clothes/cap_hat.png', (205,435)], ['clothes/cat_hat.png', (190,457)], ['clothes/cow_hat.png', (160,430)], ['clothes/horn_hat.png', (205,432)], ['clothes/straw_hat.png', (165,437)], ['clothes/sun_hat.png', (199,490)], \
['clothes/unicorn_hat.png', (236,440)]]


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
        self.bottom_set = bottoms[0]
        self.top_set = tops[0]
        self.hat_set = hats[0]
        self.bottom = self.bottom_set[0]
        self.top = self.top_set[0]
        self.hat = self.hat_set[0]
        self.bottom_coords = self.bottom_set[1]
        self.top_coords = self.top_set[1]
        self.hat_coords = self.hat_set[1]
        self.clothes_set = ''

    def change_right(self, index, clothes_type):
        self.clothes_list = clothes_type
        if clothes_type == hats:
            new_index = outfit.set_change_right(index)
            self.clothes_set = hats
            self.clothes_list = self.clothes_set[new_index]
            self.hat = self.clothes_list[0] #calls first item, the name string
            self.hat_coords = self.change_coords(new_index)
        if clothes_type == tops:
            new_index = outfit.set_change_right(index)
            self.clothes_set = tops
            self.clothes_list = self.clothes_set[new_index]
            self.top = self.clothes_list[0]
            self.top_coords = self.change_coords(new_index)
        if clothes_type == bottoms:
            new_index = outfit.set_change_right(index)
            self.clothes_set = bottoms
            self.clothes_list = self.clothes_set[new_index]
            self.bottom = self.clothes_list[0]
            self.bottom_coords = self.change_coords(new_index)
        return new_index

    def set_change_right(self, index):
        if index + 1 >= len(self.clothes_set):
            index = 0
        else: index += 1
        return index

# editing to account for calling in lists to lists
    def change_left(self, index, clothes_type):
        if clothes_type == hats: 
            new_index = outfit.set_change_left(index)
            self.clothes_set = hats
            self.clothes_list = self.clothes_set[new_index]
            self.hat_coords = self.change_coords(new_index)
            self.hat = self.clothes_list[0] #calls first item, the name string
        if clothes_type == tops:
            new_index = outfit.set_change_left(index)
            self.clothes_set = tops
            self.clothes_list = self.clothes_set[new_index]
            self.top = self.clothes_list[0]
            self.top_coords = self.change_coords(new_index)
        if clothes_type == bottoms: 
            new_index = outfit.set_change_left(index)
            self.clothes_set = bottoms
            self.clothes_list = self.clothes_set[new_index]
            self.bottom = self.clothes_list[0]
            self.bottom_coords = self.change_coords(new_index)
        return new_index

    def set_change_left(self, index):
        if index == 0 or index == -8:
            index = len(self.clothes_set) - 1
        else: index -= 1
        return index

    def show_clothes(self):
        bottom_image = pygame.image.load(self.bottom)
        top_image = pygame.image.load(self.top)
        hat_image = pygame.image.load(self.hat)
        screen.blit(bottom_image, self.bottom_coords)
        screen.blit(top_image, self.top_coords)
        screen.blit(hat_image, self.hat_coords)

    def change_coords(self, index):
        current_set = self.clothes_set[index]
        coords = current_set[1]
        return coords


# Set up the drawing window
screen = pygame.display.set_mode([500, 668])
background = pygame.image.load('sela_test_images/back_bg_layer.png')
foreground = pygame.image.load('sela_test_images/front_bg_layer.png')
instructions = pygame.image.load('sela_test_images/instructions.png')

outfit = Outfit()

# Run until the user asks to quit
running = True
while running:
    screen.blit(instructions, (0,0))
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        outfit.show_clothes()
        if event.type == KEYDOWN:
            instructions = pygame.image.load('sela_test_images/enter_instruct.png')
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
            #if enter key is pressed: move on to platformer

    screen.blit(background, (0,0))
    screen.blit(foreground, (0,0))
    screen.blit(pygame.image.load(arrow_list[selector]), (0,0))
    screen.blit(instructions, (0,0))
    
    outfit.show_clothes()
    
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
