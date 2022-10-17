import pygame
import Crocodile2
import random

pygame.init()

SCREEN_WIDTH = 1700
SCREEN_HEIGHT = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('My Spritesheet Thingy')

sprite_sheet_image = pygame.image.load('CrocodileSpritesheetMini.png').convert_alpha()
sprite_sheet = Crocodile2.SpriteSheet(sprite_sheet_image)
Coin = pygame.image.load("Coin.png")

x = 0
y = 300
CoinX = 300
CoinY = 100
rect = sprite_sheet_image.get_rect()
rect.center = (x, y)
BG = (50, 50, 50)
BLACK = (0, 0, 0)
Player = sprite_sheet_image
score = 0
step = 5
CoinMove = random.randrange(0.2*SCREEN_WIDTH, 0.8*SCREEN_WIDTH), 0

#create animation list
animation_list = []
animation_steps = [3, 3, 3, 3, 3, 3]
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 150
frame = 0
step_counter = 0

for animation in animation_steps:
    temp_img_list = []
    for _ in range(animation):
        temp_img_list.append(sprite_sheet.get_image(step_counter, 894, 490, 2, BLACK))
        step_counter += 1
    animation_list.append(temp_img_list)

print(animation_list)



run = True
while run:


		#update background
		screen.fill(BG)

		#update animation
		current_time = pygame.time.get_ticks()
		if current_time - last_update >= animation_cooldown:
			frame += 1
			last_update = current_time
			if frame >= len(animation_list[action]):
				frame = 0

		#show frame image
		screen.blit(animation_list[action][frame], (x, y))
		screen.blit(Coin, (CoinX, CoinY))

		CoinMove +=step

		#event handler
		for event in pygame.event.get():
			keys = pygame.key.get_pressed()
			if keys[pygame.K_w]:
				action = 1
				y -= 50
			if keys[pygame.K_s]:
				action = 1
				y += 50
			if keys[pygame.K_SPACE]:
				action = 2
			if event.type == pygame.QUIT:
				run = False

		pygame.display.update()

pygame.quit()
