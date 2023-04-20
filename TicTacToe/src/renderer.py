import pygame


class Renderer:

    def __init__(self, screen, height):

        self.height = height
        self._screen = screen
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.retry = pygame.image.load("assets/retry.png").convert_alpha()

    def render(self, game_board):

        self._screen.fill(self.WHITE)

        # Kanvas for game of 3x3

        #Diagonal --------------------------------------------------------------#

        startX = 125
        startY = 65
        endX = 125
        endY = self.height-65
        width = 5
        pygame.draw.line(self._screen, self.BLACK,
                         (startX, startY), (endX, endY), width)

        startX = 210
        startY = 65
        endX = 210
        endY = self.height-65
        width = 5
        pygame.draw.line(self._screen, self.BLACK,
                         (startX, startY), (endX, endY), width)

        #-----------------------------------------------------------------------#

        # Horizontal------------------------------------------------------------#

        startX = 50
        startY = 155
        endX = 290
        endY = 155
        width = 5
        pygame.draw.line(self._screen, self.BLACK,
                         (startX, startY), (endX, endY), width)

        startX = 50
        startY = 245
        endX = 290
        endY = 245
        width = 5
        pygame.draw.line(self._screen, self.BLACK,
                         (startX, startY), (endX, endY), width)

        #----------------------------------------------------------------------#
        for char, pos in game_board:
            self._screen.blit(char, pos)

        self._screen.blit(self.retry, (450, 175))

        # print(self.game_board)

        pygame.display.update()
