"""
coding go brrrrrrrrrrrrr - cla
"""
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

# RECOMMEND PLAY-TESTING TO UNDERSTAND HOW ARROWS / SELECTION WORKS BEFORE LOOKING AT MY CONFUSING CODE

#so each list item is a 2 item list that has [the clothing item, the coordinates of the clothing item]. there is a list for each type of clothing.
bottoms = [['sela_test_images/invisible.png', (0,0)], ['clothes/black_bottom.png', (159, 522)], ['clothes/blue_bottom.png', (142,524)],\
           ['clothes/creep_bottom.png', (142,524)], ['clothes/fish_bottom.png', (115,524)], ['clothes/flannel_bottom.png', (142,524)], \
           ['clothes/grey_bottom.png', (142,524)], ['clothes/net_bottom.png', (126,528)], ['clothes/rainbow_bottom.png', (142,524)],\
           ['clothes/red_bottom.png', (179,529)], ['clothes/thigh_bottom copy.png', (109,526)], ['clothes/yellow_bottom.png', (142,524)]]
#fuck pylint im lazy
tops = [['sela_test_images/invisible.png', (0,0)], ['clothes/blue_top.png', (176,520)], ['clothes/flag_top.png', (192,521)], ['clothes/flannel_top.png', (170,522)], ['clothes/ocean_top.png', (144,523)], ['clothes/pearl_top.png', (198,518)], ['clothes/rainbow_top.png', (177,522)], \
['clothes/red_top.png', (199,537)], ['clothes/tank_top.png', (190,522)], ['clothes/tie_top.png', (240,541)]]
hats = [['sela_test_images/invisible.png', (0,0)], ['clothes/cap_hat.png', (205,435)], ['clothes/cat_hat.png', (190,457)], ['clothes/cow_hat.png', (160,430)], ['clothes/horn_hat.png', (205,432)], ['clothes/straw_hat.png', (165,437)], ['clothes/sun_hat.png', (199,490)], \
['clothes/unicorn_hat.png', (236,440)]]


i_hat = 0 # tracks current hat list index
i_top = 0 # tracks current top list index
i_bottom = 0 # tracks current bottom list index

selector_list = [hats, tops, bottoms] # a list that tracks which clothing type is selected / which row of arrows is active.
selector = 0 # basically to track and change which clothing type is selected in the selector_list list
arrow_list = ['sela_test_images/top_select.png', 'sela_test_images/mid_select.png', 'sela_test_images/bottom_select.png']
# 3 separate arrow images that will give the illusion of a certain row being selected *magic* and they said i couldn't code in photoshop

pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR) # don't need this since there's no mouse action lol but i like the crosshair

class Outfit():
    """
    my one and only class; enjoy :D
    does everything.
    literally everything.
    """


    def __init__(self):
        """
        Attributes:
            bottom_set: the current 2-item list selected from the bottoms list, a "set" of a piece of clothing and it's coords if u will
            top_set: same as above, but with tops
            hat_set: same as above, but with hats

            bottom: the string of the image name of the bottoms piece selected
            top: the string of the image name of the tops piece selected
            hat: the string of the image name of the hats piece selected

            bottom_coords: the coords of the selected bottoms piece
            top_coords: the coords of the selected tops piece
            hat_coords: the coords of the selected hats piece

            clothes_set: generic attribute initialized for later use to track length of the selected clothes type list

        """
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
        # read the doc string lol i suck at naming things

    def change_right(self, index, clothes_type):
        """
        Parameters:
            index: the current i_hat/top/bottom index indicated the selected clothing piece
            clothes_type: the list of the 2-item list that is currently selected

        Attributes:
            clothes_list = the list of the clothes type

        Returns:
            new_index = the new i_hat/top/bottom that will change the selected clothing piece
        """
        self.clothes_list = clothes_type
        if clothes_type == hats:
            new_index = outfit.set_change_right(index)
            self.clothes_set = hats
            self.clothes_list = self.clothes_set[new_index]
            self.hat = self.clothes_list[0] #calls first item, the name string
            self.hat_coords = self.change_coords(new_index) # makes sure the corresponding coords for the clothing piece are used
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
        """
        What actually changes the index.
        """
        if index + 1 >= len(self.clothes_set): # loops list index back to 0 if it exceeds list length
            index = 0
        else: index += 1 # else, adds one to call the next piece of clothing in the list
        return index

