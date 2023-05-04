import pygame


class Renderer:

    def __init__(self, screen, height, grid):

        self.height = height
        self._screen = screen
        self.grid = grid
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.retry = pygame.image.load("src/assets/retry.png").convert_alpha()

    def render(self, game_board):

        self._screen.fill(self.white)

        # Kanvas for game

        lines = []
        line_width = 5

        #Horizontal

        x_axis = 50
        y_axis = 65

        for i in range(1,self.grid):
            lines.append(((x_axis,y_axis+i*90),(x_axis+self.grid*70, y_axis+i*90)))
        
        #Diagonal --------------------------------------------------------------#

        for i in range(1,self.grid):
            lines.append(((x_axis+i*70,y_axis),(x_axis+i*70, self.height - 65)))


        for start, finish in lines:
            pygame.draw.line(self._screen, self.black,(start[0], start[1]), (finish[0], finish[1]), line_width)

        #----------------------------------------------------------------------#
        for char, pos in game_board:
            self._screen.blit(char, pos)

        self._screen.blit(self.retry, (450, 175))

        # print(self.game_board)

        pygame.display.update()
