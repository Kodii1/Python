import pygame

import sys

from surfaces.map import Map
from surfaces.toolbox import  Tool_box

from buildings.star_base import Star_baze

class Game: 
    def __init__(self):
        pygame.init()
        self.WIDTH = 1280
        self.HEIGHT = 720
        self.screen = pygame.display.set_mode( (self.WIDTH, self.HEIGHT) )

        self.tool_box =  Tool_box()
        self.map = Map()
        clock = pygame.time.Clock()

    def render(self):
        self.screen.fill( ( 0, 0, 0, ) )

        self.tool_box.render( self.screen )
        self.map.render( self.screen )

        pygame.display.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit( 0 )
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
    def run_game(self):


        while True:
            self.events()
            self.render()

if __name__ == '__main__':
    Game().run_game()