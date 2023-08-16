from scripts.load_images import load_image
import pygame

class Button():
    def __init__( self, image , pos ):
        self.pos = pos
        self.image = image
        self.size = ( image.get_width() , image.get_height() )
        self.colission_area = pygame.Rect( self.pos[ 0 ], self.pos[ 1 ], self.size[ 0 ], self.size[ 1 ] ) 


class Buttons():
    def __init__( self, screen ):
        self.screen = screen
        self.buttons = []
        self.start_pos = [ 310, 150 ]

        for i in range( 1 , 10 ):
            self.buttons.append( Button( load_image( f'button{i}.png' ), [ self.start_pos [ 0 ],  self.start_pos[ 1 ] ] ) )
            self.start_pos [ 0 ] += 60

            if i == 5:
                self.start_pos [ 0 ] = 310
                self.start_pos [ 1 ] = 210


        pygame.display.update()