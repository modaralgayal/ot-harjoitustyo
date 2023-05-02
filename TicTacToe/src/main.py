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
CLICK_RANGES = []

X = 60
Y = 85
for level in range(3):
    for column in range(3):
        CLICK_RANGES.append(((column*70+X, column*70+X+70),(level*90+Y,level*90+Y+90),(level,column)))
        PLACES_ON_BOARD.append((column*70+X,level*90+Y))

print()
print(PLACES_ON_BOARD)

def main():

    event_queue = EventQueue()
    renderer = Renderer(DISPLAY, HEIGHT)
    game_loop = Gameloop(event_queue, GAME_BOARD, GAME_SITUATION, renderer,
                         WIDTH, HEIGHT, PLACES_ON_BOARD, CLICK_RANGES)
    event_queue = EventQueue()

    pygame.init()
    game_loop.start()


if __name__ == "__main__":
    main()
