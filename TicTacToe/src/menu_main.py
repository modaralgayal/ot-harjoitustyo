import pygame
from menu_loop import MenuLoop
from menu_renderer import MenuRenderer


pygame.init()

HEIGHT = 400
WIDTH = 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Main menu')
GRID_SIZES = [("3x3", (100, 200), 3), ("4x4", (210, 200), 4), ("5x5",
            (320, 200), 5), ("6x6", (430, 200), 6), ("7x7", (540, 200), 7)]
GRID_SIZES_RENDERER = [("3x3", (100, 200)), ("4x4", (210, 200)), ("5x5",
            (320, 200)), ("6x6", (430, 200)), ("7x7", (540, 200))]

def menu_main():

    menu_renderer = MenuRenderer(SCREEN, HEIGHT, WIDTH, GRID_SIZES_RENDERER)
    menu_loop = MenuLoop(GRID_SIZES_RENDERER, WIDTH, HEIGHT, menu_renderer)

    pygame.init()
    grid = menu_loop.start()
    return grid


if __name__ == "__main__":
    menu_main()
