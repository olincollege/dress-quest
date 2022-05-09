import pygame
from controllers import DgController, FpController
from game import Game
from platforms import Platforms
from players import DgPlayer, FpPlayer
from views import DgView, FpView


def main():
    '''
    Runs the dress up and then platformer game.
    '''
    # define game class
    game = Game()

    # define dressup game classes
    dg_player = DgPlayer()
    dg_controller = DgController(game, dg_player)
    dg_view = DgView(game, dg_player)

    # define platformer classes
    fp_player = FpPlayer(game)
    fp_controller = FpController(game, fp_player)
    platforms = Platforms(game)
    fp_view = FpView(game, fp_player, platforms)

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
