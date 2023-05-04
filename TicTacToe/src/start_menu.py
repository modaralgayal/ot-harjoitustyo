import pygame

pygame.init()

HEIGHT = 400
WIDTH = 700

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Main menu')

WHITE = (255,255,255)
RED = (255,0,0)

text_font = pygame.font.SysFont(None, 40)

class Draw_Menu:

    def draw_text(text, font, text_col, x, y):

        img = font.render(text, True, text_col)
        screen.blit(img, (x,y))

grid_sizes = [("3x3",(100,200),3),("4x4",(210,200),4),("5x5",(320,200),5),("6x6",(430,200),6),("7x7",(540,200),7)]
GRID_SIZE = None


run = True
while run:

    screen.fill(WHITE)

    Draw_Menu.draw_text("Choose Grid", text_font, (0,0,0), 267.5, 100)

    for text, coord, value in grid_sizes:

        Draw_Menu.draw_text(text, text_font, RED, coord[0],coord[1])

    for event in pygame.event.get():
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            
            for text,coord,value in grid_sizes:
                
                if pos[0] in range(coord[0],coord[0]+45) and pos[1] in range(coord[1],coord[1]+27):
                    GRID_SIZE = value
                    run = False

        if event.type == pygame.QUIT:
            run = False
    
        
    pygame.display.update()

pygame.quit()