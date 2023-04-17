import pygame
from gameloop import Gameloop
from clock import Clock
from renderer import Renderer
from game_board import GameBoard



width = 700
height = 400
display = pygame.display.set_mode((width,height))

game_board = []
game_situation = [[None for i in range(3)] for i in range(3)]


UL = (60,85);  UM = (145,85);  UR = (230,85)   # UpperLeft, UpperMiddle, UpperRight 
ML = (60,175);  M = (145,175); MR = (230,175)  # MiddleLeft, Middle, MiddleRight 
BL = (60,265); BM = (145,265); BR = (230,265) # BottomLeft, BottomMiddle, BottomRight


def main():

    pygame.display.set_caption("Tic Tac Toe")

    renderer = Renderer(display, game_board, height)
    game_loop = Gameloop(game_board, game_situation, renderer, width, height, UL, UM, UR, ML, M, MR, BL, BM, BR)

    pygame.init()
    game_loop.start()


if __name__ == "__main__":
    main()