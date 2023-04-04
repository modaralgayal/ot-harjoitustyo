import pygame 
import os

width = 700
height = 400

pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("First Game")
clock = pygame.time.Clock()


WHITE = (255,255,255)
PURPLE = (255,0,255)
BLACK = (0,0,0)

X = pygame.image.load("src/assets/X.png").convert_alpha()
O = pygame.image.load("src/assets/circle.png").convert_alpha()

UL = (60,85); UM = (145,85);  UR = (230,85)   # UpperLeft, UpperMiddle, UpperRight 
ML = (60,175); M = (145,175); MR = (230,175)  # MiddleLeft, Middle, MiddleRight 
BL = (60,265); BM = (175,265); BR = (230,265) # BottomLeft, BottomMiddle, BottomRight


game_board = [[None for _ in range(3)] for _ in range(3)]
print(game_board)

while True:

    pygame.time.delay(100)

    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit() 
        if event.type == pygame.MOUSEBUTTONDOWN:
            left_mouse_key = pygame.mouse.get_pressed()[0]
            mouse_pos = pygame.mouse.get_pos()
            print("Pressed")

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

    # Images for X and O


    # 1st level:
    screen.blit(X,UL)
    screen.blit(O,UM)
    # 2nd level:
    screen.blit(X,ML)
    screen.blit(O,MR)
    # 3rd level:
    screen.blit(X,BL)
    screen.blit(O,BR)



    
    pygame.display.update()
    clock.tick(30)
