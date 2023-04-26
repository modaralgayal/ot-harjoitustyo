import unittest
from gameloop import Gameloop
from renderer import Renderer
from main import main
from event_pueue import EventQueue
import pygame


width = 700
height = 400
display = pygame.display.set_mode((width, height))

game_board = []
game_situation = [[None for i in range(3)] for i in range(3)]

UL = (60, 85)
UM = (145, 85)
UR = (230, 85)   # UpperLeft, UpperMiddle, UpperRight
ML = (60, 175)
M = (145, 175)
MR = (230, 175)  # MiddleLeft, Middle, MiddleRight
BL = (60, 265)
BM = (145, 265)
BR = (230, 265)  # BottomLeft, BottomMiddle, BottomRight

places_on_board = [UL, UM, UR, ML, M, MR, BL, BM, BR]


class TestGameLoop(unittest.TestCase):

    def setUp(self):

        pass

    def test_game_loop_constructor(self): 

        renderer = Renderer(display, height)

        game_loop = Gameloop(game_board, game_situation, renderer, width, height, UL, UM, UR, ML, M, MR, BL, BM, BR)

        assert game_loop._renderer == renderer
        assert game_loop.screen == pygame.display.set_mode((width, height))
        assert game_loop.game_board == []
        assert game_loop.game_situation == [[None for i in range(3)] for i in range(3)]


class StubEvent():

    def __init__(self, event_type, position = None):
        
        self.type = event_type
        self.pos = pygame.mouse.set_pos(position)

class StubQuit():

    def __init__(self, event_type):
            
            self.type = event_type



class StubEventQueue():

    def __init__(self, events):
        
        self._events = events


    def get(self):

        return self._events
    
class StubRenderer():

    def render(self, game_board):

        pass



class TestGameLoop(unittest.TestCase):

    def setUp(self):

        self.click_ranges = [((55,120),(70,150)),((130,205),(70,150)),((160,285),(70,150)),
                             ((55,120),(130,240)),((130,205),(130,240)),((160,285),(70,240)),
                             ((55,120),(250,330)),((130,205),(250,330)),((160,285),(250,330))
                             ]
    

    def test_can_save_coordinates_correctly(self):

        game_board = []
        game_situation = [[None for i in range(3)] for i in range(3)]
        renderer = StubRenderer()

        events = []

        for place in self.click_ranges:

            click = StubEvent(pygame.MOUSEBUTTONDOWN, (place[0][0]+5,place[1][0]+5))
            events.append(click)
        
        events.append(StubQuit(pygame.QUIT),(0,0))
        
        
        game_loop = Gameloop(
            StubEventQueue(events),
            game_board, 
            game_situation, 
            renderer, 
            width, 
            height, 
            places_on_board,
            self.click_ranges
        )

        game = game_loop.start()

        assert game == [[None for i in range(3)] for i in range(3)]

        for row in game:
            for char in row:
                assert char == 'X' or char == 'O'
                print('Meni läpi')