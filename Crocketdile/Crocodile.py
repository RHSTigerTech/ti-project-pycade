import pygame, random, math, os
import Crocodile2
from pygame import mixer

pygame.init()


#redirects file finder to folder
os.chdir('Crocketdile_images')

SCREEN_WIDTH = 1530
SCREEN_HEIGHT = 756

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('Crockettdile')


sprite_sheet_image = pygame.image.load('CrocodileSpritesheetMini.png').convert_alpha()
sprite_sheet = Crocodile2.SpriteSheet(sprite_sheet_image)
Coin = pygame.image.load("Coin.png").convert_alpha()
Meat = pygame.image.load("Meat.png").convert_alpha()
Trash1 = pygame.image.load("Trash1.png").convert_alpha()
Trash2 = pygame.image.load("Trash2.png").convert_alpha()
SewerTunnel = pygame.image.load("sewerTunnel.png").convert_alpha()
SewerPipe = pygame.image.load("sewerPipe.png").convert_alpha()
SewerPipe2 = pygame.image.load("sewerPipe2.png").convert_alpha()
SewerLadder = pygame.image.load("sewerLadder.png").convert_alpha()
SeanGraffiti = pygame.image.load("seanGraffiti.png").convert_alpha()
HalfaCar = pygame.image.load("halfAcar.png").convert_alpha()
FrontBarrels = pygame.image.load("frontBarrel.png").convert_alpha()
GoWeegyGo = pygame.image.load("Wedgysavehim.png").convert_alpha()
Heart = pygame.image.load("heart.png").convert_alpha()
Barba = pygame.image.load("barberCoin_400size.png").convert_alpha()
GameOverScreeny = pygame.image.load("gameOver_screen.jpg").convert_alpha()
DontEatHim = pygame.image.load("DontEatGoWeegy.png").convert_alpha()
EndofBackStuff = pygame.image.load("EndofBackStuff.png").convert_alpha()
RottenMeat = pygame.image.load("RottenMeat.png").convert_alpha()
CloseMouth = pygame.image.load("CloseMouth.png").convert_alpha()
TipsScreenImage = pygame.image.load("UpdatedTipsScreen.jpg").convert_alpha()
ClosePipe = pygame.image.load("CloseUpPipe.png").convert_alpha()


clock = pygame.time.Clock()
FPS = 60

current_time = 0
button_press_time = 0

x = 0
y = 300
COINMOVEY = 401
COINMOVEX = -1800
MeatX = 1000
MeatY = 900
Trash1X = 1000
Trash1Y = -2000
Trash2X = 1000
Trash2Y = -305
CoinSpot = random.randint(1, 3)
TunnelX = 3800
TunnelY = -9999
Pipe1X = 10
Pipe1Y = -9999
Pipe2X = 10000
Pipe2Y = -9999
LadderX = 1200
LadderY = -9999
sgX = 123456
sgY = 10
CarX = 100
CarY = 80200
WedgyX = 1500
WedgyY = -666
HeartX = -100
HeartY = -40
BarbaX = 99999999
BarbaY = -510
GameOverX = -999990
GameOverY = -999990
BarrelX = -1000
BarrelY = 120
DontEatX = 9000
DontEatY = -666
EndX = -499
EndY = 10
RottenMeatX = 10
RottenMeatY = -200
CloseMouthX = 10
CloseMouthY = -500
TipsScreenX = 0
TipsScreenY = 0
GameOverRetry = False
GameStart = False
TipScreenPart = True
ClosePipeX = -3500
ClosePipeY = 0


rect = sprite_sheet_image.get_rect()
rect.center = (x, y)
CoinRect = Coin.get_rect()
CoinRect.center = (COINMOVEX, COINMOVEY)
BLACK = (0, 0, 0)
health_value = 3
cooldown = False
is_eating = False

#Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 50)
textX = 10
textXX = 110
textY = 10000
textYY = 10000


def show_score (textX, textY):
	score = font.render("Score : " + str(score_value),True, (255, 255, 255))
	screen.blit(score, (textX, textY))

def show_health (textXX, textYY):
	Health = font.render(str(health_value),True, (255, 0, 0))
	screen.blit(Health, (textXX, textYY))

bg = pygame.image.load('sewer_background.jpg').convert()
bg_width = bg.get_width()

#define game variables
scroll = 0
dif = 4
tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1
print(tiles)
max_slow_down = 200
slow_down_time = max_slow_down

#create animation list
animation_list = []
animation_steps = [3, 3, 3, 3, 3, 3]
action = 1
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

def slow_down(slow):
	if slow > 0:
		slow -= 1
		return slow
	else:
		return slow


screen.blit(TipsScreenImage, (TipsScreenX, TipsScreenY))
pygame.display.update()
tips = True
while tips == True:
	for event in pygame.event.get():
		keys = pygame.key.get_pressed()
		if keys[pygame.K_RETURN]:
			run = True
			tips = False
# run = True
action = 1
health_value = 3
score_value = 0
bg = pygame.image.load('sewer_background.jpg').convert()
GameOverRetry = False
dif = 4
TipsScreenX = -999990
TipsScreenY = -999990
y = 300
CarX = -499
CarY = -500
EndX = -499
EndY = 10
textX = 10
textXX = 110
textY = 10
textYY = 80
HeartX = -100
HeartY = -40





