import pygame, sys, os
#imports from other files
from settings import *
from levelselect import levelMap
from level import Level

pygame.init() #initialize pygame

os.chdir('Plat_images') #find all files 

#New Variables:

level = Level(levelMap, SCREEN)
#Player Dimensions
playerX = 400
playerY = 100
playerWidth = 50
playerHeight = 50
jumpPower = 10

#Colors:

BLACK = 0, 0, 0
PINK = 255, 8, 255
TEMPGROUND = 74, 170, 189
TestColor = 232,157,76

#gameloop
level = Level(levelMap, SCREEN)
level.setupLevel(levelMap, 'Grass')

while 1: # keeps gameloop running
    pygame.time.delay(40) # sets action delay 

    #Sets Screen Background
    SCREEN.fill(BLUE)
    level.run() #level creation / level running
    
    #quit the game
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            sys.exit()
    
    #update the display
    pygame.display.update()