import pygame
from gameloop import Gameloop
from renderer import Renderer
from event_pueue import EventQueue

pygame.display.set_caption("Tic Tac Toe")


def main(grid, places_on_board, click_ranges):

    event_queue = EventQueue()
    renderer = Renderer(grid)
    game_loop = Gameloop(event_queue, renderer,
                         places_on_board, click_ranges, grid)
    event_queue = EventQueue()

    pygame.init()
    return game_loop.start()
