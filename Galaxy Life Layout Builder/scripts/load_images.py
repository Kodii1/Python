import pygame

DEFAULT_PATH = 'images/'
def load_image( path ):
    pygame.init()
    img = pygame.image.load( DEFAULT_PATH + path ).convert()
    img.set_colorkey( ( 225, 225, 225 ) )
    return img