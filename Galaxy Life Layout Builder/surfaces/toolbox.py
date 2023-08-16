import pygame

from buildings.star_base import Star_baze

class Tool_box:
    def __init__( self ):
        self.pos = [ 500 , 10 ]
        self.tool_box_size = 72
        self.tool_box_zoom = 9
        self.surf = pygame.Surface( ( self.tool_box_size * self.tool_box_zoom, self.tool_box_size * self.tool_box_zoom) )
        
    def render( self, surf ):    
        self.surf.fill( ( 225, 225, 225 ) )

        Star_baze().render( self.surf )

        surf.blit ( self.surf , ( 700, 10) )
