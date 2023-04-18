import pygame
from random import choice
from itertools import cycle
import itertools
import random


class Gameloop:

    def __init__(self, game_board, game_situation, renderer, width , height, UL, UM, UR, ML, M, MR, BL, BM, BR):

        self.screen = pygame.display.set_mode((width,height))

        self._renderer = renderer

        X = (pygame.image.load("src/assets/X.png").convert_alpha(), 'X')
        O = (pygame.image.load("src/assets/circle.png").convert_alpha(), 'O')

        self.switch_turn = itertools.cycle([X,O]).__next__

        self.randomize = random.choice([True,False])

        if self.randomize:
            self.switch_turn()

        self.UL = UL;  self.UM = UM;  self.UR = UR   # UpperLeft, UpperMiddle, UpperRight 
        self.ML = ML;  self.M =   M; self.MR =  MR   # MiddleLeft, Middle, MiddleRight 
        self.BL = BL; self.BM =  BM; self.BR =  BR   # BottomLeft, BottomMiddle, BottomRight

        self.game_board = game_board
        self.game_situation = game_situation

    def start(self):

        while True:
            if self._handle_events() == False:
                break

            self._render(self.game_board)

    
    def _handle_events(self):
        for event in pygame.event.get():
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()


                if mouse_pos[0] in range(55,120) and mouse_pos[1] in range(70,150):
                    if self.game_situation[0][0] == None:
                        p = self.switch_turn()
                        next, char = p[0],p[1]
                        self.game_board.append((next,self.UL))
                        self.game_situation[0][0] = char

                elif mouse_pos[0] in range(130,205) and mouse_pos[1] in range(70,150):    
                    if self.game_situation[0][1] == None:
                        p = self.switch_turn()
                        next, char = p[0],p[1]
                        self.game_board.append((next,self.UM))
                        self.game_situation[0][1] = char
            
                elif mouse_pos[0] in range(160,285) and mouse_pos[1] in range(70,150):
                    if self.game_situation[0][2] == None:
                        p = self.switch_turn()
                        next, char = p[0],p[1]
                        self.game_board.append((next,self.UR))
                        self.game_situation[0][2] = char
                
                elif mouse_pos[0] in range(55,120) and mouse_pos[1] in range(130,240):
                    if self.game_situation[1][0] == None:
                        p = self.switch_turn()
                        next, char = p[0],p[1]
                        self.game_board.append((next,self.ML))
                        self.game_situation[1][0] = char
            
                elif mouse_pos[0] in range(130,205) and mouse_pos[1] in range(130,240):
                    if self.game_situation[1][1] == None:
                        p = self.switch_turn()
                        next, char = p[0],p[1]
                        self.game_board.append((next,self.M))
                        self.game_situation[1][1] = char
            
                elif mouse_pos[0] in range(160,285) and mouse_pos[1] in range(130,240):
                    if self.game_situation[1][2] == None:
                        p = self.switch_turn()
                        next, char = p[0],p[1]
                        self.game_board.append((next,self.MR))
                        self.game_situation[1][2] = char
                
                elif mouse_pos[0] in range(55,120) and mouse_pos[1] in range(250,330):
                    if self.game_situation[2][0] == None:
                        p = self.switch_turn()
                        next, char = p[0],p[1]
                        self.game_board.append((next,self.BL))
                        self.game_situation[2][0] = char
                        
                elif mouse_pos[0] in range(130,205) and mouse_pos[1] in range(250,330):
                    if self.game_situation[2][1] == None:
                        p = self.switch_turn()
                        next, char = p[0],p[1]
                        self.game_board.append((next,self.BM))
                        self.game_situation[2][1] = char
            
                elif mouse_pos[0] in range(160,285) and mouse_pos[1] in range(250,330):
                    if self.game_situation[2][2] == None:
                        p = self.switch_turn()
                        next, char = p[0],p[1]
                        self.game_board.append((next,self.BR))
                        self.game_situation[2][2] = char
                
                elif mouse_pos[0] in range(450,550) and mouse_pos[1] in range(175,275):
                    self.game_situation = [[None for i in range(3)] for i in range(3)]
                    self.game_board = []
                    
                else:
                    print('Outside')
                    pass

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