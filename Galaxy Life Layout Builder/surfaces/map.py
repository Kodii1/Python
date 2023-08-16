import pygame

class Map:
    def __init__( self ):
        self.pos = [ 10 , 10 ]
        self.map_size = 72
        self.map_zoom = 9
        self.surf = pygame.Surface( ( self.map_size * self.map_zoom, self.map_size * self.map_zoom) )
        
    def render( self, surf):    
        self.surf.fill( ( 225, 225, 225 ) )

        for i in range( 1, self.map_size ): #X
            pygame.draw.line( self.surf, ( 0, 0, 0 ), ( 0, i * self.map_zoom ), ( self.pos[ 0 ] + self.map_size * self.map_zoom, i * self.map_zoom ) )

        for i in range( 1, self.map_size ): #Y
            pygame.draw.line( self.surf, ( 0, 0, 0 ), ( i * self.map_zoom, 0 ), (  i * self.map_zoom, self.pos[ 0 ] + self.map_size * self.map_zoom ) )
            
        surf.blit( self.surf, ( self.pos[ 0 ], self.pos[ 1 ] ) )
