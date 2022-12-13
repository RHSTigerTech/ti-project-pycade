import pygame, os
from levelselect import levelMap

tilesize = 64   
SCREENWIDTH = 1200
SCREENHEIGHT = len(levelMap * tilesize) #aka 768
size = SCREENWIDTH, SCREENHEIGHT

BLACK = 0, 0, 0
PINK = 255, 8, 255
YELLOW = 209, 209, 50
GREY = 129, 138, 132
BLUE = 66, 135, 245
RED = 250, 5, 5
SCREEN = pygame.display.set_mode(size)
PLAYERSPEED = 8