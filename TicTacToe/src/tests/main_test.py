import unittest
from gameloop import Gameloop
from renderer import Renderer
from event_pueue import EventQueue
import pygame


width = 700
height = 400
display = pygame.display.set_mode((width, height))

game_board = []
game_situation = [[None for i in range(3)] for i in range(3)]

UL = (60, 85)
UM = (145, 85)
UR = (230, 85)   # UpperLeft, UpperMiddle, UpperRight
ML = (60, 175)
M = (145, 175)
MR = (230, 175)  # MiddleLeft, Middle, MiddleRight
BL = (60, 265)
BM = (145, 265)
BR = (230, 265)  # BottomLeft, BottomMiddle, BottomRight

places_on_board = [UL, UM, UR, ML, M, MR, BL, BM, BR]


click_ranges = [((55, 120), (70, 150), (0, 0)), ((130, 205), (70, 150), (0, 1)), ((160, 285), (70, 150), (0, 2)),
                ((55, 120), (130, 240), (1, 0)), ((130, 205),
                                                  (130, 240), (1, 1)), ((160, 285), (130, 240), (1, 2)),
                ((55, 120), (250, 330), (2, 0)), ((130, 205),
                                                  (250, 330), (2, 1)), ((160, 285), (250, 330), (2, 2))
                ]


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

        self.click_ranges = [((55, 120), (70, 150), (0, 0)), ((130, 205), (70, 150), (0, 1)), ((160, 285), (70, 150), (0, 2)),
                             ((55, 120), (130, 240), (1, 0)), ((130, 205),
                                                               (130, 240), (1, 1)), ((160, 285), (130, 240), (1, 2)),
                             ((55, 120), (250, 330), (2, 0)), ((130, 205),
                                                               (250, 330), (2, 1)), ((160, 285), (250, 330), (2, 2))
                             ]

    def test_can_save_coordinates_correctly(self):

        game_board = []
        game_situation = [[None for i in range(3)] for i in range(3)]
        renderer = StubRenderer()

        events = []

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
            width,
            height,
            places_on_board,
            self.click_ranges,
            grid
        )

        game = game_loop.start()

        for row in game:
            for char in row:
                assert char == 'X' or char == 'O'
