import pygame

from surfaces.map import Map

class Star_baze:
    def __init__( self ):
        pygame.init()
        self.map = Map()
        self.size = 10
        self.pos = [ 5, 5 ]
        self.zoom = self.map.map_zoom

        self.body = pygame.Rect( self.pos[ 0 ], self.pos[ 1 ], self.size * self.zoom, self.size * self.zoom )
 
        
    def render( self, surface ):
        self.body = pygame.Rect( self.pos[ 0 ], self.pos[ 1 ], self.size * self.zoom, self.size * self.zoom )
        pygame.draw.rect( surface, ( 225, 225, 0 ) ,self.body )