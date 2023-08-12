import pygame

BASE_IMG_PATH = 'images/'

def load_image( path ):
    img = pygame.image.load( BASE_IMG_PATH + path ).convert()
    img.set_colorkey((0, 0, 100))
    return img