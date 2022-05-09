'''
Runs the main game loop.
'''

import pygame
from controllers import DG_Controller, FP_Controller
from game import Game
from platforms import Platforms
from players import DG_Player, FP_Player
from views import DG_View, FP_View

def main():
    '''
    Runs the dress up and then platformer game.
    '''
    # define game class
    game = Game()

    # define dressup game classes
    dg_player = DG_Player()
    dg_controller = DG_Controller(game, dg_player)
    dg_view = DG_View(game, dg_player)

    # define platformer classes
    fp_player = FP_Player(game)
    fp_controller = FP_Controller(game, fp_player)
    platforms = Platforms(game)
    fp_view = FP_View(game, fp_player, platforms)

    while game.running:
        game.update()
        if game.game_state == "dressup":
            dg_controller.change_clothes()

            dg_view.draw_bg()
            dg_view.draw_instructions()
            dg_view.draw_clothes()
            dg_view.draw_arrows()

            dg_view.update()
        else:
            fp_view.draw_bg()
            fp_view.draw_player()
            fp_view.draw_platforms()

            fp_controller.move_player()
            fp_player.update_pos(platforms.group)

            platforms.generate()
            platforms.scroll()

            fp_view.update()

    pygame.quit()

main()
