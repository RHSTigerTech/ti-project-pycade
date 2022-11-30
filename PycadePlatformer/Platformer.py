import pygame, sys, os
#import classes
from settings import *
from levelselect import levelMap
from level import Level

pygame.init() #initialize pygame

os.chdir('Plat_images') #find all files 

#Variables:

#Initial Player Dimensions
playerX = 400
playerY = 100
playerWidth = 50
playerHeight = 50
jumpPower = 10

#testing level setup
level = Level(levelMap, SCREEN)
level.setupLevel(levelMap, 1, 'Grass')
while 1: # keeps gameloop running until game over

    pygame.time.delay(40) # sets action delay and slows down code for more responsive

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