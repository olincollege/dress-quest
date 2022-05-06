import pygame

class View():
    def __init__(self, game, player, platforms):
        self._game = game
        self._player = player
        self._platforms = platforms
        self._BG_IMG = pygame.image.load("assets/bg.jpg").convert_alpha()
    
    def draw_bg(self):
        self._game.screen.blit(self._BG_IMG, (0, 0))
    
    def draw_player(self):
        self._game.screen.blit(self._player.img, self._player.rect)
        pygame.draw.rect(self._game.screen, (0, 230, 0), self._player.rect, 2)
        pygame.draw.rect(self._game.screen, (250, 30, 0), self._player._jump_hitbox, 2)
    
    def draw_platforms(self):
        self._platforms.group.draw(self._game.screen)

    def update(self):
        pygame.display.update()
