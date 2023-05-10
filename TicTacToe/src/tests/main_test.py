import unittest
from gameloop import Gameloop
from renderer import Renderer
import pygame


class StubEvent():

    def __init__(self, event_type, position):

        self.type = event_type
        self.pos = position


class StubQuit():

    def __init__(self, event_type):

        self.type = event_type


class StubEventQueue():

    def __init__(self, events):

        self._events = events

    def get(self):

        return self._events


class StubRenderer():

    def render(self, game_board):

        pass


class TestGameLoop(unittest.TestCase):

    def setUp(self):

        self.click_ranges = [((60, 130), (85, 175), (0, 0)), ((130, 200), (85, 175), (0, 1)), ((200, 270), (85, 175), (0, 2)), ((60, 130), (175, 265), (1, 0)), ((
            130, 200), (175, 265), (1, 1)), ((200, 270), (175, 265), (1, 2)), ((60, 130), (265, 355), (2, 0)), ((130, 200), (265, 355), (2, 1)), ((200, 270), (265, 355), (2, 2))]

    def test_can_save_coordinates_correctly(self):

        game_board = []
        game_situation = [[None for i in range(3)] for i in range(3)]
        renderer = StubRenderer()
        grid = 3
        events = []
        places_on_board = [(60, 85), (130, 85), (200, 85), (60, 175),
                           (130, 175), (200, 175), (60, 265), (130, 265), (200, 265)]

        for place in self.click_ranges:

            click = StubEvent(pygame.MOUSEBUTTONDOWN,
                              (place[0][0]+5, place[1][0]+5))
            events.append(click)

        events.append(StubQuit(pygame.QUIT))

        game_loop = Gameloop(
            StubEventQueue(events),
            game_board,
            game_situation,
            renderer,
            800,
            465,
            places_on_board,
            self.click_ranges,
            grid
        )

        game = game_loop.start()

        for row in game:
            for char in row:
                assert char == 'X' or char == 'O'
        
    def test_renewing_game(self):

        game_board = []
        game_situation = [[None for i in range(3)] for i in range(3)]
        renderer = StubRenderer()
        grid = 3
        events = []
        places_on_board = []

        events = []

        click = StubEvent(pygame.MOUSEBUTTONDOWN,(650, 300))
        events.append(click)
        events.append(StubQuit(pygame.QUIT))

        game_loop = Gameloop(
            StubEventQueue(events),
            game_board,
            game_situation,
            renderer,
            800,
            465,
            places_on_board,
            self.click_ranges,
            grid
        )

        game = game_loop.start()

        for row in game:
            for char in row:
                assert char == None
        
        assert len(game_board) == 0

    def test_winning_is_detected(self):

        game_board = []
        game_situation = [['X' for i in range(3)] for i in range(3)]
        renderer = StubRenderer()
        grid = 3
        events = []
        places_on_board = []

        events = []

        click = StubEvent(pygame.MOUSEBUTTONDOWN,(650, 300))
        events.append(click)
        #events.append(StubQuit(pygame.QUIT))

        game_loop = Gameloop(
            StubEventQueue(events),
            game_board,
            game_situation,
            renderer,
            800,
            465,
            places_on_board,
            self.click_ranges,
            grid
        )

        game = game_loop.start()

        assert game == True

