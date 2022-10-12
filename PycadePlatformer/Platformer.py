import pygame, sys
from settings import *
from levelselect import levelMap
from level import Level
from player import Player
pygame.init()

#New Variables:

level = Level(levelMap, SCREEN)

#Player Dimensions
playerX = 400
playerY = 100
playerWidth = 50
playerHeight = 50
jumpPower = 10

#platform data variables



#Static Variables:


#Colors:

BLACK = 0, 0, 0
PINK = 255, 8, 255
TEMPGROUND = 74, 170, 189
TestColor = 232,157,76

#gameloop
level = Level(levelMap, SCREEN)
level.setupLevel(levelMap)

while 1: # keeps gameloop running
    pygame.time.delay(40) # sets action delay

    

    SCREEN.fill(BLACK)
    level.run()
    # print("run")
    
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            sys.exit()
    
    
    pygame.display.update()