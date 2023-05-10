import pygame


class MenuLoop:

    def __init__(self, grid_sizes, width, height, menu_renderer):

        self.screen = pygame.display.set_mode((width, height))
        self.menu_renderer = menu_renderer
        self.grid_sizes = grid_sizes
        self.grid_size = None

    def start(self):

        while True:
            if self._handle_events() is False:
                return self.grid_size
            self._render()

    def _handle_events(self):

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                for text, coord, value in self.grid_sizes:

                    if pos[0] in range(coord[0], coord[0]+45) and pos[1] in range(coord[1], coord[1]+27):
                        self.grid_size = value
                        return False

            elif event.type == pygame.QUIT:
                return False
        return True

    def _render(self):

        self.menu_renderer.render()
