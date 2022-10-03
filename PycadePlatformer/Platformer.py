import pygame, sys
from settings import *
from levelselect import levelMap
pygame.init()

#New Variables:

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
class player(): # class for player

    def __init__(self, playerX, playerY, playerWidth, playerHeight): # class constructor function: it holds the arguments for the class and is automaically run.
        self.X = playerX
        self.Y = playerY
        self.width = playerWidth
        self.height = playerHeight
        self.jumpPower = 10

        self.closePlat = []

        self.needsGravity = False
        self.jump = False
        self.grounded = False
        self.fall = False
        print("player created")

    def drawPlayer(self):
        pygame.draw.rect(SCREEN, PINK, (self.X, self.Y, self.width, self.height))

    #movement functions:
    def playerMove(self, direction):
        if direction == "left":
            self.X -= 10
        if direction == "right":
            self.X += 10
        if direction == "jump":
            self.jump = True
    
    def gravityCheck(self, level):
        platCounter = 0
        self.grounded = False
        
        platDist = 0
        #determine to fall
        for platform in level:
            if self.X + 50 >= platform[0] and self.X - 50 <= (platform[0] - 50) + platform[2]:
                #Determines if inside of a platform on X
                if self.Y >= platform[1] - 50 and self.Y <= ((platform[1] - 50) + platform[3]):

                    platCounter += 1
                    #determines which platform is closer if mulitple hit
                    if platform[1] - (self.Y - self.height) > platDist:
                        if platDist >= 0: 
                            platDist = platform[1] - (self.Y - self.height)
                            self.closePlat = [platform[0], platform[1], platform[2], platform[3]]
  
        if platCounter == 0:
            self.Y += 10
        else:
            self.Y = self.closePlat[1] - 50
            self.jump = False
            self.grounded = True
            self.jumpPower = 10

    def wallCheck(self, level):
        for platform in level:
            if self.Y >= platform[1] - 50 and self.Y <= ((platform[1] - 50) + platform[3]) and self.grounded == False:
                #determines if on same Y as platform
                if self.X + 50 >= platform[0] and self.X - 50 <= (platform[0] - 50) + platform[2]:
                    self.X = platform[0] - 50
                
class map():
    def __init__(self, levelMap):
        self.map = levelMap

    def drawlevel(self):
        tileYCount = -1
        for row in self.map:
            tileXCount = -1
            tileYCount += 1
            for cell in row:
                tileXCount += 1
                # print(tileXCount)
                tileX = tileXCount * tilesize
                tileY = tileYCount * tilesize
                if cell == "X":
                    
                    # print((tileX, tileY, tilesize, tilesize))
                    pygame.draw.rect(SCREEN, TEMPGROUND, (tileX, tileY, tilesize, tilesize))
            

testlevel = map(levelMap)

#gameloop

player = player(playerX, playerY, playerWidth, playerHeight) #create player object

while 1: # keeps gameloop running
    pygame.time.delay(40) # sets action delay
    
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            sys.exit()

    if player.jump == False:
        if keys[pygame.K_RIGHT]:
           player.playerMove("right")
        if keys[pygame.K_LEFT]:
           player.playerMove("left")
        if keys[pygame.K_SPACE] and player.grounded == True:
            player.jump = True
            player.grounded = False
            player.Y -= (player.jumpPower * abs(player.jumpPower)) * 0.5
            player.jumpPower -= 1
    if player.jump == True:
        player.Y -= (player.jumpPower * abs(player.jumpPower)) * 0.5
        player.jumpPower -= 1

        if keys[pygame.K_RIGHT]:
           player.playerMove("right")
        if keys[pygame.K_LEFT]:
           player.playerMove("left")
            
    SCREEN.fill(BLACK)


    player.drawPlayer()
    testlevel.drawlevel()
    
    pygame.display.flip()