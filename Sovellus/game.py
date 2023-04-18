import pygame 
import os
from random import choice
from itertools import cycle
import itertools
import random

width = 700
height = 400

pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Ristinolla")
clock = pygame.time.Clock()


WHITE = (255,255,255)
BLACK = (0,0,0)

X = (pygame.image.load("all/assets/X.png").convert_alpha(), 'X')
O = (pygame.image.load("all/assets/circle.png").convert_alpha(), 'O')
Retry = pygame.image.load("all/assets/retry.png").convert_alpha()

UL = (60,85);  UM = (145,85);  UR = (230,85)   # UpperLeft, UpperMiddle, UpperRight 
ML = (60,175);  M = (145,175); MR = (230,175)  # MiddleLeft, Middle, MiddleRight 
BL = (60,265); BM = (145,265); BR = (230,265) # BottomLeft, BottomMiddle, BottomRight


game_board = []
game_situation = [[None for i in range(3)] for i in range(3)]

print(game_situation)

switch_turn = itertools.cycle([X,O]).__next__

randomize = random.choice([True,False])

if randomize:
    switch_turn()

while True: 

    pygame.time.delay(100)

    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit() 
        if event.type == pygame.MOUSEBUTTONDOWN:
            left_mouse_key = pygame.mouse.get_pressed()[0]
            mouse_pos = pygame.mouse.get_pos()


            if mouse_pos[0] in range(55,120) and mouse_pos[1] in range(70,150):
                if game_situation[0][0] == None:
                    p = switch_turn()
                    next, char = p[0],p[1]
                    game_board.append((next,UL))
                    game_situation[0][0] = char

            elif mouse_pos[0] in range(130,205) and mouse_pos[1] in range(70,150):    
                if game_situation[0][1] == None:
                    p = switch_turn()
                    next, char = p[0],p[1]
                    game_board.append((next,UM))
                    game_situation[0][1] = char
        
            elif mouse_pos[0] in range(160,285) and mouse_pos[1] in range(70,150):
                if game_situation[0][2] == None:
                    p = switch_turn()
                    next, char = p[0],p[1]
                    game_board.append((next,UR))
                    game_situation[0][2] = char
            
            elif mouse_pos[0] in range(55,120) and mouse_pos[1] in range(130,240):
                if game_situation[1][0] == None:
                    p = switch_turn()
                    next, char = p[0],p[1]
                    game_board.append((next,ML))
                    game_situation[1][0] = char
        
            elif mouse_pos[0] in range(130,205) and mouse_pos[1] in range(130,240):
                if game_situation[1][1] == None:
                    p = switch_turn()
                    next, char = p[0],p[1]
                    game_board.append((next,M))
                    game_situation[1][1] = char
        
            elif mouse_pos[0] in range(160,285) and mouse_pos[1] in range(130,240):
                if game_situation[1][2] == None:
                    p = switch_turn()
                    next, char = p[0],p[1]
                    game_board.append((next,MR))
                    game_situation[1][2] = char
            
            elif mouse_pos[0] in range(55,120) and mouse_pos[1] in range(250,330):
                if game_situation[2][0] == None:
                    p = switch_turn()
                    next, char = p[0],p[1]
                    game_board.append((next,BL))
                    game_situation[2][0] = char
                    
            elif mouse_pos[0] in range(130,205) and mouse_pos[1] in range(250,330):
                if game_situation[2][1] == None:
                    p = switch_turn()
                    next, char = p[0],p[1]
                    game_board.append((next,BM))
                    game_situation[2][1] = char
        
            elif mouse_pos[0] in range(160,285) and mouse_pos[1] in range(250,330):
                if game_situation[2][2] == None:
                    p = switch_turn()
                    next, char = p[0],p[1]
                    game_board.append((next,BR))
                    game_situation[2][2] = char
            
            elif mouse_pos[0] in range(450,550) and mouse_pos[1] in range(175,275):
                game_situation = [[None for i in range(3)] for i in range(3)]
                game_board = []
                
            else:
                print('Outside')
                pass

            for row in game_situation:
                if row[0] == row[1] == row[2] != None:
                    print("VOITTO!")
                    
            for i in range(3):
                if game_situation[0][i] == game_situation[1][i] == game_situation[2][i] != None:
                    print("HUHHUH")
            
            if game_situation[0][0] == game_situation[1][1] == game_situation[2][2] != None:
                    print("HUHHUH")
            
            if game_situation[0][2] == game_situation[1][1] == game_situation[2][0] != None:
                    print("HUHHUH")


    # Kanvas for game of 3x3

    #Diagonal --------------------------------------------------------------#

    startX=125; startY=65; endX=125; endY=height-65; width=5
    pygame.draw.line(screen, BLACK, (startX, startY), (endX,endY), width)
    
    startX=210; startY=65; endX=210; endY=height-65; width=5
    pygame.draw.line(screen, BLACK, (startX, startY), (endX,endY), width)

    #-----------------------------------------------------------------------#


    # Horizontal------------------------------------------------------------#
    
    startX=50; startY=155; endX=290; endY=155; width=5
    pygame.draw.line(screen, BLACK, (startX, startY), (endX,endY), width)

    startX=50; startY=245; endX=290; endY=245; width=5
    pygame.draw.line(screen, BLACK, (startX, startY), (endX,endY), width)

    #----------------------------------------------------------------------# 


    for char, pos in game_board:
        screen.blit(char,pos)

    screen.blit(Retry,(450,175))


    
    pygame.display.update()
