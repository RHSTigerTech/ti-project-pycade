import pygame, os
import time
import random
from os import path
from pygame.locals import *
from pygame import mixer
import sys

os.chdir('tiger_images')

#Colors:
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0,255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

#settings:
pygame.init()
pygame.mixer.init()
WIDTH = 480 
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tiger")
clock = pygame.time.Clock()
FPS = 60
game_folder = path.dirname(__file__)
sprite_folder = path.join(game_folder, "tiger_images")
score = 0
font_name = pygame.font.match_font("comicsansms")
gameDisplay = pygame.display.set_mode((480, 600))
lose = 0


#Classes
class Player(pygame.sprite.Sprite):

    def __init__(self): 
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface((50, 30))  
        self.image = pygame.image.load('tiger.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT - 10
        self.speed_x = 0
        self.speed = 10
       
   
    
    def shoot_bullet(self):
        b = Bullet(self.rect.centerx, self.rect.top)
        all_bullets.add(b)
        all_sprites.add(b)
    
    def boundary(self):
        if self.rect.right > WIDTH:
             self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def movement(self):
        #Tigers movement
        self.speed_x = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_RIGHT]:
            self.speed_x = self.speed
        if keystate[pygame.K_LEFT]:
            self.speed_x = -self.speed
        self.rect.x += self.speed_x
        if lose == 1:
             self.rect.y = random.randrange(15000, 100000)
             self.speed_y = random.randrange(2, 8)
             self.speed_x = random.randrange(-3, 3)
    

        
    def WL(self):
        if score == 9000:
        #W = pygame.image.load('TigerW.jpg').convert()
         screen.blit(TigerW, (0, 580))
         screen.blit(TigerW, background_rect)
         gameDisplay.blit(background, (999, 999))
         gameDisplay.blit(wolf_img, (999, 999))
         gameDisplay.blit(bullet_img, (999, 999))
         gameDisplay.blit(player_img, (999, 999))
         
         

    def update(self):
        self.movement()  
        self.boundary()

class Wolf(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image = pygame.image.load('swolf.png') 
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-150, -100)
        self.speed_y = random.randrange(2, 8)
        self.speed_x = random.randrange(-3, 3)
      
   

    def spawn_new_wolf(self):
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-150, -100)
        self.speed_y = random.randrange(2, 8)
        self.speed_x = random.randrange(-3, 3)

    def boundary(self):
        if self.rect.right > WIDTH + 5 or self.rect.right < -5 or self.rect.top > HEIGHT + 5:
            self.spawn_new_wolf()
        if score >= 9000:
             self.rect.y = random.randrange(15000, 100000)
             self.speed_y = random.randrange(2, 8)
             self.speed_x = random.randrange(-3, 3)
        

    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        self.boundary()

class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y): #X and Y repersents middle of ship
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image = pygame.image.load("fireball.png ")
        self.rect = self.image.get_rect()
        self.rect.x = -10  
        self.rect.x = x
        self.rect.y = y 
        self.speed_y = -10    

    def update(self):
        self.rect.y += self.speed_y                                                                     
#Functions
def spawn_new_wolf():
    w = Wolf()
    all_wolfs.add(w)
    all_sprites.add(w)


def get_image(filename):
    img = pygame.image.load(path.join(sprite_folder, filename)).convert()
    return img


def message_to_screen(message, color, font_size, x, y):
    font = pygame.font.SysFont(font_name, font_size)
    text = font.render(message, True, color)
    text_rect = text.get_rect()
    text_rect.center = (x, y)
    screen.blit(text, text_rect)

 
#Images
background = get_image("background.jpg")
background_rect = background.get_rect()
player_img = get_image("tiger.png")
bullet_img = get_image("fireball.png")
wolf_img = get_image("swolf.png")
wolfL = get_image("wolfL.jpg")
TigerW = get_image("TigerW.jpg")

     
#sprites
all_sprites = pygame.sprite.Group()
all_wolfs = pygame.sprite.Group() #Group the wolfs
all_bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

for i in range(5):
    spawn_new_wolf()
   
    
#Main game loop
running = True
while running:
    #Game runs at 60 FPS
    clock.tick(FPS)

    #Check for event:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.key == pygame.K_SPACE:
               player.shoot_bullet()
           

    #Update
    if score <= 9000:
        all_sprites.update()


        #if wolf hits tiger 
        wolf_collision = pygame.sprite.spritecollide(player, all_wolfs, False)
        if wolf_collision:
            player.WL()
            background = get_image("wolfL.jpg")
            gameDisplay.blit(background, (999, 999))
            gameDisplay.blit(wolf_img, (999, 999))
            gameDisplay.blit(bullet_img, (999, 999))
            gameDisplay.blit(player_img, (999, 999))
            lose += 1
            spawn_new_wolf = False
            

            #L = pygame.image.load("wolfL.png").convert()
            # L_width = L.get_width()
            
            

        #if bullet hits wolf
        bullet_collision = pygame.sprite.groupcollide(all_wolfs, all_bullets, True, True)
        for collision in bullet_collision:
            spawn_new_wolf()
            score += 10
        


    

    if score >= 9000:
        player.WL()
        background = get_image("TigerW.jpg")
        #background_rect = background.get_rect()
        #bg = pygame.image.load('TigerW.jpg').convert()
        screen.blit(TigerW, (0, 580))
        gameDisplay.blit(background, (999, 999))
        gameDisplay.blit(wolf_img, (999, 999))
        gameDisplay.blit(bullet_img, (999, 999))
        gameDisplay.blit(player_img, (999, 999))
       
        #screen.blit(TigerW, background_rect)
        #time.sleep(2)
        # running = False


   # mouseX = pygame.mouse.get_pos()[0]
    #mouseY = pygame.mouse.get_pos()[1]   
    #print(mouseX, mouseY)
    #Draw to the screen:
    screen.blit(background, background_rect) 
    all_sprites.draw(screen)
    message_to_screen("Score: " + str(score), WHITE, 24, WIDTH/2, 10) 
   

 
    #Updte adter drawing everything to screen
    pygame.display.update()

pygame.quit()                         
