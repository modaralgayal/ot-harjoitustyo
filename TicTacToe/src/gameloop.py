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
        self.width = width
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
                            self.game_board.append((next,self.places_on_board[self.grid*box[2][0]+box[2][1]]))
                            self.game_situation[box[2][0]][box[2][1]] = char
                            for row in self.game_situation:
                                print(row)
                            break
                    elif pos[0] in range(600, 700) and event.pos[1] in range(250, 350):
                        self.game_situation = [
                            [None for i in range(self.grid)] for i in range(self.grid)
                            ]
                        self.game_board = []
                    elif pos[0] in range(self.width-150,self.width-84) and event.pos[1] in range(120, 170):
                        print("GoBack")
                        return "GoBack"

                # Test winning condition in rows ------------------------------------
                
                for row in self.game_situation:
                    if len(set(row)) == 1 and row[0] is not None:
                        print("VOITTO!")
                
                #--------------------------------------------------------------------
                # Test winning condition from TopLeft to BottomRight-----------------
    
                game_set_across = set()
                for c in range(self.grid):
                    game_set_across.add(self.game_situation[c][c])
                
                if len(game_set_across) == 1 and None not in game_set_across:
                    print("VOITTO!")

                #--------------------------------------------------------------------
                # Test winning condition from TopRight to BottomLeft-----------------

                game_set_across_reversed = set()
                for row in range(self.grid):
                    for c in range(1,self.grid+1):
                        if row + 1 == c:
                            game_set_across_reversed.add(self.game_situation[row][-c])

                if len(game_set_across_reversed) == 1 and None not in game_set_across_reversed:
                    print("VOITTO!")
                
                #--------------------------------------------------------------------
                # Test winning conidition vertically---------------------------------

                for col in range(self.grid):
                    game_set_vertical = set()
                    for row in range(self.grid):
                        game_set_vertical.add(self.game_situation[row][col])
                    if len(game_set_vertical) == 1 and None not in game_set_vertical:
                        print("VOITTO!")
                
                #--------------------------------------------------------------------



                
            if event.type == pygame.QUIT:
                return False
            
    def _render(self, game_board):

        self._renderer.render(game_board)