while run:

		# pygame.time.delay(20)

		clock.tick(FPS)

		#print(COINMOVEX)
		
		#scroll background + speeds scroll
		scroll -= dif
		current_time = pygame.time.get_ticks()
		if current_time % 5000 < 10:
			dif += 1
			#print('Speed up by', dif,)

		#reset scroll
		if abs(scroll) > bg_width:
			scroll = 0

		if TipsScreenX == 0 and TipsScreenY == 0:
			StartScreenPart = True
			dif = 0
			scroll = 0
			bg = pygame.image.load('Black.jpg').convert()

		#Makes the Coins, Background so then it respawns and moves the the background again so its not plain and boring and Obstacles Move
		COINMOVEX -= dif
		MeatX -= dif
		TunnelX -= dif
		Pipe1X -= dif
		Pipe2X -= dif
		LadderX -= dif
		sgX -= dif
		CarX -= dif
		Trash1X -= dif
		Trash2X -= dif
		WedgyX -= dif
		DontEatX -= dif
		EndX -= dif
		RottenMeatX -= dif
		BarrelX -= dif
		BarbaX -= dif
		CloseMouthX -= dif
		ClosePipeX -= dif


		#update animation
		current_time = pygame.time.get_ticks()
		if current_time - last_update >= animation_cooldown:
			frame += 1
			last_update = current_time
			if frame >= len(animation_list[action]):
				frame = 0

		#If the coin reaches the edge of the screen then move above the screen away from the players views
		if COINMOVEX <= -200:
			COINMOVEY = -200
		
		
		if CarX <= -250:
			NewCar = random.randint(1, 72)
			if NewCar == 1:
				CarX = 5500
				CarY = 200
				MeatX = 1800
				MeatY = 310
				Trash1X = 3000
				Trash1Y = 460
				Trash2X = 4444
				Trash2Y = 328
				WedgyX = 2800
				WedgyY = 186
				NewCoin = random.randint(1, 11)
				if NewCoin == 1:
					COINMOVEX = 2252
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 2252
					COINMOVEY = 400
				if NewCoin == 3:
					COINMOVEX = 2252
					COINMOVEY = 520
				if NewCoin == 4:
					COINMOVEX = 3633
					COINMOVEY = 520
				if NewCoin == 5:
					COINMOVEX = 3633
					COINMOVEY = 250
				if NewCoin == 6:
					COINMOVEX = 3633
					COINMOVEY = 400
				if NewCoin == 7:
					COINMOVEX = 5000
					COINMOVEY = 520
				if NewCoin == 8:
					COINMOVEX = 5000
					COINMOVEY = 250
				if NewCoin == 9:
					COINMOVEX = 5000
					COINMOVEY = 400
				if NewCoin == 10:
					COINMOVEX = 5600
					COINMOVEY = 520
				if NewCoin == 11:
					COINMOVEX = 5600
					COINMOVEY = 400
			if NewCar == 2:
				CarX = 4000
				CarY = 330
				MeatX = 3000
				MeatY = 580
				WedgyX = 1700
				WedgyY = 320
				NewCoin = random.randint(1, 8)
				if NewCoin == 1:
					COINMOVEX = 2252
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 2252
					COINMOVEY = 400
				if NewCoin == 3:
					COINMOVEX = 2252
					COINMOVEY = 520
				if NewCoin == 4:
					COINMOVEX = 3000
					COINMOVEY = 250
				if NewCoin == 5:
					COINMOVEX = 3000
					COINMOVEY = 400
				if NewCoin == 6:
					COINMOVEX = 3800
					COINMOVEY = 250
				if NewCoin == 7:
					COINMOVEX = 3800
					COINMOVEY = 400
				if NewCoin == 8:
					COINMOVEX = 3800
					COINMOVEY = 520
			if NewCar == 3:
				CarX = 2000
				CarY = 460
				NewCoin = random.randint(1, 3)
				if NewCoin == 1:
					COINMOVEX = 2000
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 2000
					COINMOVEY = 400
				if NewCoin == 3:
					COINMOVEX = 1900
					COINMOVEY = 520
			if NewCar == 4:
				CarX = 2200
				CarY = 200
				Trash1X = 2200
				Trash1Y = 460
				NewCoin = random.randint(1, 3)
				if NewCoin == 1:
					COINMOVEX = 2100
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 2100
					COINMOVEY = 400
				if NewCoin == 3:
					COINMOVEX = 2050
					COINMOVEY = 520
			if NewCar == 5:
				CarX = 4000
				CarY = 460
				Trash2X = 2200
				Trash2Y = 328
				NewCoin = random.randint(1, 9)
				if NewCoin == 1:
					COINMOVEX = 2000
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 2000
					COINMOVEY = 400
				if NewCoin == 3:
					COINMOVEX = 2000
					COINMOVEY = 520
				if NewCoin == 4:
					COINMOVEX = 3333
					COINMOVEY = 250
				if NewCoin == 5:
					COINMOVEX = 3333
					COINMOVEY = 400
				if NewCoin == 6:
					COINMOVEX = 3333
					COINMOVEY = 520
				if NewCoin == 7:
					COINMOVEX = 3933
					COINMOVEY = 250
				if NewCoin == 8:
					COINMOVEX = 3933
					COINMOVEY = 400
				if NewCoin == 9:
					COINMOVEX = 3933
					COINMOVEY = 520
			if NewCar == 6:
				CarX = 3500
				CarY = 460
				Trash2X = 2500
				Trash2Y = 328
				MeatX = 2000
				MeatY = 444
				NewCoin = random.randint(1, 6)
				if NewCoin == 1:
					COINMOVEX = 2000
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 2000
					COINMOVEY = 520
				if NewCoin == 3:
					COINMOVEX = 2300
					COINMOVEY = 400
				if NewCoin == 4:
					COINMOVEX = 3100
					COINMOVEY = 250
				if NewCoin == 5:
					COINMOVEX = 3100
					COINMOVEY = 400
				if NewCoin == 6:
					COINMOVEX = 3100
					COINMOVEY = 520
			if NewCar == 7:
				CarX = 3000
				CarY = 330
				Trash1X = 2000
				Trash1Y = 200
				Trash2X = 2000
				Trash2Y = 328
				NewCoin = random.randint(1, 4)
				if NewCoin == 1:
					COINMOVEX = 2900
					COINMOVEY = 520
				if NewCoin == 2:
					COINMOVEX = 2900
					COINMOVEY = 400
				if NewCoin == 3:
					COINMOVEX = 2900
					COINMOVEY = 250
				if NewCoin == 4:
					COINMOVEX = 2300
					COINMOVEY = 520
			if NewCar == 8:
				CarX = 3000
				CarY = 330
				Trash1X = 2000
				Trash1Y = 460
				Trash2X = 2000
				Trash2Y = 195
				NewCoin = random.randint(1, 2)
				if NewCoin == 1:
					COINMOVEX = 2500
					COINMOVEY = 400
				if NewCoin == 2:
					COINMOVEX = 2900
					COINMOVEY = 400
			if NewCar == 9:
				CarX = 2100
				CarY = -1000
				Trash1X = 2000
				Trash1Y = 460
				Trash2X = 2000
				Trash2Y = 195
				WedgyX = 1700
				WedgyY = 444
				NewCoin = random.randint(1, 2)
				if NewCoin == 1:
					COINMOVEX = 1900
					COINMOVEY = 400
				if NewCoin == 2:
					COINMOVEX = 1800
					COINMOVEY = 250
			if NewCar == 10:
				CarX = 2200
				CarY = -1000
				Trash1X = 2100
				Trash1Y = 200
				Trash2X = 2100
				Trash2Y = 430
				NewCoin = random.randint(1, 3)
				if NewCoin == 1:
					COINMOVEX = 1900
					COINMOVEY = 400
				if NewCoin == 2:
					COINMOVEX = 1900
					COINMOVEY = 250
				if NewCoin == 3:
					COINMOVEX = 1900
					COINMOVEY = 400
			if NewCar == 11:
				Trash1X = 1900
				Trash1Y = 200
				CarX = 2000
				CarY = 2000
				NewCoin = random.randint(1, 2)
				if NewCoin == 1:
					COINMOVEX = 1900
					COINMOVEY = 400
				if NewCoin == 2:
					COINMOVEX = 1900
					COINMOVEY = 520
			if NewCar == 12:
				Trash1X = 1900
				Trash1Y = 340
				CarX = 2000
				CarY = 2000
				NewCoin = random.randint(1, 2)
				if NewCoin == 1:
					COINMOVEX = 1900
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 1900
					COINMOVEY = 520
			if NewCar == 13:
				Trash1X = 1900
				Trash1Y = 460
				CarX = 2000
				CarY = 2000
				NewCoin = random.randint(1, 2)
				if NewCoin == 1:
					COINMOVEX = 1900
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 1900
					COINMOVEY = 400
			if NewCar == 14:
				Trash2X = 1900
				Trash2Y = 195
				CarX = 2000
				CarY = 2000
				NewCoin = random.randint(1, 2)
				if NewCoin == 1:
					COINMOVEX = 2000
					COINMOVEY = 520
				if NewCoin == 2:
					COINMOVEX = 2000
					COINMOVEY = 400
			if NewCar == 15:
				Trash2X = 1900
				Trash2Y = 328
				CarX = 2000
				CarY = 2000
				NewCoin = random.randint(1, 2)
				if NewCoin == 1:
					COINMOVEX = 2000
					COINMOVEY = 520
				if NewCoin == 2:
					COINMOVEX = 2000
					COINMOVEY = 250
			if NewCar == 16:
				Trash2X = 1900
				Trash2Y = 430
				CarX = 2000
				CarY = 2000
				NewCoin = random.randint(1, 2)
				if NewCoin == 1:
					COINMOVEX = 1950
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 1950
					COINMOVEY = 400
			if NewCar == 17:
				CarX = 2100
				CarY = -1000
				Trash1X = 2000
				Trash1Y = 460
				Trash2X = 2000
				Trash2Y = 195
				MeatX = 1800
				MeatY = 444
				NewCoin = random.randint(1, 3)
				if NewCoin == 1:
					COINMOVEX = 1820
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 1820
					COINMOVEY = 520
				if NewCoin == 3:
					COINMOVEX = 2050
					COINMOVEY = 400
			if NewCar == 18:
				CarX = 2300
				CarY = -1000
				Trash1X = 2200
				Trash1Y = 340
				Trash2X = 1900
				Trash2Y = 430
				NewCoin = random.randint(1, 4)
				if NewCoin == 1:
					COINMOVEX = 2000
					COINMOVEY = 400
				if NewCoin == 2:
					COINMOVEX = 2000
					COINMOVEY = 250
				if NewCoin == 3:
					COINMOVEX = 2250
					COINMOVEY = 250
				if NewCoin == 4:
					COINMOVEX = 2400
					COINMOVEY = 250
			if NewCar == 19:
				CarX = 5500
				CarY = 200
				MeatX = 1800
				MeatY = 310
				Trash1X = 3000
				Trash1Y = 460
				Trash2X = 4444
				Trash2Y = 328
				NewCoin = random.randint(1, 22)
				if NewCoin == 1:
					COINMOVEX = 1830
					COINMOVEY = 400
				if NewCoin == 2:
					COINMOVEX = 1830
					COINMOVEY = 520
				if NewCoin == 3:
					COINMOVEX = 2400
					COINMOVEY = 250
				if NewCoin == 4:
					COINMOVEX = 2400
					COINMOVEY = 400
				if NewCoin == 5:
					COINMOVEX = 2400
					COINMOVEY = 520
				if NewCoin == 6:
					COINMOVEX = 2850
					COINMOVEY = 250
				if NewCoin == 7:
					COINMOVEX = 2850
					COINMOVEY = 400
				if NewCoin == 8:
					COINMOVEX = 2850
					COINMOVEY = 520
				if NewCoin == 9:
					COINMOVEX = 3050
					COINMOVEY = 250
				if NewCoin == 10:
					COINMOVEX = 3050
					COINMOVEY = 400
				if NewCoin == 11:
					COINMOVEX = 3700
					COINMOVEY = 250
				if NewCoin == 12:
					COINMOVEX = 3700
					COINMOVEY = 400
				if NewCoin == 13:
					COINMOVEX = 3700
					COINMOVEY = 520
				if NewCoin == 14:
					COINMOVEX = 4344
					COINMOVEY = 250
				if NewCoin == 15:
					COINMOVEX = 4344
					COINMOVEY = 400
				if NewCoin == 16:
					COINMOVEX = 4344
					COINMOVEY = 520
				if NewCoin == 17:
					COINMOVEX = 5074
					COINMOVEY = 250
				if NewCoin == 18:
					COINMOVEX = 5074
					COINMOVEY = 400
				if NewCoin == 19:
					COINMOVEX = 5074
					COINMOVEY = 520
				if NewCoin == 20:
					COINMOVEX = 5400
					COINMOVEY = 250
				if NewCoin == 21:
					COINMOVEX = 5400
					COINMOVEY = 400
				if NewCoin == 22:
					COINMOVEX = 5400
					COINMOVEY = 520
			if NewCar == 20:
				CarX = 3000
				CarY = 330
				MeatX = 2000
				MeatY = 580
				NewCoin = random.randint(1, 10)
				if NewCoin == 1:
					COINMOVEX = 2020
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 2020
					COINMOVEY = 400
				if NewCoin == 3:
					COINMOVEX = 2600
					COINMOVEY = 250
				if NewCoin == 4:
					COINMOVEX = 2600
					COINMOVEY = 400
				if NewCoin == 5:
					COINMOVEX = 2600
					COINMOVEY = 520
				if NewCoin == 6:
					COINMOVEX = 2900
					COINMOVEY = 250
				if NewCoin == 7:
					COINMOVEX = 2900
					COINMOVEY = 400
				if NewCoin == 8:
					COINMOVEX = 2900
					COINMOVEY = 520
				if NewCoin == 9:
					COINMOVEX = 3100
					COINMOVEY = 250
				if NewCoin == 10:
					COINMOVEX = 3100
					COINMOVEY = 520
			if NewCar == 21:
				CarX = 5500
				CarY = 200
				RottenMeatX = 1800
				RottenMeatY = 310
				Trash1X = 3000
				Trash1Y = 460
				Trash2X = 4444
				Trash2Y = 328
				NewCoin = random.randint(1, 22)
				if NewCoin == 1:
					COINMOVEX = 1830
					COINMOVEY = 400
				if NewCoin == 2:
					COINMOVEX = 1830
					COINMOVEY = 520
				if NewCoin == 3:
					COINMOVEX = 2400
					COINMOVEY = 250
				if NewCoin == 4:
					COINMOVEX = 2400
					COINMOVEY = 400
				if NewCoin == 5:
					COINMOVEX = 2400
					COINMOVEY = 520
				if NewCoin == 6:
					COINMOVEX = 2850
					COINMOVEY = 250
				if NewCoin == 7:
					COINMOVEX = 2850
					COINMOVEY = 400
				if NewCoin == 8:
					COINMOVEX = 2850
					COINMOVEY = 520
				if NewCoin == 9:
					COINMOVEX = 3050
					COINMOVEY = 250
				if NewCoin == 10:
					COINMOVEX = 3050
					COINMOVEY = 400
				if NewCoin == 11:
					COINMOVEX = 3700
					COINMOVEY = 250
				if NewCoin == 12:
					COINMOVEX = 3700
					COINMOVEY = 400
				if NewCoin == 13:
					COINMOVEX = 3700
					COINMOVEY = 520
				if NewCoin == 14:
					COINMOVEX = 4344
					COINMOVEY = 250
				if NewCoin == 15:
					COINMOVEX = 4344
					COINMOVEY = 400
				if NewCoin == 16:
					COINMOVEX = 4344
					COINMOVEY = 520
				if NewCoin == 17:
					COINMOVEX = 5074
					COINMOVEY = 250
				if NewCoin == 18:
					COINMOVEX = 5074
					COINMOVEY = 400
				if NewCoin == 19:
					COINMOVEX = 5074
					COINMOVEY = 520
				if NewCoin == 20:
					COINMOVEX = 5400
					COINMOVEY = 250
				if NewCoin == 21:
					COINMOVEX = 5400
					COINMOVEY = 400
				if NewCoin == 22:
					COINMOVEX = 5400
					COINMOVEY = 520
			if NewCar == 22:
				CarX = 3000
				CarY = 330
				RottenMeatX = 2000
				RottenMeatY = 580
				NewCoin = random.randint(1, 10)
				if NewCoin == 1:
					COINMOVEX = 2020
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 2020
					COINMOVEY = 400
				if NewCoin == 3:
					COINMOVEX = 2600
					COINMOVEY = 250
				if NewCoin == 4:
					COINMOVEX = 2600
					COINMOVEY = 400
				if NewCoin == 5:
					COINMOVEX = 2600
					COINMOVEY = 520
				if NewCoin == 6:
					COINMOVEX = 2900
					COINMOVEY = 250
				if NewCoin == 7:
					COINMOVEX = 2900
					COINMOVEY = 400
				if NewCoin == 8:
					COINMOVEX = 2900
					COINMOVEY = 520
				if NewCoin == 9:
					COINMOVEX = 3100
					COINMOVEY = 250
				if NewCoin == 10:
					COINMOVEX = 3100
					COINMOVEY = 520
			if NewCar == 23:
				CarX = 2300
				CarY = -500
				Trash1X = 1900
				Trash1Y = 200
				MeatX = 2100
				MeatY = 444
				RottenMeatX = 2300
				RottenMeatY = 580
				NewCoin = random.randint(1, 4)
				if NewCoin == 1:
					COINMOVEX = 1950
					COINMOVEY = 400
				if NewCoin == 2:
					COINMOVEX = 2150
					COINMOVEY = 520
				if NewCoin == 3:
					COINMOVEX = 2200
					COINMOVEY = 250
				if NewCoin == 4:
					COINMOVEX = 2330
					COINMOVEY = 400
			if NewCar == 24:
				CarX = 2300
				CarY = -500
				Trash1X = 1900
				Trash1Y = 200
				MeatX = 2300
				MeatY = 580
				RottenMeatX = 2100
				RottenMeatY = 444
				NewCoin = random.randint(1, 4)
				if NewCoin == 1:
					COINMOVEX = 1950
					COINMOVEY = 400
				if NewCoin == 2:
					COINMOVEX = 2150
					COINMOVEY = 520
				if NewCoin == 3:
					COINMOVEX = 2200
					COINMOVEY = 250
				if NewCoin == 4:
					COINMOVEX = 2330
					COINMOVEY = 400
			if NewCar == 25:
				CarX = 2100
				CarY = -500
				RottenMeatX = 1900
				RottenMeatY = 310
				MeatX = 1900
				MeatY = 580
				NewCoin = random.randint(1, 4)
				if NewCoin == 1:
					COINMOVEX = 1950
					COINMOVEY = 400
				if NewCoin == 2:
					COINMOVEX = 2100
					COINMOVEY = 250
				if NewCoin == 3:
					COINMOVEX = 2100
					COINMOVEY = 400
				if NewCoin == 4:
					COINMOVEX = 2100
					COINMOVEY = 520
			if NewCar == 26:
				CarX = 2100
				CarY = 330
				RottenMeatX = 1900
				RottenMeatY = 310
				MeatX = 1900
				MeatY = 580
				NewCoin = random.randint(1, 4)
				if NewCoin == 1:
					COINMOVEX = 1950
					COINMOVEY = 400
				if NewCoin == 2:
					COINMOVEX = 2100
					COINMOVEY = 250
				if NewCoin == 3:
					COINMOVEX = 2100
					COINMOVEY = 520
				if NewCoin == 4:
					COINMOVEX = 1950
					COINMOVEY = 400
			if NewCar == 27:
				CarX = 2100
				CarY = 460
				RottenMeatX = 1900
				RottenMeatY = 310
				MeatX = 1900
				MeatY = 580
				NewCoin = random.randint(1, 4)
				if NewCoin == 1:
					COINMOVEX = 1950
					COINMOVEY = 400
				if NewCoin == 2:
					COINMOVEX = 2100
					COINMOVEY = 250
				if NewCoin == 3:
					COINMOVEX = 2200
					COINMOVEY = 400
				if NewCoin == 4:
					COINMOVEX = 2200
					COINMOVEY = 250
			if NewCar == 28:
				CarX = 2100
				CarY = -500
				RottenMeatX = 1900
				RottenMeatY = 580
				MeatX = 1900
				MeatY = 310
				NewCoin = random.randint(1, 4)
				if NewCoin == 1:
					COINMOVEX = 1950
					COINMOVEY = 400
				if NewCoin == 2:
					COINMOVEX = 2100
					COINMOVEY = 250
				if NewCoin == 3:
					COINMOVEX = 2100
					COINMOVEY = 400
				if NewCoin == 4:
					COINMOVEX = 2100
					COINMOVEY = 520
			if NewCar == 29:
				CarX = 2100
				CarY = 330
				RottenMeatX = 1900
				RottenMeatY = 580
				MeatX = 1900
				MeatY = 310
				NewCoin = random.randint(1, 4)
				if NewCoin == 1:
					COINMOVEX = 1950
					COINMOVEY = 400
				if NewCoin == 2:
					COINMOVEX = 2100
					COINMOVEY = 250
				if NewCoin == 3:
					COINMOVEX = 2100
					COINMOVEY = 520
				if NewCoin == 4:
					COINMOVEX = 1950
					COINMOVEY = 400
			if NewCar == 30:
				CarX = 2100
				CarY = 460
				RottenMeatX = 1900
				RottenMeatY = 580
				MeatX = 1900
				MeatY = 310
				NewCoin = random.randint(1, 4)
				if NewCoin == 1:
					COINMOVEX = 1950
					COINMOVEY = 400
				if NewCoin == 2:
					COINMOVEX = 2100
					COINMOVEY = 250
				if NewCoin == 3:
					COINMOVEX = 2200
					COINMOVEY = 400
				if NewCoin == 4:
					COINMOVEX = 2200
					COINMOVEY = 250
			if NewCar == 31:
				CarX = 2100
				CarY = -500
				RottenMeatX = 1900
				RottenMeatY = 580
				NewCoin = random.randint(1, 2)
				if NewCoin == 1:
					COINMOVEX = 1920
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 1920
					COINMOVEY = 400
			if NewCar == 32:
				CarX = 2100
				CarY = 330
				RottenMeatX = 1900
				RottenMeatY = 580
				NewCoin = random.randint(1, 4)
				if NewCoin == 1:
					COINMOVEX = 1920
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 1920
					COINMOVEY = 400
				if NewCoin == 3:
					COINMOVEX = 2180
					COINMOVEY = 250
				if NewCoin == 4:
					COINMOVEX = 2180
					COINMOVEY = 520
			if NewCar == 33:
				CarX = 2100
				CarY = 460
				RottenMeatX = 1900
				RottenMeatY = 580
				NewCoin = random.randint(1, 4)
				if NewCoin == 1:
					COINMOVEX = 1920
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 1920
					COINMOVEY = 400
				if NewCoin == 3:
					COINMOVEX = 2150
					COINMOVEY = 250
				if NewCoin == 4:
					COINMOVEX = 2150
					COINMOVEY = 400
			if NewCar == 34:
				CarX = 2100
				CarY = -500
				RottenMeatX = 1900
				RottenMeatY = 310
				NewCoin = random.randint(1, 2)
				if NewCoin == 1:
					COINMOVEX = 1920
					COINMOVEY = 520
				if NewCoin == 2:
					COINMOVEX = 1920
					COINMOVEY = 400
			if NewCar == 35:
				CarX = 2100
				CarY = -500
				RottenMeatX = 1900
				RottenMeatY = 444
				NewCoin = random.randint(1, 2)
				if NewCoin == 1:
					COINMOVEX = 1920
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 1920
					COINMOVEY = 520
			if NewCar == 36:
				CarX = 2100
				CarY = -500
				Trash1X = 1900
				Trash1Y = 200
				RottenMeatX = 1900
				RottenMeatY = 444
				Trash2X = 1900
				Trash2Y = 430
			if NewCar == 37:
				CarX = 2300
				CarY = -1000
				Trash1X = 2100
				Trash1Y = 460
				Trash2X = 2100
				Trash2Y = 195
				MeatX = 1800
				MeatY = 444
				RottenMeatX = 2300
				RottenMeatY = 444
				NewCoin = random.randint(1, 4)
				if NewCoin == 1:
					COINMOVEX = 1820
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 1820
					COINMOVEY = 520
				if NewCoin == 3:
					COINMOVEX = 2420
					COINMOVEY = 250
				if NewCoin == 4:
					COINMOVEX = 2420
					COINMOVEY = 520
			if NewCar == 38:
				CarX = 4200
				CarY = 330
				Trash1X = 2700
				Trash1Y = 340
				Trash2X = 1900
				Trash2Y = 430
				NewCoin = random.randint(1, 17)
				if NewCoin == 1:
					COINMOVEX = 1800
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 1800
					COINMOVEY = 400
				if NewCoin == 3:
					COINMOVEX = 1800
					COINMOVEY = 520
				if NewCoin == 4:
					COINMOVEX = 2550
					COINMOVEY = 250
				if NewCoin == 5:
					COINMOVEX = 2550
					COINMOVEY = 400
				if NewCoin == 6:
					COINMOVEX = 2550
					COINMOVEY = 520
				if NewCoin == 7:
					COINMOVEX = 3050
					COINMOVEY = 250
				if NewCoin == 8:
					COINMOVEX = 3050
					COINMOVEY = 400
				if NewCoin == 9:
					COINMOVEX = 3050
					COINMOVEY = 520
				if NewCoin == 10:
					COINMOVEX = 3550
					COINMOVEY = 250
				if NewCoin == 11:
					COINMOVEX = 3550
					COINMOVEY = 400
				if NewCoin == 12:
					COINMOVEX = 3550
					COINMOVEY = 520
				if NewCoin == 13:
					COINMOVEX = 4100
					COINMOVEY = 250
				if NewCoin == 14:
					COINMOVEX = 4100
					COINMOVEY = 400
				if NewCoin == 15:
					COINMOVEX = 4100
					COINMOVEY = 520
				if NewCoin == 16:
					COINMOVEX = 4300
					COINMOVEY = 250
				if NewCoin == 17:
					COINMOVEX = 4300
					COINMOVEY = 520
			if NewCar == 39:
				CarX = 4500
				CarY = 330
				Trash1X = 2700
				Trash1Y = 340
				Trash2X = 1900
				Trash2Y = 430
				RottenMeatX = 3653
				RottenMeatY = 310
				NewCoin = random.randint(11, 11)
				if NewCoin == 1:
					COINMOVEX = 1800
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 1800
					COINMOVEY = 400
				if NewCoin == 3:
					COINMOVEX = 1800
					COINMOVEY = 520
				if NewCoin == 4:
					COINMOVEX = 2550
					COINMOVEY = 250
				if NewCoin == 5:
					COINMOVEX = 2550
					COINMOVEY = 400
				if NewCoin == 6:
					COINMOVEX = 2550
					COINMOVEY = 520
				if NewCoin == 7:
					COINMOVEX = 3050
					COINMOVEY = 250
				if NewCoin == 8:
					COINMOVEX = 3050
					COINMOVEY = 400
				if NewCoin == 9:
					COINMOVEX = 3050
					COINMOVEY = 520
				if NewCoin == 10:
					COINMOVEX = 3500
					COINMOVEY = 250
				if NewCoin == 11:
					COINMOVEX = 3700
					COINMOVEY = 400
				if NewCoin == 12:
					COINMOVEX = 3700
					COINMOVEY = 520
				if NewCoin == 13:
					COINMOVEX = 4100
					COINMOVEY = 250
				if NewCoin == 14:
					COINMOVEX = 4100
					COINMOVEY = 400
				if NewCoin == 15:
					COINMOVEX = 4100
					COINMOVEY = 520
				if NewCoin == 16:
					COINMOVEX = 4300
					COINMOVEY = 250
				if NewCoin == 17:
					COINMOVEX = 4300
					COINMOVEY = 520
			if NewCar == 40:
				CarX = 3000
				CarY = 330
				Trash1X = 2700
				Trash1Y = 460
				Trash2X = 1900
				Trash2Y = 328
				NewCoin = random.randint(1, 7)
				if NewCoin == 1:
					COINMOVEX = 2000
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 2000
					COINMOVEY = 520
				if NewCoin == 3:
					COINMOVEX = 2500
					COINMOVEY = 250
				if NewCoin == 4:
					COINMOVEX = 2500
					COINMOVEY = 400
				if NewCoin == 5:
					COINMOVEX = 2500
					COINMOVEY = 520
				if NewCoin == 6:
					COINMOVEX = 2900
					COINMOVEY = 400
				if NewCoin == 7:
					COINMOVEX = 3050
					COINMOVEY = 250
			if NewCar == 41:
				CarX = 3000
				CarY = 460
				Trash1X = 1900
				Trash1Y = 340
				Trash2X = 2700
				Trash2Y = 195
				NewCoin = random.randint(1, 12)
				if NewCoin == 1:
					COINMOVEX = 1950
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 1950
					COINMOVEY = 520
				if NewCoin == 3:
					COINMOVEX = 2400
					COINMOVEY = 250
				if NewCoin == 4:
					COINMOVEX = 2400
					COINMOVEY = 400
				if NewCoin == 5:
					COINMOVEX = 2400
					COINMOVEY = 520
				if NewCoin == 6:
					COINMOVEX = 2600
					COINMOVEY = 250
				if NewCoin == 7:
					COINMOVEX = 2600
					COINMOVEY = 400
				if NewCoin == 8:
					COINMOVEX = 2600
					COINMOVEY = 520
				if NewCoin == 9:
					COINMOVEX = 2900
					COINMOVEY = 400
				if NewCoin == 10:
					COINMOVEX = 2900
					COINMOVEY = 520
				if NewCoin == 11:
					COINMOVEX = 3050
					COINMOVEY = 400
				if NewCoin == 12:
					COINMOVEX = 3100
					COINMOVEY = 250
			if NewCar == 42:
				CarX = 3000
				CarY = 330
				Trash1X = 2700
				Trash1Y = 460
				Trash2X = 1900
				Trash2Y = 328
				RottenMeatX = 2700
				RottenMeatY = 310
				NewCoin = random.randint(1, 7)
				if NewCoin == 1:
					COINMOVEX = 2000
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 2000
					COINMOVEY = 520
				if NewCoin == 3:
					COINMOVEX = 2500
					COINMOVEY = 250
				if NewCoin == 4:
					COINMOVEX = 2500
					COINMOVEY = 400
				if NewCoin == 5:
					COINMOVEX = 2500
					COINMOVEY = 520
				if NewCoin == 6:
					COINMOVEX = 2900
					COINMOVEY = 400
				if NewCoin == 7:
					COINMOVEX = 3050
					COINMOVEY = 250
			if NewCar == 43:
				CarX = 5000
				CarY = 460
				RottenMeatX = 1900
				RottenMeatY = 310
				WedgyX = 2522
				WedgyY = 320
				Trash1X = 3309
				Trash1Y = 200
				Trash2X = 4044
				Trash2Y = 328
				NewCoin = random.randint(1, 25)
				if NewCoin == 1:
					COINMOVEX = 1950
					COINMOVEY = 400
				if NewCoin == 2:
					COINMOVEX = 1950
					COINMOVEY = 520
				if NewCoin == 3:
					COINMOVEX = 2450
					COINMOVEY = 250
				if NewCoin == 4:
					COINMOVEX = 2450
					COINMOVEY = 400
				if NewCoin == 5:
					COINMOVEX = 2450
					COINMOVEY = 520
				if NewCoin == 6:
					COINMOVEX = 3000
					COINMOVEY = 250
				if NewCoin == 7:
					COINMOVEX = 3000
					COINMOVEY = 400
				if NewCoin == 8:
					COINMOVEX = 3000
					COINMOVEY = 520
				if NewCoin == 9:
					COINMOVEX = 3150
					COINMOVEY = 250
				if NewCoin == 10:
					COINMOVEX = 3150
					COINMOVEY = 400
				if NewCoin == 11:
					COINMOVEX = 3150
					COINMOVEY = 520
				if NewCoin == 12:
					COINMOVEX = 3350
					COINMOVEY = 400
				if NewCoin == 13:
					COINMOVEX = 3350
					COINMOVEY = 520
				if NewCoin == 14:
					COINMOVEX = 3750
					COINMOVEY = 250
				if NewCoin == 15:
					COINMOVEX = 3750
					COINMOVEY = 400
				if NewCoin == 16:
					COINMOVEX = 3750
					COINMOVEY = 520
				if NewCoin == 17:
					COINMOVEX = 3900
					COINMOVEY = 250
				if NewCoin == 18:
					COINMOVEX = 3900
					COINMOVEY = 400
				if NewCoin == 19:
					COINMOVEX = 3900
					COINMOVEY = 520
				if NewCoin == 20:
					COINMOVEX = 4600
					COINMOVEY = 250
				if NewCoin == 21:
					COINMOVEX = 4600
					COINMOVEY = 400
				if NewCoin == 22:
					COINMOVEX = 4600
					COINMOVEY = 520
				if NewCoin == 23:
					COINMOVEX = 4900
					COINMOVEY = 250
				if NewCoin == 24:
					COINMOVEX = 4900
					COINMOVEY = 400
				if NewCoin == 25:
					COINMOVEX = 4900
					COINMOVEY = 520
			if NewCar == 44:
				CarX = 5000
				CarY = 460
				RottenMeatX = 1900
				RottenMeatY = 310
				Trash1X = 3309
				Trash1Y = 200
				Trash2X = 4044
				Trash2Y = 328
				NewCoin = random.randint(1, 25)
				if NewCoin == 1:
					COINMOVEX = 1950
					COINMOVEY = 400
				if NewCoin == 2:
					COINMOVEX = 1950
					COINMOVEY = 520
				if NewCoin == 3:
					COINMOVEX = 2450
					COINMOVEY = 250
				if NewCoin == 4:
					COINMOVEX = 2450
					COINMOVEY = 400
				if NewCoin == 5:
					COINMOVEX = 2450
					COINMOVEY = 520
				if NewCoin == 6:
					COINMOVEX = 3000
					COINMOVEY = 250
				if NewCoin == 7:
					COINMOVEX = 3000
					COINMOVEY = 400
				if NewCoin == 8:
					COINMOVEX = 3000
					COINMOVEY = 520
				if NewCoin == 9:
					COINMOVEX = 3150
					COINMOVEY = 250
				if NewCoin == 10:
					COINMOVEX = 3150
					COINMOVEY = 400
				if NewCoin == 11:
					COINMOVEX = 3150
					COINMOVEY = 520
				if NewCoin == 12:
					COINMOVEX = 3350
					COINMOVEY = 400
				if NewCoin == 13:
					COINMOVEX = 3350
					COINMOVEY = 520
				if NewCoin == 14:
					COINMOVEX = 3750
					COINMOVEY = 250
				if NewCoin == 15:
					COINMOVEX = 3750
					COINMOVEY = 400
				if NewCoin == 16:
					COINMOVEX = 3750
					COINMOVEY = 520
				if NewCoin == 17:
					COINMOVEX = 3900
					COINMOVEY = 250
				if NewCoin == 18:
					COINMOVEX = 3900
					COINMOVEY = 400
				if NewCoin == 19:
					COINMOVEX = 3900
					COINMOVEY = 520
				if NewCoin == 20:
					COINMOVEX = 4600
					COINMOVEY = 250
				if NewCoin == 21:
					COINMOVEX = 4600
					COINMOVEY = 400
				if NewCoin == 22:
					COINMOVEX = 4600
					COINMOVEY = 520
				if NewCoin == 23:
					COINMOVEX = 4900
					COINMOVEY = 250
				if NewCoin == 24:
					COINMOVEX = 4900
					COINMOVEY = 400
				if NewCoin == 25:
					COINMOVEX = 4900
					COINMOVEY = 520
			if NewCar == 45:
				CarX = 3500
				CarY = 460
				RottenMeatX = 1900
				RottenMeatY = 310
				Trash1X = 2209
				Trash1Y = 460
				Trash2X = 3044
				Trash2Y = 328
				NewCoin = random.randint(1, 8)
				if NewCoin == 1:
					COINMOVEX = 1950
					COINMOVEY = 400
				if NewCoin == 2:
					COINMOVEX = 1950
					COINMOVEY = 520
				if NewCoin == 3:
					COINMOVEX = 2420
					COINMOVEY = 400
				if NewCoin == 4:
					COINMOVEX = 2520
					COINMOVEY = 520
				if NewCoin == 5:
					COINMOVEX = 2920
					COINMOVEY = 400
				if NewCoin == 6:
					COINMOVEX = 3200
					COINMOVEY = 250
				if NewCoin == 7:
					COINMOVEX = 3600
					COINMOVEY = 400
				if NewCoin == 8:
					COINMOVEX = 3600
					COINMOVEY = 250
			if NewCar == 46:
				CarX = 2800
				CarY = 200
				Trash1X = 1900
				Trash1Y = 340
				Trash2X = 2800
				Trash2Y = 430
				NewCoin = random.randint(1, 9)
				if NewCoin == 1:
					COINMOVEX = 2050
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 2050
					COINMOVEY = 520
				if NewCoin == 3:
					COINMOVEX = 2420
					COINMOVEY = 250
				if NewCoin == 4:
					COINMOVEX = 2420
					COINMOVEY = 400
				if NewCoin == 5:
					COINMOVEX = 2420
					COINMOVEY = 520
				if NewCoin == 6:
					COINMOVEX = 2700
					COINMOVEY = 250
				if NewCoin == 7:
					COINMOVEX = 2700
					COINMOVEY = 400
				if NewCoin == 8:
					COINMOVEX = 2700
					COINMOVEY = 520
				if NewCoin == 9:
					COINMOVEX = 2880
					COINMOVEY = 400
			if NewCar == 47:
				CarX = 2800
				CarY = 200
				Trash2X = 1900
				Trash2Y = 430
				NewCoin = random.randint(1, 7)
				if NewCoin == 1:
					COINMOVEX = 1970
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 1970
					COINMOVEY = 400
				if NewCoin == 3:
					COINMOVEX = 2522
					COINMOVEY = 250
				if NewCoin == 4:
					COINMOVEX = 2522
					COINMOVEY = 400
				if NewCoin == 5:
					COINMOVEX = 2701
					COINMOVEY = 250
				if NewCoin == 6:
					COINMOVEX = 2701
					COINMOVEY = 400
				if NewCoin == 7:
					COINMOVEX = 2701
					COINMOVEY = 520
			if NewCar == 48:
				CarX = 2800
				CarY = 200
				Trash1X = 2820
				Trash1Y = 460
				Trash2X = 1900
				Trash2Y = 328
				NewCoin = random.randint(1, 7)
				if NewCoin == 1:
					COINMOVEX = 1970
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 1970
					COINMOVEY = 520
				if NewCoin == 3:
					COINMOVEX = 2522
					COINMOVEY = 250
				if NewCoin == 4:
					COINMOVEX = 2522
					COINMOVEY = 400
				if NewCoin == 5:
					COINMOVEX = 2701
					COINMOVEY = 250
				if NewCoin == 6:
					COINMOVEX = 2701
					COINMOVEY = 400
				if NewCoin == 7:
					COINMOVEX = 2660
					COINMOVEY = 520
			if NewCar == 49:
				CarX = 1900
				CarY = 200
				Trash2X = 1900
				Trash2Y = 328
				RottenMeatX = 1940
				RottenMeatY = 580
				NewCoin = random.randint(1, 3)
				if NewCoin == 1:
					COINMOVEX = 1800
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 1800
					COINMOVEY = 400
				if NewCoin == 3:
					COINMOVEX = 1800
					COINMOVEY = 520
			if NewCar == 50:
				CarX = 1900
				CarY = 460
				Trash2X = 1900
				Trash2Y = 328
				RottenMeatX = 1940
				RottenMeatY = 310
				NewCoin = random.randint(1, 3)
				if NewCoin == 1:
					COINMOVEX = 1800
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 1800
					COINMOVEY = 400
				if NewCoin == 3:
					COINMOVEX = 1800
					COINMOVEY = 520
			if NewCar == 51:
				CarX = 1900
				CarY = -460
				Trash1X = 1900
				Trash1Y = 200
				Trash2X = 1900
				Trash2Y = 328
				RottenMeatX = 1940
				RottenMeatY = 580
				NewCoin = random.randint(1, 3)
				if NewCoin == 1:
					COINMOVEX = 1800
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 1800
					COINMOVEY = 400
				if NewCoin == 3:
					COINMOVEX = 1800
					COINMOVEY = 520
			if NewCar == 52:
				CarX = 1900
				CarY = -460
				Trash1X = 1900
				Trash1Y = 460
				Trash2X = 1900
				Trash2Y = 328
				RottenMeatX = 1940
				RottenMeatY = 310
				NewCoin = random.randint(1, 3)
				if NewCoin == 1:
					COINMOVEX = 1800
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 1800
					COINMOVEY = 400
				if NewCoin == 3:
					COINMOVEX = 1800
					COINMOVEY = 520
			if NewCar == 53:
				CarX = 5500
				CarY = 330
				Trash1X = 3533
				Trash1Y = 340
				Trash2X = 1900
				Trash2Y = 328
				NewCoin = random.randint(1, 16)
				if NewCoin == 1:
					COINMOVEX = 2000
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 2000
					COINMOVEY = 520
				if NewCoin == 3:
					COINMOVEX = 2200
					COINMOVEY = 400
				if NewCoin == 4:
					COINMOVEX = 2750
					COINMOVEY = 250
				if NewCoin == 5:
					COINMOVEX = 2750
					COINMOVEY = 400
				if NewCoin == 6:
					COINMOVEX = 2750
					COINMOVEY = 520
				if NewCoin == 7:
					COINMOVEX = 3350
					COINMOVEY = 250
				if NewCoin == 8:
					COINMOVEX = 3350
					COINMOVEY = 400
				if NewCoin == 9:
					COINMOVEX = 3350
					COINMOVEY = 520
				if NewCoin == 10:
					COINMOVEX = 3800
					COINMOVEY = 400
				if NewCoin == 11:
					COINMOVEX = 4650
					COINMOVEY = 250
				if NewCoin == 12:
					COINMOVEX = 4650
					COINMOVEY = 400
				if NewCoin == 13:
					COINMOVEX = 4650
					COINMOVEY = 520
				if NewCoin == 14:
					COINMOVEX = 5400
					COINMOVEY = 250
				if NewCoin == 15:
					COINMOVEX = 5400
					COINMOVEY = 400
				if NewCoin == 16:
					COINMOVEX = 5400
					COINMOVEY = 520
			if NewCar == 54:
				CarX = 5500
				CarY = 330
				Trash1X = 1900
				Trash1Y = 340
				Trash2X = 3533
				Trash2Y = 328
				NewCoin = random.randint(1, 16)
				if NewCoin == 1:
					COINMOVEX = 2000
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 2000
					COINMOVEY = 520
				if NewCoin == 3:
					COINMOVEX = 2200
					COINMOVEY = 400
				if NewCoin == 4:
					COINMOVEX = 2750
					COINMOVEY = 250
				if NewCoin == 5:
					COINMOVEX = 2750
					COINMOVEY = 400
				if NewCoin == 6:
					COINMOVEX = 2750
					COINMOVEY = 520
				if NewCoin == 7:
					COINMOVEX = 3350
					COINMOVEY = 250
				if NewCoin == 8:
					COINMOVEX = 3350
					COINMOVEY = 400
				if NewCoin == 9:
					COINMOVEX = 3350
					COINMOVEY = 520
				if NewCoin == 10:
					COINMOVEX = 3800
					COINMOVEY = 400
				if NewCoin == 11:
					COINMOVEX = 4650
					COINMOVEY = 250
				if NewCoin == 12:
					COINMOVEX = 4650
					COINMOVEY = 400
				if NewCoin == 13:
					COINMOVEX = 4650
					COINMOVEY = 520
				if NewCoin == 14:
					COINMOVEX = 5400
					COINMOVEY = 250
				if NewCoin == 15:
					COINMOVEX = 5400
					COINMOVEY = 400
				if NewCoin == 16:
					COINMOVEX = 5400
					COINMOVEY = 520
			if NewCar == 55:
				CarX = 2700
				CarY = 200
				Trash1X = 1900
				Trash1Y = 340
				Trash2X = 2700
				Trash2Y = 430
				NewCoin = random.randint(1, 7)
				if NewCoin == 1:
					COINMOVEX = 1970
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 1970
					COINMOVEY = 520
				if NewCoin == 3:
					COINMOVEX = 2522
					COINMOVEY = 250
				if NewCoin == 4:
					COINMOVEX = 2522
					COINMOVEY = 400
				if NewCoin == 5:
					COINMOVEX = 2600
					COINMOVEY = 250
				if NewCoin == 6:
					COINMOVEX = 2600
					COINMOVEY = 400
				if NewCoin == 7:
					COINMOVEX = 2660
					COINMOVEY = 520
			if NewCar == 56:
				CarX = 2700
				CarY = 200
				Trash1X = 1900
				Trash1Y = 340
				Trash2X = 2700
				Trash2Y = 430
				RottenMeatX = 2700
				RottenMeatY = 444
				NewCoin = random.randint(1, 6)
				if NewCoin == 1:
					COINMOVEX = 1970
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 1970
					COINMOVEY = 520
				if NewCoin == 3:
					COINMOVEX = 2522
					COINMOVEY = 250
				if NewCoin == 4:
					COINMOVEX = 2522
					COINMOVEY = 400
				if NewCoin == 5:
					COINMOVEX = 2600
					COINMOVEY = 250
				if NewCoin == 6:
					COINMOVEX = 2600
					COINMOVEY = 520
			if NewCar == 57:
				CarX = 2705
				CarY = 460
				Trash1X = 1900
				Trash1Y = 340
				Trash2X = 2700
				Trash2Y = 328
				RottenMeatX = 2700
				RottenMeatY = 310
				NewCoin = random.randint(1, 6)
				if NewCoin == 1:
					COINMOVEX = 1970
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 1970
					COINMOVEY = 520
				if NewCoin == 3:
					COINMOVEX = 2522
					COINMOVEY = 250
				if NewCoin == 4:
					COINMOVEX = 2522
					COINMOVEY = 400
				if NewCoin == 5:
					COINMOVEX = 2600
					COINMOVEY = 250
				if NewCoin == 6:
					COINMOVEX = 2600
					COINMOVEY = 520
			if NewCar == 58:
				CarX = 2700
				CarY = 200
				Trash1X = 1900
				Trash1Y = 340
				Trash2X = 2700
				Trash2Y = 328
				RottenMeatX = 2700
				RottenMeatY = 580
				NewCoin = random.randint(1, 6)
				if NewCoin == 1:
					COINMOVEX = 1970
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 1970
					COINMOVEY = 520
				if NewCoin == 3:
					COINMOVEX = 2522
					COINMOVEY = 250
				if NewCoin == 4:
					COINMOVEX = 2522
					COINMOVEY = 400
				if NewCoin == 5:
					COINMOVEX = 2600
					COINMOVEY = 250
				if NewCoin == 6:
					COINMOVEX = 2600
					COINMOVEY = 520
			if NewCar == 59:
				BarbaX = 1800
				BarbaY = 266
				CarX = 2000
				CarY = -500
				NewCoin = random.randint(1, 5)
				if NewCoin == 1:
					COINMOVEX = 1970
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 1970
					COINMOVEY = 400
				if NewCoin == 3:
					COINMOVEX = 1970
					COINMOVEY = 520
				if NewCoin == 4:
					COINMOVEX = 1800
					COINMOVEY = 400
				if NewCoin == 5:
					COINMOVEX = 1800
					COINMOVEY = 520
			if NewCar == 60:
				BarbaX = 1800
				BarbaY = 410
				CarX = 2000
				CarY = -500
				NewCoin = random.randint(1, 5)
				if NewCoin == 1:
					COINMOVEX = 1970
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 1970
					COINMOVEY = 400
				if NewCoin == 3:
					COINMOVEX = 1970
					COINMOVEY = 520
				if NewCoin == 4:
					COINMOVEX = 1800
					COINMOVEY = 250
				if NewCoin == 5:
					COINMOVEX = 1800
					COINMOVEY = 520
			if NewCar == 61:
				BarbaX = 1800
				BarbaY = 530
				CarX = 2000
				CarY = -500
				NewCoin = random.randint(1, 5)
				if NewCoin == 1:
					COINMOVEX = 1970
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 1970
					COINMOVEY = 400
				if NewCoin == 3:
					COINMOVEX = 1970
					COINMOVEY = 520
				if NewCoin == 4:
					COINMOVEX = 1800
					COINMOVEY = 400
				if NewCoin == 5:
					COINMOVEX = 1800
					COINMOVEY = 250
			if NewCar == 62:
				BarbaX = 1800
				BarbaY = 266
				CarX = 2000
				CarY = 460
				NewCoin = random.randint(1, 5)
				if NewCoin == 1:
					COINMOVEX = 1970
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 1970
					COINMOVEY = 400
				if NewCoin == 3:
					COINMOVEX = 1900
					COINMOVEY = 520
				if NewCoin == 4:
					COINMOVEX = 1800
					COINMOVEY = 400
				if NewCoin == 5:
					COINMOVEX = 1800
					COINMOVEY = 520
			if NewCar == 63:
				Trash1X = 1800
				Trash1Y = 200
				Trash2X = 2500
				Trash2Y = 328
				BarbaX = 3200
				BarbaY = 530
				CarX = 3700
				CarY = 330
				NewCoin = random.randint(1, 11)
				if NewCoin == 1:
					COINMOVEX = 1850
					COINMOVEY = 400
				if NewCoin == 2:
					COINMOVEX = 1850
					COINMOVEY = 520
				if NewCoin == 3:
					COINMOVEX = 2370
					COINMOVEY = 400
				if NewCoin == 4:
					COINMOVEX = 2770
					COINMOVEY = 520
				if NewCoin == 5:
					COINMOVEX = 3200
					COINMOVEY = 400
				if NewCoin == 6:
					COINMOVEX = 3200
					COINMOVEY = 250
				if NewCoin == 7:
					COINMOVEX = 3600
					COINMOVEY = 250
				if NewCoin == 8:
					COINMOVEX = 3600
					COINMOVEY = 400
				if NewCoin == 9:
					COINMOVEX = 3600
					COINMOVEY = 520
				if NewCoin == 10:
					COINMOVEX = 3800
					COINMOVEY = 250
				if NewCoin == 11:
					COINMOVEX = 3800
					COINMOVEY = 520
			if NewCar == 64:
				Trash2X = 1900
				Trash2Y = 195
				Trash1X = 1901
				Trash1Y = 460
				BarbaX = 2800
				BarbaY = 410
				CarX = 3200
				CarY = 330
				NewCoin = random.randint(1, 6)
				if NewCoin == 1:
					COINMOVEX = 1950
					COINMOVEY = 400
				if NewCoin == 2:
					COINMOVEX = 2450
					COINMOVEY = 250
				if NewCoin == 3:
					COINMOVEX = 2450
					COINMOVEY = 520
				if NewCoin == 4:
					COINMOVEX = 3100
					COINMOVEY = 400
				if NewCoin == 5:
					COINMOVEX = 3300
					COINMOVEY = 250
				if NewCoin == 6:
					COINMOVEX = 3300
					COINMOVEY = 520
			if NewCar == 65:
				BarbaX = 2000
				BarbaY = 410
				Trash1X = 3000
				Trash1Y = 340
				MeatX = 4000
				MeatY = 444
				Trash2X = 5000
				Trash2Y = 328
				RottenMeatX = 6000
				RottenMeatY = 444
				CarX = 7000
				CarY = 330
				NewCoin = random.randint(1, 14)
				if NewCoin == 1:
					COINMOVEX = 2000
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 2000
					COINMOVEY = 520
				if NewCoin == 3:
					COINMOVEX = 2500
					COINMOVEY = 250
				if NewCoin == 4:
					COINMOVEX = 2500
					COINMOVEY = 520
				if NewCoin == 5:
					COINMOVEX = 3050
					COINMOVEY = 250
				if NewCoin == 6:
					COINMOVEX = 3050
					COINMOVEY = 520
				if NewCoin == 7:
					COINMOVEX = 3500
					COINMOVEY = 250
				if NewCoin == 8:
					COINMOVEX = 3500
					COINMOVEY = 520
				if NewCoin == 9:
					COINMOVEX = 4900
					COINMOVEY = 400
				if NewCoin == 10:
					COINMOVEX = 6000
					COINMOVEY = 250
				if NewCoin == 11:
					COINMOVEX = 6000
					COINMOVEY = 520
				if NewCoin == 12:
					COINMOVEX = 6500
					COINMOVEY = 250
				if NewCoin == 13:
					COINMOVEX = 6500
					COINMOVEY = 520
				if NewCoin == 14:
					COINMOVEX = 6900
					COINMOVEY = 400
			if NewCar == 66:
				BarbaX = 2000
				BarbaY = 410
				Trash1X = 3000
				Trash1Y = 340
				RottenMeatX = 4000
				RottenMeatY = 444
				Trash2X = 5000
				Trash2Y = 328
				CarX = 6000
				CarY = 330
				NewCoin = random.randint(1, 11)
				if NewCoin == 1:
					COINMOVEX = 2000
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 2000
					COINMOVEY = 520
				if NewCoin == 3:
					COINMOVEX = 2500
					COINMOVEY = 250
				if NewCoin == 4:
					COINMOVEX = 2500
					COINMOVEY = 520
				if NewCoin == 5:
					COINMOVEX = 3050
					COINMOVEY = 250
				if NewCoin == 6:
					COINMOVEX = 3050
					COINMOVEY = 520
				if NewCoin == 7:
					COINMOVEX = 3500
					COINMOVEY = 250
				if NewCoin == 8:
					COINMOVEX = 3500
					COINMOVEY = 520
				if NewCoin == 9:
					COINMOVEX = 4900
					COINMOVEY = 400
				if NewCoin == 10:
					COINMOVEX = 6000
					COINMOVEY = 250
				if NewCoin == 11:
					COINMOVEX = 6000
					COINMOVEY = 520
			if NewCar == 67:
				CarX = 2800
				CarY = -500
				Trash1X = 1900
				Trash1Y = 460
				Trash2X = 2300
				Trash2Y = 328
				BarbaX = 2700
				BarbaY = 266
				NewCoin = random.randint(1, 4)
				if NewCoin == 1:
					COINMOVEX = 2000
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 2700
					COINMOVEY = 400
				if NewCoin == 3:
					COINMOVEX = 2180
					COINMOVEY = 400
				if NewCoin == 4:
					COINMOVEX = 2400
					COINMOVEY = 250
			if NewCar == 68:
				Trash1X = 1900
				Trash1Y = 340
				BarbaX = 2770
				BarbaY = 530
				CarX = 2700
				CarY = 200
				NewCoin = random.randint(1, 4)
				if NewCoin == 1:
					COINMOVEX = 2400
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 2400
					COINMOVEY = 400
				if NewCoin == 3:
					COINMOVEX = 2400
					COINMOVEY = 520
				if NewCoin == 4:
					COINMOVEX = 2640
					COINMOVEY = 400
			if NewCar == 69:
				Trash1X = 1900
				Trash1Y = 340
				BarbaX = 2770
				BarbaY = 266
				CarX = 2700
				CarY = 460
				NewCoin = random.randint(1, 4)
				if NewCoin == 1:
					COINMOVEX = 2400
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 2400
					COINMOVEY = 400
				if NewCoin == 3:
					COINMOVEX = 2400
					COINMOVEY = 520
				if NewCoin == 4:
					COINMOVEX = 2640
					COINMOVEY = 400
			if NewCar == 70:
				Trash1X = 1900
				Trash1Y = 200
				Trash2X = 1900
				Trash2Y = 328
				CarX = 2700
				CarY = 460
				BarbaX = 2750
				BarbaY = 410
				NewCoin = random.randint(1, 5)
				if NewCoin == 1:
					COINMOVEX = 2000
					COINMOVEY = 520
				if NewCoin == 2:
					COINMOVEX = 2400
					COINMOVEY = 520
				if NewCoin == 3:
					COINMOVEX = 2400
					COINMOVEY = 400
				if NewCoin == 4:
					COINMOVEX = 2400
					COINMOVEY = 250
				if NewCoin == 5:
					COINMOVEX = 2750
					COINMOVEY = 250
			if NewCar == 71:
				Trash1X = 1900
				Trash1Y = 200
				Trash2X = 1900
				Trash2Y = 328
				CarX = 2700
				CarY = 460
				RottenMeatX = 2750
				RottenMeatY = 444
				NewCoin = random.randint(1, 5)
				if NewCoin == 1:
					COINMOVEX = 2000
					COINMOVEY = 520
				if NewCoin == 2:
					COINMOVEX = 2400
					COINMOVEY = 520
				if NewCoin == 3:
					COINMOVEX = 2400
					COINMOVEY = 400
				if NewCoin == 4:
					COINMOVEX = 2400
					COINMOVEY = 250
				if NewCoin == 5:
					COINMOVEX = 2750
					COINMOVEY = 250
			if NewCar == 72:
				Trash1X = 1950
				Trash1Y = 460
				Trash2X = 1900
				Trash2Y = 328
				CarX = 2700
				CarY = 200
				BarbaX = 2770
				BarbaY = 410
				NewCoin = random.randint(1, 5)
				if NewCoin == 1:
					COINMOVEX = 2000
					COINMOVEY = 250
				if NewCoin == 2:
					COINMOVEX = 2400
					COINMOVEY = 520
				if NewCoin == 3:
					COINMOVEX = 2400
					COINMOVEY = 400
				if NewCoin == 4:
					COINMOVEX = 2400
					COINMOVEY = 250
				if NewCoin == 5:
					COINMOVEX = 2750
					COINMOVEY = 520


				
		#Health Cap
		if health_value > 3:
			health_value = 3

		
		#If Obstacles or other so then it respawns and moves the the background again so its not plain and boring goes off screen
		if MeatX <= -300:
			MeatY = -100

		if Trash1X <= -250:
			Trash1Y = -900

		if Trash2X <= -290:
			Trash2Y = -900

		if WedgyX <= -400:
			WedgyY = -666

		if RottenMeatX <= -300:
			RottenMeatY = -100

		if BarbaX <= -170:
			BarbaY = -500

		#Background Respawn so then it respawns and moves the the background again so its not plain and boring
		if EndX <= -500:
			NewBack = random.randint(1, 29)
			if NewBack == 1:
				LadderX = 1800
				LadderY = -2
				EndX = 1900
			if NewBack == 2:
				sgX = 1800
				sgY = 10
				EndX = 1900
			if NewBack == 3:
				Pipe1X = 2000
				Pipe1Y = -2
				Pipe2X = 3000
				Pipe2Y = 10
				EndX = 3500
			if NewBack == 4:
				TunnelX = 1900
				TunnelY = 10
				EndX = 2500
			if NewBack == 5:
				DontEatX = 1800
				DontEatY = 30
				EndX = 2000
			if NewBack == 6:
				LadderX = 2100
				LadderY = -2
				Pipe1X = 2100
				Pipe1Y = -2
				EndX = 2500
			if NewBack == 7:
				LadderX = 3200
				LadderY = -2
				Pipe1X = 2100
				Pipe1Y = -2
				EndX = 3500
			if NewBack == 8:
				Pipe2X = 2000
				Pipe2Y = 10
				TunnelX = 3700
				TunnelY = 10
				Pipe1X = 4200
				Pipe1Y = -2
				EndX = 5700
			if NewBack == 9:
				Pipe2X = 2000
				Pipe2Y = 10
				TunnelX = 3700
				TunnelY = 10
				Pipe1X = 4500
				Pipe1Y = -2
				EndX = 5000
			if NewBack == 10:
				Pipe1X = 2000
				Pipe1Y = -2
				EndX = 2700
			if NewBack == 11:
				Pipe2X = 2000
				Pipe2Y = 10
				EndX = 2500
			if NewBack == 12:
				Pipe2X = 2000
				Pipe2Y = 10
				LadderX = 2800
				LadderY = -2
				EndX = 3000
			if NewBack == 13:
				Pipe2X = 2200
				Pipe2Y = 10
				LadderX = 2000
				LadderY = -2
				EndX = 3000
			if NewBack == 14:
				Pipe2X = 2200
				Pipe2Y = 10
				LadderX = 4500
				LadderY = -2
				Pipe1X = 6000
				Pipe1Y = -2
				EndX = 6600
			if NewBack == 15:
				LadderX = 4800
				LadderY = -2
				TunnelX = 8700
				TunnelY = 10
				Pipe2X = 2000
				Pipe2Y = 10
				Pipe1X = 6700
				Pipe1Y = -2
				EndX = 9700
			if NewBack == 16:
				Pipe2X = 2200
				Pipe2Y = 10
				LadderX = 4500
				LadderY = -2
				Pipe1X = 6000
				Pipe1Y = -2
				EndX = 6600
			if NewBack == 17:
				LadderX = 4800
				LadderY = -2
				TunnelX = 8700
				TunnelY = 10
				Pipe2X = 2000
				Pipe2Y = 10
				Pipe1X = 6700
				Pipe1Y = -2
				EndX = 9700
			if NewBack == 18:
				Pipe2X = 2200
				Pipe2Y = 10
				LadderX = 4500
				LadderY = -2
				Pipe1X = 6000
				Pipe1Y = -2
				EndX = 6600
			if NewBack == 19:
				LadderX = 5800
				LadderY = -2
				TunnelX = 10700
				TunnelY = 10
				Pipe2X = 2000
				Pipe2Y = 10
				Pipe1X = 7707
				Pipe1Y = -2
				EndX = 11700
			if NewBack == 20:
				Pipe2X = 2000
				Pipe2Y = 10
				TunnelX = 4700
				TunnelY = 10
				Pipe1X = 6500
				Pipe1Y = -2
				EndX = 7500
			if NewBack == 21:
				CloseMouthX = 2000
				CloseMouthY = 55
				EndX = 2100
			if NewBack == 22:
				Pipe1X = 2000
				Pipe1Y = -2
				CloseMouthX = 2300
				CloseMouthY = 55
				EndX = 2222
			if NewBack == 23:
				TunnelX = 2000
				TunnelY = 10
				Pipe1X = 3000
				Pipe1Y = -2
				CloseMouthX = 3300
				CloseMouthY = 55
				LadderX = 4400
				LadderY = -2
				EndX = 4444
			if NewBack == 24:
				TunnelX = 2000
				TunnelY = 10
				Pipe1X = 3000
				Pipe1Y = -2
				LadderX = 4400
				LadderY = -2
				EndX = 4444
			if NewBack == 25:
				Pipe2X = 2000
				Pipe2Y = 10
				CloseMouthX = 3300
				CloseMouthY = 55
				LadderX = 4000
				LadderY = -2
				EndX = 4100
			if NewBack == 26:
				Pipe2X = 2000
				Pipe2Y = 10
				DontEatX = 3300
				DontEatY = 30
				LadderX = 4000
				LadderY = -2
				EndX = 4100
			if NewBack == 27:
				CloseMouthX = 2000
				CloseMouthY = 55
				TunnelX = 2700
				TunnelY = 10
				Pipe2X = 3300
				Pipe2Y = 10
				EndX = 3500
			if NewBack == 28:
				sgX = 1800
				sgY = 10
				LadderX = 2150
				LadderY = -2
				EndX = 2300
			if NewBack == 29:
				LadderX = 8800
				LadderY = -2
				TunnelX = 4300
				TunnelY = 10
				Pipe2X = 6600
				Pipe2Y = 10
				Pipe1X = 2000
				Pipe1Y = -2
				EndX = 8990
				

		if BarrelX <= -500:
			NewBarrel = random.randint(1, 5)
			if NewBarrel == 1:
				BarrelX = 1800
			if NewBarrel == 2:
				BarrelX = 2800
			if NewBarrel == 3:
				BarrelX = 5800
			if NewBarrel == 4:
				BarrelX = 7800
			if NewBarrel == 5:
				BarrelX = 9800

		if ClosePipeX <= -3500:
			NewClosePipe = random.randint(1, 5)
			if NewClosePipe == 1:
				ClosePipeX = 1800
			if NewClosePipe == 2:
				ClosePipeX = 9800
			if NewClosePipe == 3:
				ClosePipeX = 59800
			if NewClosePipe == 4:
				ClosePipeX = 35800
			if NewClosePipe == 5:
				ClosePipeX = 75000


		#If Crockettdile and Coin are in the same lane then randomly choose another lane to spawn in
		if COINMOVEX <= 400 and COINMOVEX >= -10 and y == 170 and COINMOVEY == 250:
			COINMOVEY = -200
			score_value += 5
		if COINMOVEX <= 400 and COINMOVEX >= -10 and y == 300 and COINMOVEY == 400:
			COINMOVEY = -200
			score_value += 5
		if COINMOVEX <= 400 and COINMOVEX >= -10 and y == 430 and COINMOVEY == 520:
			COINMOVEY = -200
			score_value += 5

		
		#If Meat is Eaten
		if MeatX <= 400 and MeatX >= 50 and y == 170 and MeatY == 310 and action == 2:
			MeatY = -100
			dif += 5
			score_value += 10
			health_value += 1
		if MeatX <= 400 and MeatX >= 50 and y == 430 and MeatY == 580 and action == 2:
			MeatY = -100
			dif += 5
			score_value += 10
			health_value += 1
		if MeatX <= 400 and MeatX >= 50 and y == 300 and MeatY == 444 and action == 2:
			MeatY = -100
			dif += 5
			score_value += 10
			health_value += 1

		#If Rotten Meat is Eaten
		if RottenMeatX <= 400 and RottenMeatX >= 80 and y == 170 and RottenMeatY == 310 and action == 2:
			RottenMeatY = -100
			dif = 4
			score_value -= 10
			health_value -= 2
		if RottenMeatX <= 400 and RottenMeatX >= 80 and y == 430 and RottenMeatY == 580 and action == 2:
			RottenMeatY = -100
			dif = 4
			score_value -= 10
			health_value -= 2
		if RottenMeatX <= 400 and RottenMeatX >= 80 and y == 300 and RottenMeatY == 444 and action == 2:
			RottenMeatY = -100
			dif = 4
			score_value -= 10
			health_value -= 2

		#If Braden Barba is touched
		if BarbaX <= 380 and BarbaX >= 100 and y == 170 and BarbaY == 266:
			BarbaY = -500
			dif += 5
			score_value += 20
		if BarbaX <= 380 and BarbaX >= 100 and y == 300 and BarbaY == 410:
			BarbaY = -500
			dif += 5
			score_value += 20
		if BarbaX <= 380 and BarbaX >= 100 and y == 430 and BarbaY == 530:
			BarbaY = -500
			dif += 5
			score_value += 20

		#If Car is Touched
		if CarX <= 300 and CarX >= -100 and y == 170 and CarY == 200:
			CarY = -600
			dif = 4
			score_value -= 15
			if action == 1:
				health_value -= 1
			elif action == 2:
				health_value -= 2
		if CarX <= 300 and  CarX >= -100 and y == 300 and CarY == 330:
			CarY = -600
			dif = 4
			score_value -= 15
			if action == 1:
				health_value -= 1
			elif action == 2:
				health_value -= 2
		if CarX <= 300 and CarX >= -100 and y == 430 and CarY == 460:
			CarY = -600
			dif = 4
			score_value -= 15
			if action == 1:
				health_value -= 1
			elif action == 2:
				health_value -= 2
			

		#Devin sprite touched
		if WedgyX <= 400 and WedgyX >= 50 and y == 170 and WedgyY == 186 and action == 2:
			WedgyY = -1000
			dif += 5
			score_value += 10
			health_value += 1
		if WedgyX <= 400 and WedgyX >= 50 and y == 300 and WedgyY == 320 and action == 2:
			WedgyY = -1000
			dif += 5
			score_value += 10
			health_value += 1
		if WedgyX <= 400 and WedgyX >= 50 and y == 430 and WedgyY == 444 and action == 2:
			WedgyY = -1000
			dif += 5
			score_value += 10
			health_value += 1


		if WedgyX <= 400 and WedgyX >= 20 and y == 170 and WedgyY == 186 and action == 1:
			WedgyY = -1000
			dif = 4
			score_value -= 10
			health_value -= 1
		if WedgyX <= 400 and WedgyX >= 20 and y == 300 and WedgyY == 320 and action == 1:
			WedgyY = -1000
			dif = 4
			score_value -= 10
			health_value += -1
		if WedgyX <= 400 and WedgyX >= 20 and y == 430 and WedgyY == 444 and action == 1:
			WedgyY = -1000
			dif = 4
			score_value -= 10
			health_value -= 1



		#If touching Trash1 (The pile of cement so then it respawns and moves the the background again so its not plain and boring)
		if Trash1X <= 400 and Trash1X >= -100 and y == 170 and Trash1Y == 200:
			Trash1Y = -250
			dif = 4
			if action == 1:
				health_value -= 1
			elif action == 2:
				health_value -= 2
		if Trash1X <= 400 and Trash1X >= -100 and y == 300 and Trash1Y == 340:
			Trash1Y = -250
			dif = 4
			if action == 1:
				health_value -= 1
			elif action == 2:
				health_value -= 2
		if Trash1X <= 400 and Trash1X >= -100 and y == 430 and Trash1Y == 460:
			Trash1Y = -250
			dif = 4
			if action == 1:
				health_value -= 1
			elif action == 2:
				health_value -= 2

		#If touching Trash2 (The alcohol pile)
		if Trash2X <= 400 and Trash2X >= -100 and y == 170 and Trash2Y == 195:
			Trash2Y = -250
			dif = 4
			if action == 1:
				health_value -= 1
			elif action == 2:
				health_value -= 2
		if Trash2X <= 400 and Trash2X >= -100 and y == 300 and Trash2Y == 328:
			Trash2Y = -250
			dif = 4
			if action == 1:
				health_value -= 1
			elif action == 2:
				health_value -= 2
		if Trash2X <= 400 and Trash2X >= -100 and y == 430 and Trash2Y == 430:
			Trash2Y = -250
			dif = 4
			if action == 1:
				health_value -= 1
			elif action == 2:
				health_value -= 2


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
		screen.blit(EndofBackStuff, (EndX, EndY))
		screen.blit(DontEatHim, (DontEatX, DontEatY))
		screen.blit(CloseMouth, (CloseMouthX, CloseMouthY))
		screen.blit(SeanGraffiti, (sgX, sgY))
		screen.blit(SewerTunnel, (TunnelX, TunnelY))
		screen.blit(SewerLadder, (LadderX, LadderY))
		screen.blit(SewerPipe2, (Pipe2X, Pipe2Y))
		screen.blit(SewerPipe, (Pipe1X, Pipe1Y))
		screen.blit(FrontBarrels, (BarrelX, BarrelY))
		screen.blit(RottenMeat, (RottenMeatX, RottenMeatY))
		screen.blit(GoWeegyGo, (WedgyX, WedgyY))
		screen.blit(HalfaCar, (CarX, CarY))
		screen.blit(Trash2, (Trash2X, Trash2Y))
		screen.blit(Trash1, (Trash1X, Trash1Y))
		screen.blit(Barba, (BarbaX, BarbaY))
		screen.blit(Coin, (COINMOVEX, COINMOVEY))
		screen.blit(Meat, (MeatX, MeatY))
		screen.blit(animation_list[action][frame], (x, y))
		screen.blit(ClosePipe, (ClosePipeX, ClosePipeY))
		screen.blit(Heart, (HeartX, HeartY))
		
		screen.blit(GameOverScreeny, (GameOverX, GameOverY))


		if health_value <= 0:
			dif = 0
			scroll = 0
			bg = pygame.image.load('Black.jpg').convert()
			GameOverX = 0
			GameOverY = 0


			COINMOVEY = 10000
			Trash1Y = 10000
			Trash2Y = 10000
			MeatY = 10000
			TunnelY = 10000
			Pipe1Y = 10000
			Pipe2Y = 10000
			LadderY = 10000
			sgY = 10000
			CarY = 10000
			WedgyY = 10000
			HeartY = 10000
			textY = 10000
			textYY = 10000
			GameOverRetry = True


		#event handler and Crockettdile Movement
		for event in pygame.event.get():
			keys = pygame.key.get_pressed()

			if keys[pygame.K_RETURN] and GameOverRetry == True:
				action = 1
				health_value = 3
				score_value = 0
				bg = pygame.image.load('sewer_background.jpg').convert()
				GameOverRetry = False
				dif = 4
				GameOverX = -999990
				GameOverY = -999990
				y = 300
				CarX = -499
				CarY = -500
				EndX = -499
				EndY = 10
				textX = 10
				textXX = 110
				textY = 10
				textYY = 80
				HeartX = -100
				HeartY = -40
	
			if keys[pygame.K_w]:
				y -= 65
			if keys[pygame.K_s]:
				y += 65

			#eating motion
			if keys[pygame.K_SPACE]:
				if cooldown == False:
					if is_eating == True:
						action = 1
						is_eating = False
						cooldown = True

					elif is_eating == False:
						action = 2
						is_eating = True
						cooldown = True
			else:
				cooldown = False
		
			
			if keys[pygame.K_ESCAPE]:
				run = False

		show_score(textX, textY)
		show_health(textXX, textYY)
		pygame.display.update()

pygame.quit()
