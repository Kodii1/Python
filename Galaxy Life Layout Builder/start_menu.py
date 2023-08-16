import pygame

import sys

from scripts.load_images import load_image
from buttons import Buttons

from main import Game

class Menu():
    def __init__( self ):
        pygame.init()
        self.screen = pygame.display.set_mode( (709, 280) )

        self.background =  load_image( 'background.png')

        self.buttons = Buttons( self.screen )

        self.ran_menu = True

    def render( self ):
        self.screen.fill( ( 0, 0, 0 ) )
        self.screen.blit( self.background, ( 0, 0 ) )

        for i in range(len( self.buttons.buttons ) ):
            self.screen.blit( self.buttons.buttons[ i ].image, ( self.buttons.buttons[ i ].pos[ 0 ], self.buttons.buttons[ i ].pos[ 1 ] ) )
        
        pygame.display.update()

    def events( self ):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for i in range ( len( self.buttons.buttons ) ):
                        if self.buttons.buttons[ i ].colission_area.collidepoint(pygame.mouse.get_pos() ) :
                            self.baze_lvl = i + 1
                            self.ran_menu = False
                            pygame.quit()
                            Game().run_game()
    def run( self ):
        while self.ran_menu:
            self.events()
            self.render()

        




if __name__ == "__main__":
    Menu().run()