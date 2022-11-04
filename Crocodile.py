import pygame
import Crocodile2
import random
import math

from pygame import mixer

pygame.init()

SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 756

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('The Crockettdile')

sprite_sheet_image = pygame.image.load('CrocodileSpritesheetMini.png').convert_alpha()
sprite_sheet = Crocodile2.SpriteSheet(sprite_sheet_image)
Coin = pygame.image.load("Coin.png")
Meat = pygame.image.load("Meat.png")
Trash1 = pygame.image.load("Trash1.png")
Trash2 = pygame.image.load("Trash2.png")
SewerTunnel = pygame.image.load("sewerTunnel.png")
SewerPipe = pygame.image.load("sewerPipe.png")
SewerPipe2 = pygame.image.load("sewerPipe2.png")
SewerLadder = pygame.image.load("sewerLadder.png")
SeanGraffiti = pygame.image.load("seanGraffiti.png")

clock = pygame.time.Clock()
FPS = 60

current_time = 0
button_press_time = 0

x = 0
y = 300
COINMOVEY = 400
COINMOVEX = 1800
MeatX = 1500
MeatY = 310
Trash1X = 10
Trash1Y = 10
Trash2X = 50
Trash2Y = 10
CoinSpot = random.randint(1, 3)
TunnelX = 3800
TunnelY = 10
Pipe1X = 10
Pipe1Y = -2
Pipe2X = 10000
Pipe2Y = 10
LadderX = 1200
LadderY = -2
sgX = 123456
sgY = 10




rect = sprite_sheet_image.get_rect()
rect.center = (x, y)
CoinRect = Coin.get_rect()
CoinRect.center = (COINMOVEX, COINMOVEY)
BLACK = (0, 0, 0)

#Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 50)
textX = 10
textY = 10

def show_score (textX, textY):
	score = font.render("Score : " + str(score_value),True, (255, 255, 255))
	screen.blit(score, (textX, textY))

bg = pygame.image.load('sewer_background.jpg').convert()
bg_width = bg.get_width()

