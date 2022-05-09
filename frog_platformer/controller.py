import pygame

class Controller():
    """
    Controller for the player sprite in the platformer.

    Attributes:
        _game: the instance of the game being controlled
        _player: the instance of the player being controlled
    """
    def __init__(self, game, player):
        self._game = game
        self._player = player
    
    def move_player(self):
        """
        Takes input from the arrow keys and moves the player around screen.

        The up key causes the player to jump if they're on a platform,
        the right key causes the player to move right, and the left key
        causes the player to move left.
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if self._player.on_platform:
                self._player.jump()
        if keys[pygame.K_RIGHT] and self._player.rect.bottomright[0] <= \
            self._game.SCREEN_WIDTH:
            self._player.set_xdir(1)
        elif keys[pygame.K_LEFT] and self._player.rect.bottomleft[0] >= 0:
            self._player.set_xdir(-1)
        else:
            self._player.set_xdir(0)
