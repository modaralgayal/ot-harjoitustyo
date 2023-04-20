import pygame
from gameloop import Gameloop
from renderer import Renderer


width = 700
height = 400
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")

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


def main():

    renderer = Renderer(display, height)
    game_loop = Gameloop(game_board, game_situation, renderer,
                         width, height, UL, UM, UR, ML, M, MR, BL, BM, BR)

    pygame.__init__()
    game_loop.start()


if __name__ == "__main__":
    main()
