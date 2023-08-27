import sys

import pygame

from items.cow import Cow
from items.fence import Fences


from scripts.load_images import load_image

class Game():
    def __init__( self ):
        pygame.init()
        pygame.display.set_caption('Jumping_Cow by Adrian Jarząb')

        self.font = pygame.font.SysFont('Segoe', 26)
        self.WIDHT = 800
        self.HEIGHT = 300
        self.screen = pygame.display.set_mode( ( self.WIDHT, self.HEIGHT ) )

        self.clock = pygame.time.Clock()
        self.speed = 15

        self.score_text = 0
        self.move = False

        self.run_game = False

        self.assets = {
            'cow' : load_image( 'cow2.png' ),
            'cow_fall' : load_image( 'cow_falls.png'),
            'background' : load_image ( 'background.png' ),
            'fence' : load_image ('fence2.png')
        }

        self.cow = Cow( ( 10.0, 237.0 ), self.screen ,self.assets['cow'], self.assets['cow_fall'] )
        self.fences = Fences ( self.speed , 4 )

        self.score = 0

    def score_count( self ):

        if  pygame.Rect( 0 , 237 , self.speed -1  , self.HEIGHT ).colliderect(pygame.Rect( self.fences.fences[ 0 ].pos[ 0 ] , self.fences.fences[ 0 ].pos[ 1 ] , 1 , self.HEIGHT )):
            self.score += 1            
            self.fences.del_old()

    def lose( self ):
        if self.cow.colision_area.colliderect(self.fences.fences[ 0 ].colision_area):
            self.font = pygame.font.SysFont('Segoe', 60)
            self.lost_text = self.font.render('You Lost', True, ( 225, 0, 0) )
            self.screen.blit(self.lost_text, ( ( self.WIDHT / 2 ) - 100, ( self.HEIGHT /2 ) - 30 ) )
            pygame.display.update()
            pygame.time.delay( 4000 )
            Game().run()

    def events( self ):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit( 0 )
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.move = True
                        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.move = False

    def render( self ):
        

        self.screen.fill( ( 0, 0, 225 ) )
        self.score_text = self.font.render('Score: ' + str(self.score), True, (255, 255, 255))      #???   
        self.screen.blit ( self.assets['background'], ( 0, 0 ) )
        self.fences.render( self.assets['fence'], self.screen )
        
        self.cow.render()

        self.screen.blit(self.score_text, (10, 10))
        pygame.display.update()

        self.clock.tick( 60 )

        pygame.time.delay( 50 )

    def menu( self ):
        self.menu_text = self.font.render('Easy = 1 Medium = 2 Hard = 3', True, (0, 0, 0) )

        self.screen.blit ( self.assets['background'], ( 0, 0 ) )
        
        self.screen.blit(self.menu_text, (10, 10))
        
        self.cow.render()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit( 0 )
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.speed = 15
                    self.run_game = True

                if event.key == pygame.K_2:
                    self.speed = 20
                    self.run_game = True

                if event.key == pygame.K_3:
                    self.speed = 25
                    self.run_game = True

    def run( self ):
        while True:
            self.menu()

            while self.run_game:
                

                self.fences.get_new()

                self.cow.update( self.move )

                self.fences.update()

                self.fences.collision( self.assets['fence'].get_width() , self.assets['fence'].get_height() )
                self.cow.body_update( self.assets['cow'].get_width() , self.assets['cow'].get_height() )

                self.events()


                self.lose()
                self.score_count()

                self.render()
Game().run()