# editing to account for calling in lists to lists
    def change_left(self, index, clothes_type):
        """
        the same as change_right... but calls set_change_left instead...
        could i have refactored where there is one change method that has an if statement for left/right?
        y e s
        did i?
        ahahhahaahahhahahhahahha QUICK LOOK A FROG
        
        """
        if clothes_type == hats: 
            new_index = outfit.set_change_left(index)
            self.clothes_set = hats
            self.clothes_list = self.clothes_set[new_index]
            self.hat_coords = self.change_coords(new_index)
            self.hat = self.clothes_list[0]
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
        """
        Does the same as set_change_right, but for the left (woooooooow).
        """
        if index == 0 or index == -8: # loops the index to the last item of the list
            index = -1 # i just changed this to -1: big brain to be last item??
        else: index -= 1
        return index

    def show_clothes(self):
        """
        Updates the outfit being displayed.
        """
        bottom_image = pygame.image.load(self.bottom)
        top_image = pygame.image.load(self.top)
        hat_image = pygame.image.load(self.hat)
        screen.blit(bottom_image, self.bottom_coords)
        screen.blit(top_image, self.top_coords)
        screen.blit(hat_image, self.hat_coords)

    def change_coords(self, index):
        """
        Updates the coords to match the item of clothing being selected
        """
        current_set = self.clothes_set[index]
        coords = current_set[1] # selects the 2nd item in the set from the big list, the coords
        return coords


# Set up the drawing window
screen = pygame.display.set_mode([500, 668])
background = pygame.image.load('sela_test_images/back_bg_layer.png')
foreground = pygame.image.load('sela_test_images/front_bg_layer.png') # don't question it pls, layering images is the ONE thing i can do
instructions = pygame.image.load('sela_test_images/instructions.png')
# an image that is either the instruction screen upon start, of or what says to hit enter when done

outfit = Outfit() # creates instance of Outfit

# Run until the user asks to quit
running = True
while running:
    screen.blit(instructions, (0,0)) # shows instruction screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # checks if the game was quit
            running = False
        outfit.show_clothes() # shows the initial outfit (which is invisible)
        if event.type == KEYDOWN:
            instructions = pygame.image.load('sela_test_images/enter_instruct.png') # makes instructions change to little 'hit enter when done one'
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_UP]: # changes row/selector
                if selector == 0: selector = 2
                else: selector -= 1
            if pressed_keys[K_DOWN]: # changes row/selector
                if selector == 2: selector = 0
                else: selector += 1
            clothing = selector_list[selector] # pulls the current clothing type based on what the selector value is
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_RIGHT]: # calls the outfit change process
                if selector == 2: i_bottom = outfit.change_right(i_bottom, clothing)
                if selector == 1: i_top = outfit.change_right(i_top, clothing)
                if selector == 0: i_hat = outfit.change_right(i_hat, clothing)
            if pressed_keys[K_LEFT]: # calls the outfit change process
                if selector == 2: i_bottom = outfit.change_left(i_bottom, clothing)
                if selector == 1: i_top = outfit.change_left(i_top, clothing)
                if selector == 0: i_hat = outfit.change_left(i_hat, clothing)
            #if enter key is pressed: move on to platformer

    screen.blit(background, (0,0))
    screen.blit(foreground, (0,0))
    screen.blit(pygame.image.load(arrow_list[selector]), (0,0))
    screen.blit(instructions, (0,0)) # order of these are important for layering stuffs whee
    
    outfit.show_clothes()
    
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()

#OH BOY
