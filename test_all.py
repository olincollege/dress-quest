"""
Unit tests.
"""
import pytest
import pygame

from players import DgPlayer
from game import Game

pygame.init()

#dress up game player test code
player_coords_test_cases = (
  #test that the clothing appears in the correct spot in the correct order.
  ( ((0,1), (0,1)), [(190, 457), (0, 0), (0, 0)], '[<Surface(120x50x32 SW)>, \
                        <Surface(500x668x32 SW)>, <Surface(500x668x32 SW)>]' ),
  ( ((1,1), (2,1)), [(0, 0), (176, 520), (159, 522)], '[<Surface(500x668x32 SW)>, \
                            <Surface(147x55x32 SW)>, <Surface(197x87x32 SW)>]' ),
)

#controller key test code
right_arrow = pygame.event.Event(pygame.KEYDOWN, {'unicode': '',
    'key': 1073741903, 'mod': 0, 'scancode': 79, 'window': None})

left_arrow = pygame.event.Event(pygame.KEYDOWN, {'unicode': '',
    'key': 1073741904, 'mod': 0, 'scancode': 80, 'window': None})

up_arrow = pygame.event.Event(pygame.KEYDOWN, {'unicode': '',
    'key': 1073741906, 'mod': 0, 'scancode': 82, 'window': None})

down_arrow = pygame.event.Event(pygame.KEYDOWN, {'unicode': '',
    'key': 1073741905, 'mod': 0, 'scancode': 82, 'window': None})

enter_key = pygame.event.Event(pygame.KEYDOWN, {'unicode': '',
    'key': 13, 'mod': 0, 'scancode': 83, 'window': None})

space_bar = pygame.event.Event(pygame.KEYDOWN, {'unicode': '',
    'key': 32, 'mod': 0, 'scancode': 83, 'window': None})


get_input_cases = [
    # Test that right arrow moves right.
    (right_arrow, 1073741903),
    # Test that left arrow moves left.
    (left_arrow, 1073741904),
    # Test that up arrow moves up.
    (up_arrow, 1073741906),
    # Test that up arrow moves down.
    (down_arrow, 1073741905),
    # Test that enter key enteres.
    (enter_key, 13),
    # Test that space bar spaces.
    (space_bar, 32),
]

get_event_cases = [
    # Test that space bar spaces.
    (space_bar),
]

get_event_cases2 = [
    # Test that space bar spaces.
    (enter_key),
]


@pytest.mark.parametrize("test_case", player_coords_test_cases)
def test_player_coords(test_case):
    """
    Test that the clothing appears in the correct spot in the correct order.
    """
    player = DgPlayer()
    for item, direction in test_case[0]:
        player.change_outfit(item, direction)
    assert player.coords == test_case[1]

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


@pytest.mark.parametrize("event",
    get_event_cases)
def test_update(event):
    """
    Test update event loop is working.
    Args:
        event: The event in event loop.
    """
    pygame.event.clear()
    # Add event to the queue
    pygame.event.post(event)
    game = Game()
    game.update()
    # Check that the event was added.
    assert game.show_instructions is False

@pytest.mark.parametrize("event",
    get_event_cases2)
def test_update2(event):
    """
    Test update event loop is working.
    Args:
        event: The event in event loop.
    """
    pygame.event.clear()
    # Add event to the queue
    pygame.event.post(event)
    game = Game()
    game.update()
    # Check that the event was added.
    assert game.running is True
