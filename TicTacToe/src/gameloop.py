import pygame
from random import choice
from itertools import cycle
import itertools
import random


class Gameloop:

    def __init__(self, event_queue, game_board, game_situation, renderer, width, height, places_on_board, click_ranges):

        self.screen = pygame.display.set_mode((width, height))
        self._renderer = renderer
        self.event_queue = event_queue
        self.click_ranges = click_ranges

        X = (pygame.image.load("src/assets/X.png").convert_alpha(), 'X')
        O = (pygame.image.load("src/assets/circle.png").convert_alpha(), 'O')

        self.switch_turn = itertools.cycle([X, O]).__next__

        self.randomize = random.choice([True, False])

        if self.randomize:
            self.switch_turn()

        self.places_on_board = places_on_board
        self.game_board = game_board
        self.game_situation = game_situation

    def start(self):

        while True:
            if self._handle_events() == False:
                return self.game_situation
                break

            self._render(self.game_board)

    def _handle_events(self):

        for event in self.event_queue.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                
                mouse_pos = pygame.mouse.get_pos()
                

                for box in self.click_ranges:
                    print()
                    if mouse_pos[0] in range(box[0][0],box[0][1]) and mouse_pos[1] in range(box[1][0],box[1][1]):
                        if self.game_situation[box[2][0]][box[2][1]] == None:
                            
                            p = self.switch_turn()
                            next, char = p[0], p[1]
                            self.game_board.append((next,self.places_on_board[3*box[2][0]+box[2][1]]))
                            self.game_situation[box[2][0]][box[2][1]] = char

                            for row in self.game_situation:
                                print(row)

                            break
                        
                    elif mouse_pos[0] in range(450, 550) and mouse_pos[1] in range(175, 275):
                        self.game_situation = [
                            [None for i in range(3)] for i in range(3)
                            ]
                        self.game_board = []

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


            if event.type == pygame.QUIT:
                return False
            
        

    def _render(self, game_board):

        self._renderer.render(game_board)
