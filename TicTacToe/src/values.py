import pygame


def values(grid):

    width = 800
    height = 270 + grid*65
    display = pygame.display.set_mode((width, height))

    game_board = []
    places_on_board = []
    click_ranges = []

    game_situation = [[None for i in range(grid)] for i in range(grid)]

    X = 60
    Y = 85
    for level in range(grid):
        for column in range(grid):
            click_ranges.append(((column*70+X, column*70+X+70),
                                (level*90+Y, level*90+Y+90), (level, column)))
            places_on_board.append((column*70+X, level*90+Y))
    
    return display, grid, height, width, game_board, game_situation, places_on_board, click_ranges

