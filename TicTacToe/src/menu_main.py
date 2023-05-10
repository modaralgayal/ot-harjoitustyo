from menu_loop import MenuLoop
from menu_renderer import MenuRenderer
import pygame

pygame.init()

HEIGHT = 400
WIDTH = 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Main menu')
GRID_SIZES = [("3x3", (100, 200), 3), ("4x4", (210, 200), 4), ("5x5",
                                                               (320, 200), 5), ("6x6", (430, 200), 6), ("7x7", (540, 200), 7)]



def menu_main():

    menu_renderer = MenuRenderer(SCREEN, HEIGHT, WIDTH, GRID_SIZES)
    menu_loop = MenuLoop(GRID_SIZES, WIDTH, HEIGHT, menu_renderer)

    pygame.init()
    GRID = menu_loop.start()
    return GRID


if __name__ == "__main__":
    menu_main()
