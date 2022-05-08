import pygame

class Controller:
    def __init__(self, game, player):
        arrow_list = [
            'sela_test_images/top_select.png',
            'sela_test_images/mid_select.png',
            'sela_test_images/bottom_select.png'
        ]

        self.game = game
        self.player = player

    def change_clothes(self):
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

