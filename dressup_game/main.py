import pygame
from player import Player
from controller import Controller
from view import View
from game import Game

game = Game()
player = Player()

controller = Controller(game, player)

view = View(game, player)

while game.running:
  game.update()

  controller.change_clothes()
  
  view.draw_bg()
  view.draw_instructions()
  view.draw_clothes()
  
  view.update()

pygame.quit()
