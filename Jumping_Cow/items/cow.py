import pygame

class Cow():
    def __init__( self , pos ,screen, image, image_fall ):
        self.pos = pos
        self.start_y = pos[1]

        self.cow_image = image
        self.cow_image_fall = image_fall
        self.screen = screen

        self.velocity = 0
        self.jump_stage = 0
        self.jump_height = 24

    def update( self , move = False ):
                
        self.velocity = min( 12, self.velocity + 3 )
        
        if self.jump_stage > self.jump_height:
            self.jump_stage = 0

        if move and self.jump_stage == 0:
            self.jump_stage = 1

        if self.jump_stage and self.jump_stage <= ( self.jump_height / 2 ):

            self.jump_stage += 1
            self.pos = ( 10 , (self.pos[1] - self.velocity) )

        elif self.jump_stage > ( self.jump_height / 2) :
            self.jump_stage += 1
            self.pos = ( 10 , (self.pos[1] + self.velocity) )




        if self.pos[1] >= self.start_y or self.jump_stage == ( self.jump_height / 2 ) + 1:
            self.velocity = 0


    def body_update(self , width, height):
        x = int(self.pos[0])
        y = int(self.pos[1])
        self.colision_area = pygame.Rect(x , y , width , height )

    def render( self):
        if self.jump_stage <= ( self.jump_height / 2 ):
            self.screen.blit ( self.cow_image, ( self.pos ) )
        else: 
            self.screen.blit ( self.cow_image_fall, ( self.pos ) )