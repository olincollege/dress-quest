import pygame

class Controller:
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
                    self.game.item = self.game.item + 1 % 3
                elif event.key == pygame.K_UP:
                    self.game.item = (self.game.item - 1) % 3
        
                if event.key == pygame.K_RIGHT:
                    self.player.change_outfit(self.game.item, 1)
                elif event.key == pygame.K_LEFT:
                    self.player.change_outfit(self.game.item, -1)

