import pygame


class Renderer:

    def __init__(self, screen, height):

        self.height = height
        self._screen = screen
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.retry = pygame.image.load("src/assets/retry.png").convert_alpha()

    def render(self, game_board):

        '''
        In this updated instance, render() function gets game_board as it's variable as well as the length of the grid, for example if the game is 3x3, it gets 3 as it's variable. That way
        we can use it to loop and draw the lines we need for the TicTacToe game, which allows us to expand the game at will. 
        '''

        self._screen.fill(self.white)

        # Kanvas for game

        lines = []
        line_width = 5

        #Horizontal

        x_axis = 50; y_axis = 65

        for i in range(1,3):
            lines.append(((x_axis,y_axis+i*90),(x_axis+3*70, y_axis+i*90)))
        
        #Diagonal --------------------------------------------------------------#

        for i in range(1,3):
            lines.append(((x_axis+i*70,y_axis),(x_axis+i*70, self.height - 65)))


        for start, finish in lines:
            pygame.draw.line(self._screen, self.black,(start[0], start[1]), (finish[0], finish[1]), line_width)

        #----------------------------------------------------------------------#
        for char, pos in game_board:
            self._screen.blit(char, pos)

        self._screen.blit(self.retry, (450, 175))

        # print(self.game_board)

        pygame.display.update()
