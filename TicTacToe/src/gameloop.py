from random import choice
from itertools import cycle
import pygame


class Gameloop:

    def __init__(self, event_queue, renderer, places_on_board, click_ranges, grid):
        self.screen = pygame.display.set_mode((800, 270+grid*65))
        self._renderer = renderer
        self.event_queue = event_queue
        self.click_ranges = click_ranges
        self.grid = grid
        self.width = 800
        _x = (pygame.image.load("src/assets/X.png").convert_alpha(), 'X')
        _o = (pygame.image.load("src/assets/circle.png").convert_alpha(), 'O')
        self.switch_turn = cycle([_x, _o]).__next__
        self.randomize = choice([True, False])
        if self.randomize:
            self.switch_turn()
        self.places_on_board = places_on_board
        self.game_board = []
        self.game_situation = [
            [None for i in range(grid)] for i in range(grid)]

    def start(self):
        self.winning = False
        while True:
            action = self._handle_events()
            if action == "GoBack":
                return "GoBack"
            if not action:
                break
            if action is True:
                self.winning = True
            self._render(self.game_board,self.winning)
        return self.game_situation, self.check_game()

    def _handle_events(self):
        for event in self.event_queue.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos() == (0, 0):
                    pos = event.pos
                else:
                    pos = pygame.mouse.get_pos()
                for box in self.click_ranges:
                    if (
                        pos[0] in range(box[0][0], box[0][1])
                        and pos[1] in range(box[1][0], box[1][1])
                    ):
                        if not self.game_situation[box[2][0]][box[2][1]]:
                            next_item, char = self.switch_turn()
                            self.game_board.append(
                                (next_item,
                                 self.places_on_board[self.grid * box[2][0] + box[2][1]])
                            )
                            self.game_situation[box[2][0]][box[2][1]] = char
                            break
                if pos[0] in range(600, 700) and pos[1] in range(250, 350):
                    self.game_situation = [
                        [None for i in range(self.grid)] for i in range(self.grid)
                    ]
                    self.game_board = []
                    self.winning = False
                elif (
                    pos[0] in range(self.width - 150, self.width - 84)
                    and pos[1] in range(120, 170)
                    ):
                    return "GoBack"

            if event.type == pygame.QUIT:
                return False
        return self.check_game()

    def check_game(self):

        for row in self.game_situation:
            if len(set(row)) == 1 and row[0] is not None:
                return True
        # --------------------------------------------------------------------
        # Test winning condition from TopLeft to BottomRight-----------------
        game_set_across = set()
        for _c in range(self.grid):
            game_set_across.add(self.game_situation[_c][_c])

        if len(game_set_across) == 1 and None not in game_set_across:
            return True
        # --------------------------------------------------------------------
        # Test winning condition from TopRight to BottomLeft-----------------
        game_set_across_reversed = set()
        for row in range(self.grid):
            for _c in range(1, self.grid):
                if row + 1 == _c:
                    game_set_across_reversed.add(self.game_situation[row][-_c])
        if len(game_set_across_reversed) == 1 and None not in game_set_across_reversed:
            return True
        # --------------------------------------------------------------------
        # Test winning conidition vertically---------------------------------
        for col in range(self.grid):
            game_set_vertical = set()
            for row in range(self.grid):
                game_set_vertical.add(self.game_situation[row][col])
            if len(game_set_vertical) == 1 and None not in game_set_vertical:
                return True
                # --------------------------------------------------------------------
        return "Skip"

    def _render(self,game_board,winning):
        self._renderer.render(game_board,winning)
