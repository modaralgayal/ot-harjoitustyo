import pygame 
import os
from random import choice
import random

width = 700
height = 400

pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Ristinolla")
clock = pygame.time.Clock()


WHITE = (255,255,255)
PURPLE = (255,0,255)
BLACK = (0,0,0)

X = pygame.image.load("src/assets/X.png").convert_alpha()
O = pygame.image.load("src/assets/circle.png").convert_alpha()

UL = (60,85);  UM = (145,85);  UR = (230,85)   # UpperLeft, UpperMiddle, UpperRight 
ML = (60,175);  M = (145,175); MR = (230,175)  # MiddleLeft, Middle, MiddleRight 
BL = (60,265); BM = (145,265); BR = (230,265) # BottomLeft, BottomMiddle, BottomRight


game_board = []

def alternate():
    while True:
        yield X
        yield O

switch = alternate()

randomize = random.choice([True,False])

if randomize:
    switch.__next__()



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
                if UL not in game_board:
                    game_board.append(UL)
            elif mouse_pos[0] in range(130,205) and mouse_pos[1] in range(70,150):
                if UM not in game_board:
                    game_board.append(UM)
            elif mouse_pos[0] in range(160,285) and mouse_pos[1] in range(70,150):
                if UR not in game_board:
                    game_board.append(UR)
            
            elif mouse_pos[0] in range(55,120) and mouse_pos[1] in range(130,240):
                if ML not in game_board:
                    game_board.append(ML)
            elif mouse_pos[0] in range(130,205) and mouse_pos[1] in range(130,240):
                if M not in game_board:
                    game_board.append(M)
            elif mouse_pos[0] in range(160,285) and mouse_pos[1] in range(130,240):
                if MR not in game_board:
                    game_board.append(MR)
            
            elif mouse_pos[0] in range(55,120) and mouse_pos[1] in range(250,330):
                if BL not in game_board:
                    game_board.append(BL)
            elif mouse_pos[0] in range(130,205) and mouse_pos[1] in range(250,330):
                if BM not in game_board:
                    game_board.append(BM)
            elif mouse_pos[0] in range(160,285) and mouse_pos[1] in range(250,330):
                if BR not in game_board:
                    game_board.append(BR)
            else:
                print("Outside")
                pass


    key = pygame.key.get_pressed()


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



    for pos in game_board:
        screen.blit(switch.__next__(),pos)


    
    pygame.display.update()
    clock.tick(30)
