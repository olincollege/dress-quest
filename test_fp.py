"""
Unit tests.
"""
import pytest
import pygame

from fp_player import Player
from fp_controller import Controller
from fp_game import Game

pygame.init()



#controller key test code
right_arrow = pygame.event.Event(pygame.KEYDOWN, {'unicode': '',
    'key': 1073741903, 'mod': 0, 'scancode': 79, 'window': None})

left_arrow = pygame.event.Event(pygame.KEYDOWN, {'unicode': '',
    'key': 1073741904, 'mod': 0, 'scancode': 80, 'window': None})

up_arrow = pygame.event.Event(pygame.KEYDOWN, {'unicode': '',
    'key': 1073741906, 'mod': 0, 'scancode': 82, 'window': None})

down_arrow = pygame.event.Event(pygame.KEYDOWN, {'unicode': '',
    'key': 1073741905, 'mod': 0, 'scancode': 82, 'window': None})



get_input_cases = [
    # Test that right arrow moves right.
    (right_arrow, 1073741903),
    # Test that left arrow moves left.
    (left_arrow, 1073741904),
    # Test that up arrow moves up.
    (up_arrow, 1073741906),
    # Test that up arrow moves down.
    (down_arrow, 1073741905),
]



@pytest.mark.parametrize("event, key",
    get_input_cases)
def test_input(event, key):
    """
    Test that user input is inputted.
    Args:
        event: The event is caused by pressing the key.
        key: The key pressed.
    """
    pygame.event.clear()
    # Add event to the queue
    pygame.event.post(event)
    # Check that the event was added.
    for each_event in pygame.event.get(pygame.KEYDOWN):
        assert each_event.key == key

@pytest.mark.parametrize("event, key",
    get_input_cases)
def test_input(event, key):
    """
    Test that user input is inputted.
    Args:
        event: The event is caused by pressing the key.
        key: The key pressed.
    """
    pygame.event.clear()
    # Add event to the queue
    pygame.event.post(event)
    # Check that the event was added.
    for each_event in pygame.event.get(pygame.KEYDOWN):
        assert each_event.key == key