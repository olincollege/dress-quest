import pygame

class Controller:
    def __init__(self):
        arrow_list = [
            'sela_test_images/top_select.png',
            'sela_test_images/mid_select.png',
            'sela_test_images/bottom_select.png'
        ]

    def change_clothes(self):
        keys = pygame.key.get_pressed()
        