import pygame
import math

from pygame import mixer

pygame.init()

clock = pygame.time.Clock()
FPS = 60

current_time = 0
button_press_time = 0

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 756

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Crocketdile')

#Background Sound
mixer.music.load("Groovy-house-music.mp3")
mixer.music.play(-1)

#load image
bg = pygame.image.load('sewer_background.jpg').convert()
bg_width = bg.get_width()

#define game variables
scroll = 0
dif = 4
tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1
print(tiles)

#game loop
run = True
while run:

    clock.tick(FPS)

    #draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
    
    #scroll background + speeds scroll
    scroll -= dif
    current_time = pygame.time.get_ticks()
    if current_time % 5000 < 10:
        dif += 1
        print('Speed up by', dif,)

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