#define game variables
scroll = 0
dif = 4
tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1
print(tiles)

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

		clock.tick(FPS)
		
		#scroll background + speeds scroll
		scroll -= dif
		current_time = pygame.time.get_ticks()
		if current_time % 5000 < 10:
			dif += 1
			print('Speed up by', dif,)

		#reset scroll
		if abs(scroll) > bg_width:
			scroll = 0

		#Makes the Coin Move
		COINMOVEX -= dif
		MeatX -= dif
		TunnelX -= dif
		Pipe1X -= dif
		Pipe2X -= dif
		LadderX -= dif
		sgX -= dif


		#update animation
		current_time = pygame.time.get_ticks()
		if current_time - last_update >= animation_cooldown:
			frame += 1
			last_update = current_time
			if frame >= len(animation_list[action]):
				frame = 0

		#If the coin reaches the edge of the screen then randomly choose a new lane to respawn
		if COINMOVEX <= -100:
			CoinSpot = random.randint(1, 3)
			if CoinSpot == 1:
				COINMOVEX = 1800
				COINMOVEY = 250
			if CoinSpot == 2:
				COINMOVEX = 1800
				COINMOVEY = 400
			if CoinSpot == 3:
				COINMOVEX = 1800
				COINMOVEY = 520

		#Choosing a New Tunnel
		if TunnelX <= -500:
			BackgroundStuff = random.randint(1, 5)
			if BackgroundStuff == 1:
				TunnelX = 10000
			if BackgroundStuff == 2:
				TunnelX = 3000
			if BackgroundStuff == 3:
				TunnelX = 8000
			if BackgroundStuff == 4:
				TunnelX = 20000
			if BackgroundStuff == 5:
				TunnelX = 69420

		if Pipe1X <= -1000:
			BackgroundStuff = random.randint(1, 5)
			if BackgroundStuff == 1:
				Pipe1X = 1800
			if BackgroundStuff == 2:
				Pipe1X = 5050
			if BackgroundStuff == 3:
				Pipe1X = 9100
			if BackgroundStuff == 4:
				Pipe1X = 20000
			if BackgroundStuff == 5:
				Pipe1X = 42069

		if Pipe2X <= -1000:
			Pipe2Stuff = random.randint(1, 5)
			if Pipe2Stuff == 1:
				Pipe2X = 2100
			if Pipe2Stuff == 2:
				Pipe2X = 5950
			if Pipe2Stuff == 3:
				Pipe2X = 7300
			if Pipe2Stuff == 4:
				Pipe2X = 10000
			if Pipe2Stuff == 5:
				Pipe2X = 3500

		if LadderX <= -950:
			LadderRandom = random.randint(1, 6)
			if LadderRandom == 1:
				LadderX = 2522
			if LadderRandom == 2:
				LadderX = 5050
			if LadderRandom == 3:
				LadderX = 3500
			if LadderRandom == 4:
				LadderX = 9000
			if LadderRandom == 5:
				LadderX = 2069
			if LadderRandom == 6:
				LadderX = 10000
		
		if sgX <= -1000:
			EasterEgg = random.randint(1, 3)
			if EasterEgg == 1:
				sgX = 123456
			if EasterEgg == 2:
				sgX = 654321
			if EasterEgg == 3:
				sgX = 696969

		#If Crockettdile and Coin are in the same lane then randomly choose another lane to spawn in
		if COINMOVEX <= 400 and y == 170 and COINMOVEY == 250:
			score_value += 5
			CoinSpot = random.randint(1, 3)
			if CoinSpot == 1:
				COINMOVEX = 1800
				COINMOVEY = 250
			if CoinSpot == 2:
				COINMOVEX = 1800
				COINMOVEY = 400
			if CoinSpot == 3:
				COINMOVEX = 1800
				COINMOVEY = 520
		if COINMOVEX <= 400 and y == 300 and COINMOVEY == 400:
			score_value += 5
			CoinSpot = random.randint(1, 3)
			if CoinSpot == 1:
				COINMOVEX = 1800
				COINMOVEY = 250
			if CoinSpot == 2:
				COINMOVEX = 1800
				COINMOVEY = 400
			if CoinSpot == 3:
				COINMOVEX = 1800
				COINMOVEY = 520
		if COINMOVEX <= 400 and y == 430 and COINMOVEY == 520:
			score_value += 5
			print(score_value)
			CoinSpot = random.randint(1, 3)
			if CoinSpot == 1:
				COINMOVEX = 1800
				COINMOVEY = 250
			if CoinSpot == 2:
				COINMOVEX = 1800
				COINMOVEY = 400
			if CoinSpot == 3:
				COINMOVEX = 1800
				COINMOVEY = 520

		#If Crockettdile is trying to go past the top or bottom lane then stay in the same lane as it is
		if y <= 170:
			y = 170
		if y >= 430:
			y = 430

		#If Crockettdile is trying get between two lanes then just dont let him
		if y == 235:
			y = 300 or 170
		if y == 365:
			y = 300 or 430

		#show frame image
		for i in range(0, tiles):
			screen.blit(bg, (i * bg_width + scroll, 0))
		screen.blit(SeanGraffiti, (sgX, sgY))
		screen.blit(SewerTunnel, (TunnelX, TunnelY))
		screen.blit(SewerLadder, (LadderX, LadderY))
		screen.blit(SewerPipe2, (Pipe2X, Pipe2Y))
		screen.blit(SewerPipe, (Pipe1X, Pipe1Y))
		screen.blit(Trash2, (Trash2X, Trash2Y))
		screen.blit(Trash1, (Trash1X, Trash1Y))
		screen.blit(Coin, (COINMOVEX, COINMOVEY))
		screen.blit(Meat, (MeatX, MeatY))
		screen.blit(animation_list[action][frame], (x, y))



		#event handler and Crockettdile Movement
		for event in pygame.event.get():
			keys = pygame.key.get_pressed()
			if keys[pygame.K_w]:
				action = 1
				y -= 65
			if keys[pygame.K_s]:
				action = 1
				y += 65
			if keys[pygame.K_SPACE]:
				action = 2
			if event.type == pygame.QUIT:
				run = False
					
		show_score(textX, textY)
		pygame.display.update()

pygame.quit()
