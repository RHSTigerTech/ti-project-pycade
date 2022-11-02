import pygame
import time
import random

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
pygame.display.set_caption("Tiger Shooter!")
clock = pygame.time.Clock()
FPS = 60

#Classes
class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 30))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT - 10
        self.speed_x = 0
        self.speed = 8
    
    def boundary(self):
        if self.rect.right > WIDTH:
             self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def movement(self):
        #ships movement
        self.speed_x = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_RIGHT]:
            self.speed_x = self.speed
        if keystate[pygame.K_LEFT]:
            self.speed_x = -self.speed
        self.rect.x += self.speed_x
    


    def update(self):
        self.movement()  
        self.boundary()

class Wolf(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
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

    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        self.boundary()


#Functions

#sprites
all_sprites = pygame.sprite.Group()
all_wolfs = pygame.sprite.Group() #Group the wolfs
player = Player()
all_sprites.add(player)

for i in range(5):
    w = Wolf()
    all_wolfs.add(w)
    all_sprites.add(w)


#Main game loop
running = True
while running:
    #Game runs at 60 FPS
    clock.tick(FPS)

    #Check for event:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #Update
    all_sprites.update()

    #if wolf hits tiger

    wolf_collision = pygame.sprite.spritecollide(player, all_wolfs, False)
    if wolf_collision:
        running = False


    #Draw to the screen:
    screen.fill(GREEN)
    all_sprites.draw(screen)

    #Updte adter drawing everything to screen
    pygame.display.update()

pygame.quit()