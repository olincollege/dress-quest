from game import Game
from view import View
from player import Player
from controller import Controller

game = Game()
player = Player(game)
view = View(game, player)
controller = Controller(game, player)


while game.running:
    view.draw_bg()
    view.draw_player()

    controller.move_x()

    game.update()
    view.update()
