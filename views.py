'''
Contains the classes for the view of both the dress up and platform games.
'''
import pygame

class DG_View:
    """
    View for the dress up game, contains functions for updating the display.

    Attributes:
        ARROWS: a list of strings for the images for the display arrows
        BG_IMG: a pygame Surface representing the loaded background image
        FG_IMG: a pygame Surface representing the loaded foreground image
        instructions_img: a pygame Surface representing the loaded
            instructions image, changes when start instructions are closed
    """
    ARROWS = [
            'sela_test_images/top_select.png', \
            'sela_test_images/mid_select.png', \
            'sela_test_images/bottom_select.png'
    ]

    def __init__(self, game, player):
        self._game = game
        self._player = player

        self.BG_IMG = pygame.image.load('sela_test_images/back_bg_layer.png')
        self.FG_IMG = pygame.image.load('sela_test_images/front_bg_layer.png')
        self.instructions_img = pygame.image.load('sela_test_images/instructions.png')

    def draw_bg(self):
        """
        Draw the background for the game in the pygame window.
        """
        self._game.screen.blit(self.BG_IMG, (0, 0))
        self._game.screen.blit(self.FG_IMG, (0, 0))

    def draw_clothes(self):
        """
        Draw the clothes the frog is wearing in the pygame window.
        """
        for i in range(3):
            self._game.screen.blit(self._player.images[i], \
                self._player.coords[i])

    def draw_instructions(self):
        """
        Display the correct instructions in the pygame window.

        If the start instructions have been closed, switch to displaying
        the instructions for continuing.
        """
        if not self._game.show_instructions:
            self.instructions_img = \
                pygame.image.load('sela_test_images/enter_instruct.png')
        self._game.screen.blit(self.instructions_img, (0, 0))

    def draw_arrows(self):
        """
        Display the highlighted arrow to show which article of clothing
        is being changed.
        """
        if not self._game.show_instructions:
            self._game.screen.blit(pygame.image.load(\
                self.ARROWS[self._game.item]), (0, 0))

    def update(self):
        """
        Update the display.
        """
        pygame.display.update()


class FP_View():
    """
    View for the platformer, contains functions for updating the display.
    """
    def __init__(self, game, player, platforms):
        self._game = game
        self._player = player
        self._platforms = platforms
        self._BG_IMG = pygame.image.load("assets/tree_background.png").convert_alpha()

    def draw_bg(self):
        """
        Draw the background for the game.
        """
        self._game.screen.blit(self._BG_IMG, (0, 0))

    def draw_player(self):
        """
        Draw the player for the game.
        """
        self._game.screen.blit(self._player.img, self._player.rect)

    def draw_platforms(self):
        """
        Draw the platforms for the game.
        """
        self._platforms.group.draw(self._game.screen)

    def update(self):
        """
        Update the display window.
        """
        pygame.display.update()
