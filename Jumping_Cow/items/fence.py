import pygame

import random

import gc

class Fence():
    def __init__( self , speed , pos ):
        self.pos = pos
        self.speed = speed
    def update ( self ):
        self.pos = ( self.pos[ 0 ] - self.speed, self.pos[ 1 ] )

    def collision( self , width, height ):
        x = int( self.pos [ 0 ] )
        y = int( self.pos [ 1 ] )

        self.colision_area = pygame.Rect( x , y , width , height )
        
    def render( self , assets, screen):
        screen.blit ( assets, ( self.pos ) )       

class Fences():
    def __init__( self , speed, count ):
        self.fences = [ ]
        self.distans = 450
        self.speed = speed
        self.count = count

        for i in range( self.count ):
            self.fences.append( Fence ( self.speed ,(  random.randrange( self.distans , self.distans + 100  ), 237 ) ) )
            self.distans += 500
    def update ( self ):
        for fence in self.fences:
            fence.update()

    def collision( self , width, height ):
        for fence in self.fences:
            fence.collision( width, height )

    def render( self, assets, screen ):
        for fence in self.fences:

            fence.render( assets, screen )

    def del_old( self ):
        # self.fences = [ fence for fence in self.fences if ??? ] #if fence.pos[ 0 ] > fence[ 0 ].pos[ 0 ]]
        self.fences = [fence for index, fence in enumerate(self.fences) if index > 0]

        gc.collect()

    def get_new( self ):
        if len ( self.fences ) == 2:
            self.distans = self.fences[ 1 ].pos[ 0 ] + 400
            for i in range( self.count ):
                self.fences.append( Fence ( self.speed ,(  random.randrange( self.distans , self.distans + 100  ), 237 ) ) )
                self.distans += 700