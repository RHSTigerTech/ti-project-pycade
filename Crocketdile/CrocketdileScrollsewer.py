import pygame
import math

from pygame import mixer

pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 756

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Crocketdile')

#Background Sound
mixer.music.load("Groovy-house-music.mp3")
mixer.music.play(-1)

#load image
bg = pygame.image.load('sewer_V2.jpg').convert()
bg_width = bg.get_width()
#bg_rect = bg.get_rect()

#define game variables
scroll = 0
tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1
print(tiles)

#game loop
run = True
while run:

    clock.tick(FPS)

    #draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
       # bg_rect.x = i * bg_width + scroll
       # pygame.draw.rect(screen, (255, 0, 0), bg_rect, 1)
    
    #scroll background
    scroll -= 5

    #reset scroll
    if abs(scroll) > bg_width:
        scroll = 0

    #movement + event handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("Up arrow is pressed")
            if event.key == pygame.K_DOWN:
                print("Down arrow is pressed")
            if event.key == pygame.K_SPACE:
                print("Space Bar is pressed")
            if event.key == pygame.K_e:
                print("E key is pressed")
            if event.key == pygame.K_ESCAPE:
               run = False
        elif event.type == pygame.QUIT:
            run = False





    pygame.display.update()

pygame.quit()

