import pygame
from gameloop import Gameloop
from renderer import Renderer
from event_pueue import EventQueue
from menu_main import menu_main


WIDTH = 700
HEIGHT = 205
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

GAME_BOARD = []
GAME_SITUATION = [[None for i in range(3)] for i in range(3)]
PLACES_ON_BOARD = []
CLICK_RANGES = []

X = 60
Y = 85

def create_levels(grid):
    for level in range(grid):
        for column in range(grid):
            CLICK_RANGES.append(((column*70+X, column*70+X+70),(level*90+Y,level*90+Y+90),(level,column)))
            PLACES_ON_BOARD.append((column*70+X,level*90+Y))

print()
print(PLACES_ON_BOARD)

def main(grid):

    event_queue = EventQueue()
    renderer = Renderer(DISPLAY, HEIGHT + grid*65, grid)
    game_loop = Gameloop(event_queue, GAME_BOARD, GAME_SITUATION, renderer,
                         WIDTH, HEIGHT + grid*65, PLACES_ON_BOARD, CLICK_RANGES, grid)
    event_queue = EventQueue()

    pygame.init()
    game_loop.start()


if __name__ == "__main__":
    grid = menu_main()
    create_levels(grid)
    main(grid)
