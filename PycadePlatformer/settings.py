import pygame
from levelselect import levelMap
    

tilesize = 64   
SCREENWIDTH = 1200
SCREENHEIGHT = len(levelMap * tilesize)
size = SCREENWIDTH, SCREENHEIGHT

BLACK = 0, 0, 0
PINK = 255, 8, 255
SCREEN = pygame.display.set_mode(size)