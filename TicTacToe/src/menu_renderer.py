import pygame


class MenuRenderer:

    def __init__(self, screen, height, width, grid_sizes):

        self.height = height
        self._screen = screen
        self.width = width
        self.grid_sizes = grid_sizes
        self.text_font = pygame.font.SysFont(None, 40)
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.red = (255,0,0)

    def draw_text(self, text, font, text_col, x, y):

        img = font.render(text, True, text_col)
        self._screen.blit(img, (x,y))
    
    def render(self):

        self._screen.fill(self.white)

        self.draw_text("Choose Grid", self.text_font, (0,0,0), 267.5, 100)

        for text, coord, value in self.grid_sizes:

            self.draw_text(text, self.text_font, self.red, coord[0],coord[1])
        

        pygame.display.update()