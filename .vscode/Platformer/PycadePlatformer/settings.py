import pygame
from levelselect import levelMap
    

tilesize = 64   
SCREENWIDTH = 1200
SCREENHEIGHT = len(levelMap * tilesize)
size = SCREENWIDTH, SCREENHEIGHT

BLACK = 0, 0, 0
PINK = 255, 8, 255
YELLOW = 209, 209, 50
GREY = 129, 138, 132
SCREEN = pygame.display.set_mode(size)