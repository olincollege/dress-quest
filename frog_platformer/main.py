from game import Game
from view import View
from player import Player
from controller import Controller
from platforms import Platforms

def main():

    game = Game()
    player = Player(game)
    platforms = Platforms(game)
    
    view = View(game, player, platforms)

    controller = Controller(game, player)
    
    while game.running:
        view.draw_bg()
        view.draw_player()
        view.draw_platforms()

        controller.move_player()
        player.update_pos(platforms.group)

        platforms.generate()
        platforms.scroll()

        game.update()
        view.update()



main()