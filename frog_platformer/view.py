import pygame

class View():
    """
    View for the platformer, contains functions for updating the display.
    """
    def __init__(self, game, player, platforms):
        self._game = game
        self._player = player
        self._platforms = platforms
        self._BG_IMG = pygame.image.load("assets/bg.jpg").convert_alpha()
    
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
