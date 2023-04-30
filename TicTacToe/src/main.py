import pygame
from gameloop import Gameloop
from renderer import Renderer
from event_pueue import EventQueue


width = 700
height = 400
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")

game_board = []
game_situation = [[None for i in range(3)] for i in range(3)]

places_on_board = []

x = 60; y = 85
for level in range(3):
    for column in range(3):
        places_on_board.append((column*70+x,level*90+y))

#print(places_on_board)


click_ranges = [((55,120),(70,150),(0,0)), ((130,205),(70,150), (0,1)),((160,285),(70,150),(0,2)),
                ((55,120),(130,240),(1,0)),((130,205),(130,240),(1,1)),((160,285),(130,240),(1,2)),
                ((55,120),(250,330),(2,0)),((130,205),(250,330),(2,1)),((160,285),(250,330),(2,2))
                ]


def main():

    event_queue = EventQueue()
    renderer = Renderer(display, height)
    game_loop = Gameloop(event_queue, game_board, game_situation, renderer,
                         width, height, places_on_board, click_ranges)
    event_queue = EventQueue()

    pygame.init()
    game_loop.start()


if __name__ == "__main__":
    main()
