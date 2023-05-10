import pygame
from gameloop import Gameloop
from renderer import Renderer
from event_pueue import EventQueue

pygame.display.set_caption("Tic Tac Toe")

def main(display, grid, height, width, game_board, game_situation, places_on_board, click_ranges):

    

    event_queue = EventQueue()
    renderer = Renderer(display, height, grid, width)
    game_loop = Gameloop(event_queue, game_board, game_situation, renderer,
                         width, height, places_on_board, click_ranges, grid)
    event_queue = EventQueue()

    pygame.init()
    game_loop.start()