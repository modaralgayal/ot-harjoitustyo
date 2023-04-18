import unittest
from gameloop import Gameloop
from renderer import Renderer
import pygame


class TestGameLoop(unittest.TestCase):

    def setUp(self):

        pass

    def test_game_loop_constructor(self):
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

        renderer = Renderer(display, height)

        game_loop = Gameloop(game_board, game_situation, renderer,
                             width, height, UL, UM, UR, ML, M, MR, BL, BM, BR)

        assert game_loop._renderer == renderer
        assert game_loop.screen == pygame.display.set_mode((width, height))
