from time import sleep
from turtle import back
import pygame
pygame.init()
from random import uniform, randint
import time
import os

windowSize = [1366, 768]
screen = pygame.display.set_mode(windowSize)
backcolour = pygame.color.Color('#010520')

#sets the window size
gameDisplay = pygame.display.set_mode((1366, 768))

#file for images
os.chdir('Arcade_Project_Images')

#loads in your pics to use later
Titlep = pygame.image.load('Title.jpeg')
WBox = pygame.image.load('Box.jpeg')
WSBox = pygame.image.load('RatingBox.jpeg')
WSBox1 = pygame.image.load('RatingBox.jpeg')
WSBox2 = pygame.image.load('RatingBox.jpeg')
WSBox3 = pygame.image.load('RatingBox.jpeg')
CrocketdileGame = pygame.image.load('Crocketdile4.jpg')
Gthumb = pygame.image.load('GreenThumb.jpeg')
Gthumb1 = pygame.image.load('GreenThumb.jpeg')
Gthumb2 = pygame.image.load('GreenThumb.jpeg')
Gthumb3 = pygame.image.load('GreenThumb.jpeg')
Rthumb = pygame.image.load('RedThumb.jpeg')
Rthumb1 = pygame.image.load('RedThumb.jpeg')
Rthumb2 = pygame.image.load('RedThumb.jpeg')
Rthumb3 = pygame.image.load('RedThumb.jpeg')
Arrow = pygame.image.load('Arrow.png')
Gamemenu = pygame.image.load('W1.jpeg')
DY = pygame.image.load('DevinYon.jpeg')
X = pygame.image.load('X1.jpg')
PlayButton = pygame.image.load('Playbutton.jpeg')
InfoButton = pygame.image.load('Infobutton.jpeg')
BlueScreen = pygame.image.load('BlueScreen.jpeg')
BigCi = pygame.image.load('BigCrocketdile.jpeg')
CrocketdileNi = pygame.image.load('CrocketdileNamei.jpeg')
CrocketdileDi = pygame.image.load('CrocketdileDescription.jpeg')
Leaderboard= pygame.image.load('leaderboard.jpeg')

innerMenu = False
Info = False

def drawMenu(innerMenu):
    screen.fill(backcolour)
    gameDisplay.blit(Titlep, (200, 40))
    gameDisplay.blit(WBox, (300, 300))
    gameDisplay.blit(WSBox, (100, 680))
    gameDisplay.blit(WSBox1, (400, 680))
    gameDisplay.blit(WSBox2, (700, 680))
    gameDisplay.blit(WSBox3, (1000, 680))
    gameDisplay.blit(Gthumb, (110, 697))
    gameDisplay.blit(Gthumb1, (410, 697))
    gameDisplay.blit(Gthumb2, (710, 697))
    gameDisplay.blit(Gthumb3, (1010, 697))
    gameDisplay.blit(Rthumb, (150, 696))
    gameDisplay.blit(Rthumb1, (450, 696))
    gameDisplay.blit(Rthumb2, (750, 696))
    gameDisplay.blit(Rthumb3, (1050, 696))
    gameDisplay.blit(Arrow, (1250, 530))
    if innerMenu == False:
        gameDisplay.blit(CrocketdileGame, (73, 470))

def drawInnerMenu(innerMenu):
    if innerMenu == True:
        gameDisplay.blit(Gamemenu, (73, 470))
        gameDisplay.blit(PlayButton, (150, 500))
        gameDisplay.blit(InfoButton, (150, 600))
        gameDisplay.blit(X, (310, 470))

def drawInfo(info):
    if info == True:
        gameDisplay.blit(BlueScreen, (0, 0))
        gameDisplay.blit(BigCi , (56, 62))
        gameDisplay.blit(CrocketdileNi, (688, 62))
        gameDisplay.blit(Leaderboard, (56, 560))

#DISPLAY BACKGROUND
pygame.display.update()
# sleep(1)


finished = False
while not finished:
    pygame.time.delay(100)

    #mouse location
    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]
    
    # if innerMenu == False:
    #     
    # elif Info == False:
    #     drawInnerMenu(innerMenu)
    # elif Info == True: 

    # else:
        # 
    
    # if backx == False:
    #      innermenu = True
    # else:
        #  gameDisplay.blit(X, (310, 470))
        #  gameDisplay.blit(Gamemenu, (73, 470))

    if innerMenu == False:
        if mouseX >= 105 and mouseX <= 497:
            if mouseY <= 659 and mouseY >= 470:
                if pygame.mouse.get_pressed(num_buttons=3)[0] == True: 
                    innerMenu = True
                    # print("1", innerMenu ) testing
    else:
        if innerMenu ==True:
            if mouseX >= 315 and mouseX <= 472:
                if mouseY >= 450 and mouseY <= 500:
                    if pygame.mouse.get_pressed(num_buttons=3)[0] == True:
                            innerMenu = False

            if Info == False:
                if mouseX >= 155 and mouseX <= 280:
                    if mouseY >= 605 and mouseY <= 662:
                        if pygame.mouse.get_pressed(num_buttons=3)[0] == True: 
                            Info = True
                        # print('test')



            else:
                if Info ==True:
                    if mouseX >= 155 and mouseX <= 280:
                        if mouseY >= 605 and mouseY <= 662:
                            if pygame.mouse.get_pressed(num_buttons=3)[0] == True:
                                Info = False

                                # print("2", innerMenu) testing

                            # print('test')

       
       
                    # print("1", innerMenu ) testing
    # pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True 

    
    # if mouseX >= 500 and mouseX <= 173:
        # if mouseY <= 570 and mouseY >= 470:
            # if pygame.mouse.get_pressed(num_buttons=3)[0] == True: 
# 
                    # 
                # X = True
                # print('yippe' )
    

    drawMenu(innerMenu)
    if innerMenu == True:
        drawInnerMenu(innerMenu)
        if Info == True:
            drawInfo(Info)  
   



    print(mouseX, mouseY)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True 
            






#DISPLAY YOU ARE HERE

#GAME WILL NOW EXIT UNLESS YOU LOOP IT OR ADD AN input

   
pygame.quit()
quit()
