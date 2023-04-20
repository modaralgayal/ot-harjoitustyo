import pygame


class Renderer:

    def __init__(self, screen, height):

        self.height = height
        self._screen = screen
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.retry = pygame.image.load("src/assets/retry.png").convert_alpha()

    def render(self, game_board):

        self._screen.fill(self.white)

        # Kanvas for game of 3x3

        #Diagonal --------------------------------------------------------------#

        start_x = 125
        start_y = 65
        end_x = 125
        end_y = self.height-65
        width = 5
        pygame.draw.line(self._screen, self.black,(start_x, start_y), (end_x, end_y), width)

        start_x = 210
        start_y = 65
        end_x = 210
        end_y = self.height-65
        width = 5
        pygame.draw.line(self._screen, self.black,(start_x, start_y), (end_x, end_y), width)

        #-----------------------------------------------------------------------#

        # Horizontal------------------------------------------------------------#

        start_x = 50
        start_y = 155
        end_x = 290
        end_y = 155
        width = 5
        pygame.draw.line(self._screen, self.black,
                         (start_x, start_y), (end_x, end_y), width)

        start_x = 50
        start_y = 245
        end_x = 290
        end_y = 245
        width = 5
        pygame.draw.line(self._screen, self.black,
                         (start_x, start_y), (end_x, end_y), width)

        #----------------------------------------------------------------------#
        for char, pos in game_board:
            self._screen.blit(char, pos)

        self._screen.blit(self.retry, (450, 175))

        # print(self.game_board)

        pygame.display.update()
