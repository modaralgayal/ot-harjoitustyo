import pygame
from gameloop import Gameloop
from renderer import Renderer
from event_pueue import EventQueue


WIDTH = 700
HEIGHT = 400
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

GAME_BOARD = []
GAME_SITUATION = [[None for i in range(3)] for i in range(3)]

PLACES_ON_BOARD = []

X = 60
Y = 85
for level in range(3):
    for column in range(3):
        PLACES_ON_BOARD.append((column*70+X,level*90+Y))


click_ranges = [((55,120),(70,150),(0,0)), ((130,205),(70,150), (0,1)),((160,285),(70,150),(0,2)),
                ((55,120),(130,240),(1,0)),((130,205),(130,240),(1,1)),((160,285),(130,240),(1,2)),
                ((55,120),(250,330),(2,0)),((130,205),(250,330),(2,1)),((160,285),(250,330),(2,2))
                ]


def main():

    event_queue = EventQueue()
    renderer = Renderer(DISPLAY, HEIGHT)
    game_loop = Gameloop(event_queue, GAME_BOARD, GAME_SITUATION, renderer,
                         WIDTH, HEIGHT, PLACES_ON_BOARD, click_ranges)
    event_queue = EventQueue()

    pygame.init()
    game_loop.start()


if __name__ == "__main__":
    main()
