import pygame

class DG_Controller:
    """
    Controller for changing the frog sprite's clothing.

    Attributes:
        game: An instance of the Game class, representing the current game
            being played
        player: An instance of the Player class, representing the player
            being controlled by the controller
    """

    def __init__(self, game, player):
        self.game = game
        self.player = player

    def change_clothes(self):
        """
        Changes the clothing on the player sprite using input from the arrows.

        The left and right arrows are used to scroll between clothing items,
        and the up and down arrows are used to select which item of clothing
        is being changed (hat, top, or bottom)
        """
        for event in self.game.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.game.item = (self.game.item + 1) % 3
                elif event.key == pygame.K_UP:
                    self.game.item = (self.game.item - 1) % 3

                if event.key == pygame.K_RIGHT:
                    self.player.change_outfit(self.game.item, 1)
                elif event.key == pygame.K_LEFT:
                    self.player.change_outfit(self.game.item, -1)


class FP_Controller():
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
