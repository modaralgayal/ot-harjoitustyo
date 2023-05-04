from random import choice
from itertools import cycle
import pygame



class Gameloop:

    def __init__(self, event_queue, game_board, game_situation, 
                 renderer, width, height, places_on_board, click_ranges, grid):

        self.screen = pygame.display.set_mode((width, height))
        self._renderer = renderer
        self.event_queue = event_queue
        self.click_ranges = click_ranges
        self.grid = grid
        print(self.grid)
        _x = (pygame.image.load("src/assets/X.png").convert_alpha(), 'X')
        _o = (pygame.image.load("src/assets/circle.png").convert_alpha(), 'O')
        self.switch_turn = cycle([_x,_o]).__next__
        self.randomize = choice([True, False])
        if self.randomize:
            self.switch_turn()
        self.places_on_board = places_on_board
        self.game_board = game_board
        self.game_situation = game_situation

    def start(self):
        while True:
            if self._handle_events() is False:
                break
            self._render(self.game_board)
        return self.game_situation

    def _handle_events(self):

        for event in self.event_queue.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos() == (0,0):
                    pos = event.pos
                else:
                    pos = pygame.mouse.get_pos()
                for box in self.click_ranges:
                    print()
                    if pos[0] in range(box[0][0],box[0][1]) and pos[1] in range(box[1][0],box[1][1]):
                        if not self.game_situation[box[2][0]][box[2][1]]:
                            _p = self.switch_turn()
                            next, char = _p[0], _p[1]
                            self.game_board.append((next,self.places_on_board[3*box[2][0]+box[2][1]]))
                            self.game_situation[box[2][0]][box[2][1]] = char
                            for row in self.game_situation:
                                print(row)
                            break
                    elif pos[0] in range(550, 650) and event.pos[1] in range(175, 275):
                        self.game_situation = [
                            [None for i in range(3)] for i in range(3)
                            ]
                        self.game_board = []
                

                '''  
                for row in self.game_situation:
                    if row[0] == row[1] == row[2] != None:
                        print("VOITTO!")
                for i in range(3):
                    if self.game_situation[0][i] == self.game_situation[1][i] == self.game_situation[2][i] != None:
                        print("HUHHUH")
                    if self.game_situation[0][0] == self.game_situation[1][1] == self.game_situation[2][2] != None:
                        print("HUHHUH")
                    if self.game_situation[0][2] == self.game_situation[1][1] == self.game_situation[2][0] != None:
                        print("HUHHUH")
                '''
                
            if event.type == pygame.QUIT:
                return False
            
    def _render(self, game_board):

        self._renderer.render(game_board)
