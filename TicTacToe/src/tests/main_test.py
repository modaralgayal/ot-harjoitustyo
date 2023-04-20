import unittest
from gameloop import Gameloop
from renderer import Renderer
from main import main
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

class TestGameLoop(unittest.TestCase):

    def setUp(self):

        pass

    def test_game_loop_constructor(self): 

        renderer = Renderer(display, height)

        game_loop = Gameloop(game_board, game_situation, renderer, width, height, UL, UM, UR, ML, M, MR, BL, BM, BR)

        assert game_loop._renderer == renderer
        assert game_loop.screen == pygame.display.set_mode((width, height))
        assert game_loop.game_board == []
        assert game_loop.game_situation == [[None for i in range(3)] for i in range(3)]

    def test_game_coordinates(self):

        renderer = Renderer(display, height)

        game_loop = Gameloop(game_board, game_situation, renderer, width, height, UL, UM, UR, ML, M, MR, BL, BM, BR)

        assert game_loop.UL == UL
        assert game_loop.UM == UM
        assert game_loop.UR == UR
        assert game_loop.ML == ML
        assert game_loop.M == M
        assert game_loop.MR == MR
        assert game_loop.BL == BL
        assert game_loop.BM == BM
        assert game_loop.BR == BR
    