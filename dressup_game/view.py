import pygame

class View:
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
      self._game.screen.blit(self.BG_IMG, (0, 0))
      # self._game.screen.blit(self.FG_IMG, (0, 0))
  
    def draw_clothes(self):
        for i in range(3):
            self._game.screen.blit(self._player.images[i], \
                self._player.coords[i])
    
    def draw_instructions(self):
        if not self._game.show_instructions:
            self.instructions_img = \
                pygame.image.load('sela_test_images/enter_instruct.png')
        self._game.screen.blit(self.instructions_img, (0, 0))
    
    def draw_arrows(self):
        if not self._game.show_instructions:
            self._game.screen.blit(pygame.image.load(\
                self.ARROWS[self._game.item]), (0, 0))
    
    def update(self):
        pygame.display.update()

