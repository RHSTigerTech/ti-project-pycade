import pygame, random, math, os
import Crocodile2

# from pygame import mixer

pygame.init()

#redirects file finder to folder
os.chdir('Crocketdile_images')

SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 756

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Crockettdile')

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
HalfaCar = pygame.image.load("halfAcar.png")
FrontBarrels = pygame.image.load("frontBarrel.png")
GoWeegyGo = pygame.image.load("Wedgysavehim.png")
Heart = pygame.image.load("heart.png")
Barba = pygame.image.load("barberCoin.png")
GameOverScreeny = pygame.image.load("gameOver_screen.jpg")
DontEatHim = pygame.image.load("DontEatGoWeegy.png")
EndofBackStuff = pygame.image.load("EndofBackStuff.png")
RottenMeat = pygame.image.load("RottenMeat.png")

#Barba image size
default_size = (250, 250)
Barba = pygame.transform.scale(Barba, default_size)
default_position = (200, 200)


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
BarbaX = -1000
BarbaY = -1000
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
GameOverRetry = False


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
textY = 10
textYY = 80

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





run = True
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


		#update animation
		current_time = pygame.time.get_ticks()
		if current_time - last_update >= animation_cooldown:
			frame += 1
			last_update = current_time
			if frame >= len(animation_list[action]):
				frame = 0

		#If the coin reaches the edge of the screen then randomly choose a new lane to respawn
		if COINMOVEX <= -100:
			CoinSpot = random.randint(1, 6)
			if CoinSpot == 1:
				COINMOVEX = 1800
				COINMOVEY = 250
			if CoinSpot == 2:
				COINMOVEX = 1800
				COINMOVEY = 400
			if CoinSpot == 3:
				COINMOVEX = 1800
				COINMOVEY = 520
			if CoinSpot == 4:
				COINMOVEX = 2800
				COINMOVEY = 250
			if CoinSpot == 5:
				COINMOVEX = 2800
				COINMOVEY = 400
			if CoinSpot == 6:
				COINMOVEX = 2800
				COINMOVEY = 520
		
		if CarX <= -250:
			NewCar = random.randint(1, 53)
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
			if NewCar == 2:
				CarX = 6000
				CarY = 330
				MeatX = 5000
				MeatY = 580
				WedgyX = 1700
				WedgyY = 320
			if NewCar == 3:
				CarX = 5000
				CarY = 460
				MeatX = 3000
				MeatY = 444
			if NewCar == 4:
				CarX = 5500
				CarY = 200
				Trash1X = 5500
				Trash1Y = 460
			if NewCar == 5:
				CarX = 7000
				CarY = 460
				Trash2X = 5500
				Trash2Y = 328
			if NewCar == 6:
				CarX = 7000
				CarY = 460
				Trash2X = 5500
				Trash2Y = 328
				MeatX = 5000
				MeatY = 444
			if NewCar == 7:
				CarX = 3000
				CarY = 330
				Trash1X = 2000
				Trash1Y = 200
				Trash2X = 2000
				Trash2Y = 328
			if NewCar == 8:
				CarX = 3000
				CarY = 330
				Trash1X = 2000
				Trash1Y = 460
				Trash2X = 2000
				Trash2Y = 195
			if NewCar == 9:
				CarX = 2100
				CarY = -1000
				Trash1X = 2000
				Trash1Y = 460
				Trash2X = 2000
				Trash2Y = 195
				WedgyX = 1700
				WedgyY = 444
			if NewCar == 10:
				CarX = 2100
				CarY = -1000
				Trash1X = 2000
				Trash1Y = 200
				Trash2X = 2000
				Trash2Y = 430
			if NewCar == 11:
				Trash1X = 1900
				Trash1Y = 200
				CarX = 2000
				CarY = 2000
			if NewCar == 12:
				Trash1X = 1900
				Trash1Y = 340
				CarX = 2000
				CarY = 2000
			if NewCar == 13:
				Trash1X = 1900
				Trash1Y = 460
				CarX = 2000
				CarY = 2000
			if NewCar == 14:
				Trash2X = 1900
				Trash2Y = 195
				CarX = 2000
				CarY = 2000
			if NewCar == 15:
				Trash2X = 1900
				Trash2Y = 328
				CarX = 2000
				CarY = 2000
			if NewCar == 16:
				Trash2X = 1900
				Trash2Y = 430
				CarX = 2000
				CarY = 2000
			if NewCar == 17:
				CarX = 2100
				CarY = -1000
				Trash1X = 2000
				Trash1Y = 460
				Trash2X = 2000
				Trash2Y = 195
				MeatX = 1800
				MeatY = 444
			if NewCar == 18:
				CarX = 2100
				CarY = -1000
				Trash1X = 2000
				Trash1Y = 340
				Trash2X = 1900
				Trash2Y = 430
			if NewCar == 19:
				CarX = 5500
				CarY = 200
				MeatX = 1800
				MeatY = 310
				Trash1X = 3000
				Trash1Y = 460
				Trash2X = 4444
				Trash2Y = 328
			if NewCar == 20:
				CarX = 6000
				CarY = 330
				MeatX = 5000
				MeatY = 580
			if NewCar == 21:
				CarX = 5500
				CarY = 200
				RottenMeatX = 1800
				RottenMeatY = 310
				Trash1X = 3000
				Trash1Y = 460
				Trash2X = 4444
				Trash2Y = 328
			if NewCar == 22:
				CarX = 6000
				CarY = 330
				RottenMeatX = 5000
				RottenMeatY = 580
			if NewCar == 23:
				CarX = 2300
				CarY = -500
				Trash1X = 1900
				Trash1Y = 200
				MeatX = 2100
				MeatY = 444
				RottenMeatX = 2300
				RottenMeatY = 580
			if NewCar == 24:
				CarX = 2200
				CarY = -500
				Trash1X = 1900
				Trash1Y = 200
				MeatX = 2300
				MeatY = 580
				RottenMeatX = 2100
				RottenMeatY = 444
			if NewCar == 25:
				CarX = 2100
				CarY = -500
				RottenMeatX = 1900
				RottenMeatY = 310
				MeatX = 1900
				MeatY = 580
			if NewCar == 26:
				CarX = 2100
				CarY = 330
				RottenMeatX = 1900
				RottenMeatY = 310
				MeatX = 1900
				MeatY = 580
			if NewCar == 27:
				CarX = 2100
				CarY = 460
				RottenMeatX = 1900
				RottenMeatY = 310
				MeatX = 1900
				MeatY = 580
			if NewCar == 28:
				CarX = 2100
				CarY = -500
				RottenMeatX = 1900
				RottenMeatY = 580
				MeatX = 1900
				MeatY = 310
			if NewCar == 29:
				CarX = 2100
				CarY = 330
				RottenMeatX = 1900
				RottenMeatY = 580
				MeatX = 1900
				MeatY = 310
			if NewCar == 30:
				CarX = 2100
				CarY = 460
				RottenMeatX = 1900
				RottenMeatY = 580
				MeatX = 1900
				MeatY = 310
			if NewCar == 31:
				CarX = 2100
				CarY = -500
				RottenMeatX = 1900
				RottenMeatY = 580
			if NewCar == 32:
				CarX = 2100
				CarY = 330
				RottenMeatX = 1900
				RottenMeatY = 580
			if NewCar == 33:
				CarX = 2100
				CarY = 460
				RottenMeatX = 1900
				RottenMeatY = 580
			if NewCar == 34:
				CarX = 2100
				CarY = -500
				RottenMeatX = 1900
				RottenMeatY = 310
			if NewCar == 35:
				CarX = 2100
				CarY = -500
				RottenMeatX = 1900
				RottenMeatY = 444
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
			if NewCar == 38:
				CarX = 4500
				CarY = 330
				Trash1X = 2700
				Trash1Y = 340
				Trash2X = 1900
				Trash2Y = 430
			if NewCar == 39:
				CarX = 4500
				CarY = 330
				Trash1X = 2700
				Trash1Y = 340
				Trash2X = 1900
				Trash2Y = 430
				RottenMeatX = 3653
				RottenMeatY = 310
			if NewCar == 40:
				CarX = 3000
				CarY = 330
				Trash1X = 2700
				Trash1Y = 460
				Trash2X = 1900
				Trash2Y = 328
			if NewCar == 41:
				CarX = 3000
				CarY = 460
				Trash1X = 1900
				Trash1Y = 340
				Trash2X = 2700
				Trash2Y = 195
			if NewCar == 42:
				CarX = 3000
				CarY = 330
				Trash1X = 2700
				Trash1Y = 460
				Trash2X = 1900
				Trash2Y = 328
				RottenMeatX = 2700
				RottenMeatY = 310
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
			if NewCar == 44:
				CarX = 5000
				CarY = 460
				RottenMeatX = 1900
				RottenMeatY = 310
				Trash1X = 3309
				Trash1Y = 200
				Trash2X = 4044
				Trash2Y = 328
			if NewCar == 45:
				CarX = 3500
				CarY = 460
				RottenMeatX = 1900
				RottenMeatY = 310
				Trash1X = 2209
				Trash1Y = 460
				Trash2X = 3044
				Trash2Y = 328
			if NewCar == 46:
				CarX = 2800
				CarY = 200
				Trash1X = 1900
				Trash1Y = 340
				Trash2X = 2800
				Trash2Y = 430
			if NewCar == 47:
				CarX = 2800
				CarY = 200
				Trash2X = 1900
				Trash2Y = 430
			if NewCar == 48:
				CarX = 2800
				CarY = 200
				Trash1X = 2800
				Trash1Y = 460
				Trash2X = 1900
				Trash2Y = 328
			if NewCar == 49:
				CarX = 1900
				CarY = 200
				Trash2X = 1900
				Trash2Y = 328
				RottenMeatX = 1900
				RottenMeatY = 580
			if NewCar == 50:
				CarX = 1900
				CarY = 460
				Trash2X = 1900
				Trash2Y = 328
				RottenMeatX = 1900
				RottenMeatY = 310
			if NewCar == 51:
				CarX = 1900
				CarY = -460
				Trash1X = 1900
				Trash1Y = 200
				Trash2X = 1900
				Trash2Y = 328
				RottenMeatX = 1900
				RottenMeatY = 580
			if NewCar == 52:
				CarX = 1900
				CarY = -460
				Trash1X = 1900
				Trash1Y = 460
				Trash2X = 1900
				Trash2Y = 328
				RottenMeatX = 1900
				RottenMeatY = 310
			if NewCar == 53:
				CarX = 5500
				CarY = 330
				Trash1X = 3533
				Trash1Y = 340
				Trash2X = 1900
				Trash2Y = 328


				
		#Health Cap
		if health_value > 3:
			health_value = 3

		
		#If Obstacles or other so then it respawns and moves the the background again so its not plain and boring goes off screen
		if MeatX <= -150:
			MeatY = -100

		if Trash1X <= -170:
			Trash1Y = -900

		if Trash2X <= -240:
			Trash2Y = -900

		if WedgyX <= -200:
			WedgyY = -666

		if RottenMeatX <= -150:
			RottenMeatY = -100

		#Background Respawn so then it respawns and moves the the background again so its not plain and boring
		if EndX <= -500:
			NewBack = random.randint(1, 19)
			print(NewBack)
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




		#If Crockettdile and Coin are in the same lane then randomly choose another lane to spawn in
		if COINMOVEX <= 400 and y == 170 and COINMOVEY == 250:
			score_value += 5
			CoinSpot = random.randint(1, 6)
			if CoinSpot == 1:
				COINMOVEX = 1800
				COINMOVEY = 250
			if CoinSpot == 2:
				COINMOVEX = 1800
				COINMOVEY = 400
			if CoinSpot == 3:
				COINMOVEX = 1800
				COINMOVEY = 520
			if CoinSpot == 4:
				COINMOVEX = 2800
				COINMOVEY = 250
			if CoinSpot == 5:
				COINMOVEX = 2800
				COINMOVEY = 400
			if CoinSpot == 6:
				COINMOVEX = 2800
				COINMOVEY = 520
		if COINMOVEX <= 400 and y == 300 and COINMOVEY == 400:
			score_value += 5
			CoinSpot = random.randint(1, 6)
			if CoinSpot == 1:
				COINMOVEX = 1800
				COINMOVEY = 250
			if CoinSpot == 2:
				COINMOVEX = 1800
				COINMOVEY = 400
			if CoinSpot == 3:
				COINMOVEX = 1800
				COINMOVEY = 520
			if CoinSpot == 4:
				COINMOVEX = 2800
				COINMOVEY = 250
			if CoinSpot == 5:
				COINMOVEX = 2800
				COINMOVEY = 400
			if CoinSpot == 6:
				COINMOVEX = 2800
				COINMOVEY = 520
		if COINMOVEX <= 400 and y == 430 and COINMOVEY == 520:
			score_value += 5
			CoinSpot = random.randint(1, 6)
			if CoinSpot == 1:
				COINMOVEX = 1800
				COINMOVEY = 250
			if CoinSpot == 2:
				COINMOVEX = 1800
				COINMOVEY = 400
			if CoinSpot == 3:
				COINMOVEX = 1800
				COINMOVEY = 520
			if CoinSpot == 4:
				COINMOVEX = 2800
				COINMOVEY = 250
			if CoinSpot == 5:
				COINMOVEX = 2800
				COINMOVEY = 400
			if CoinSpot == 6:
				COINMOVEX = 2800
				COINMOVEY = 520
		
		#If Meat is Eaten
		if MeatX <= 400 and y == 170 and MeatY == 310 and action == 2:
			MeatY = -100
			dif += 5
			score_value += 10
			health_value += 1
		if MeatX <= 400 and y == 430 and MeatY == 580 and action == 2:
			MeatY = -100
			dif += 5
			score_value += 10
			health_value += 1
		if MeatX <= 400 and y == 300 and MeatY == 444 and action == 2:
			MeatY = -100
			dif += 5
			score_value += 10
			health_value += 1

		#If Rotten Meat is Eaten
		if RottenMeatX <= 400 and y == 170 and RottenMeatY == 310 and action == 2:
			RottenMeatY = -100
			dif = 4
			score_value -= 10
			health_value -= 2
		if RottenMeatX <= 400 and y == 430 and RottenMeatY == 580 and action == 2:
			RottenMeatY = -100
			dif = 4
			score_value -= 10
			health_value -= 2
		if RottenMeatX <= 400 and y == 300 and RottenMeatY == 444 and action == 2:
			RottenMeatY = -100
			dif = 4
			score_value -= 10
			health_value -= 2

		#If Car is Touched
		if CarX <= 300 and y == 170 and CarY == 200:
			dif = 4
			score_value -= 15
			if action == 1:
				health_value -= 1
			elif action == 2:
				health_value -= 2
			NewCar = random.randint(1, 18)
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
			if NewCar == 2:
				CarX = 6000
				CarY = 330
				MeatX = 5000
				MeatY = 580
				WedgyX = 1700
				WedgyY = 320
			if NewCar == 3:
				CarX = 7000
				CarY = 460
				MeatX = 3000
				MeatY = 444
			if NewCar == 4:
				CarX = 5500
				CarY = 200
				Trash1X = 5500
				Trash1Y = 460
			if NewCar == 5:
				CarX = 7000
				CarY = 460
				Trash2X = 5500
				Trash2Y = 328
			if NewCar == 6:
				CarX = 7000
				CarY = 460
				Trash2X = 5500
				Trash2Y = 328
				MeatX = 5000
				MeatY = 444
			if NewCar == 7:
				CarX = 3000
				CarY = 330
				Trash1X = 2000
				Trash1Y = 200
				Trash2X = 2000
				Trash2Y = 328
			if NewCar == 8:
				CarX = 3000
				CarY = 330
				Trash1X = 2000
				Trash1Y = 460
				Trash2X = 2000
				Trash2Y = 195
			if NewCar == 9:
				CarX = 2100
				CarY = -1000
				Trash1X = 2000
				Trash1Y = 460
				Trash2X = 2000
				Trash2Y = 195
				WedgyX = 1700
				WedgyY = 444
			if NewCar == 10:
				CarX = 2100
				CarY = -1000
				Trash1X = 2000
				Trash1Y = 200
				Trash2X = 2000
				Trash2Y = 430
			if NewCar == 11:
				Trash1X = 1900
				Trash1Y = 200
				CarX = 2000
				CarY = 2000
			if NewCar == 12:
				Trash1X = 1900
				Trash1Y = 340
				CarX = 2000
				CarY = 2000
			if NewCar == 13:
				Trash1X = 1900
				Trash1Y = 460
				CarX = 2000
				CarY = 2000
			if NewCar == 14:
				Trash2X = 1900
				Trash2Y = 195
				CarX = 2000
				CarY = 2000
			if NewCar == 15:
				Trash2X = 1900
				Trash2Y = 328
				CarX = 2000
				CarY = 2000
			if NewCar == 16:
				Trash2X = 1900
				Trash2Y = 430
				CarX = 2000
				CarY = 2000
			if NewCar == 17:
				CarX = 2100
				CarY = -1000
				Trash1X = 2000
				Trash1Y = 460
				Trash2X = 2000
				Trash2Y = 195
				MeatX = 1800
				MeatY = 444
			if NewCar == 18:
				CarX = 2100
				CarY = -1000
				Trash1X = 2000
				Trash1Y = 340
				Trash2X = 1900
				Trash2Y = 430
		if CarX <= 300 and y == 300 and CarY == 330:
			dif = 4
			score_value -= 15
			if action == 1:
				health_value -= 1
			elif action == 2:
				health_value -= 2
			NewCar = random.randint(1, 18)
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
			if NewCar == 2:
				CarX = 6000
				CarY = 330
				MeatX = 5000
				MeatY = 580
				WedgyX = 1700
				WedgyY = 320
			if NewCar == 3:
				CarX = 7000
				CarY = 460
				MeatX = 3000
				MeatY = 444
			if NewCar == 4:
				CarX = 5500
				CarY = 200
				Trash1X = 5500
				Trash1Y = 460
			if NewCar == 5:
				CarX = 7000
				CarY = 460
				Trash2X = 5500
				Trash2Y = 328
			if NewCar == 6:
				CarX = 7000
				CarY = 460
				Trash2X = 5500
				Trash2Y = 328
				MeatX = 5000
				MeatY = 444
			if NewCar == 7:
				CarX = 3000
				CarY = 330
				Trash1X = 2000
				Trash1Y = 200
				Trash2X = 2000
				Trash2Y = 328
			if NewCar == 8:
				CarX = 3000
				CarY = 330
				Trash1X = 2000
				Trash1Y = 460
				Trash2X = 2000
				Trash2Y = 195
			if NewCar == 9:
				CarX = 2100
				CarY = -1000
				Trash1X = 2000
				Trash1Y = 460
				Trash2X = 2000
				Trash2Y = 195
				WedgyX = 1700
				WedgyY = 444
			if NewCar == 10:
				CarX = 2100
				CarY = -1000
				Trash1X = 2000
				Trash1Y = 200
				Trash2X = 2000
				Trash2Y = 430
			if NewCar == 11:
				Trash1X = 1900
				Trash1Y = 200
				CarX = 2000
				CarY = 2000
			if NewCar == 12:
				Trash1X = 1900
				Trash1Y = 340
				CarX = 2000
				CarY = 2000
			if NewCar == 13:
				Trash1X = 1900
				Trash1Y = 460
				CarX = 2000
				CarY = 2000
			if NewCar == 14:
				Trash2X = 1900
				Trash2Y = 195
				CarX = 2000
				CarY = 2000
			if NewCar == 15:
				Trash2X = 1900
				Trash2Y = 328
				CarX = 2000
				CarY = 2000
			if NewCar == 16:
				Trash2X = 1900
				Trash2Y = 430
				CarX = 2000
				CarY = 2000
			if NewCar == 17:
				CarX = 2100
				CarY = -1000
				Trash1X = 2000
				Trash1Y = 460
				Trash2X = 2000
				Trash2Y = 195
				MeatX = 1800
				MeatY = 444
			if NewCar == 18:
				CarX = 2100
				CarY = -1000
				Trash1X = 2000
				Trash1Y = 340
				Trash2X = 1900
				Trash2Y = 430
		if CarX <= 300 and y == 430 and CarY == 460:
			dif = 4
			score_value -= 15
			if action == 1:
				health_value -= 1
			elif action == 2:
				health_value -= 2
			NewCar = random.randint(1, 18)
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
			if NewCar == 2:
				CarX = 6000
				CarY = 330
				MeatX = 5000
				MeatY = 580
				WedgyX = 1700
				WedgyY = 320
			if NewCar == 3:
				CarX = 7000
				CarY = 460
				MeatX = 3000
				MeatY = 444
			if NewCar == 4:
				CarX = 5500
				CarY = 200
				Trash1X = 5500
				Trash1Y = 460
			if NewCar == 5:
				CarX = 7000
				CarY = 460
				Trash2X = 5500
				Trash2Y = 328
			if NewCar == 6:
				CarX = 7000
				CarY = 460
				Trash2X = 5500
				Trash2Y = 328
				MeatX = 5000
				MeatY = 444
			if NewCar == 7:
				CarX = 3000
				CarY = 330
				Trash1X = 2000
				Trash1Y = 200
				Trash2X = 2000
				Trash2Y = 328
			if NewCar == 8:
				CarX = 3000
				CarY = 330
				Trash1X = 2000
				Trash1Y = 460
				Trash2X = 2000
				Trash2Y = 195
			if NewCar == 9:
				CarX = 2100
				CarY = -1000
				Trash1X = 2000
				Trash1Y = 460
				Trash2X = 2000
				Trash2Y = 195
				WedgyX = 1700
				WedgyY = 444
			if NewCar == 10:
				CarX = 2100
				CarY = -1000
				Trash1X = 2000
				Trash1Y = 200
				Trash2X = 2000
				Trash2Y = 430
			if NewCar == 11:
				Trash1X = 1900
				Trash1Y = 200
				CarX = 2000
				CarY = 2000
			if NewCar == 12:
				Trash1X = 1900
				Trash1Y = 340
				CarX = 2000
				CarY = 2000
			if NewCar == 13:
				Trash1X = 1900
				Trash1Y = 460
				CarX = 2000
				CarY = 2000
			if NewCar == 14:
				Trash2X = 1900
				Trash2Y = 195
				CarX = 2000
				CarY = 2000
			if NewCar == 15:
				Trash2X = 1900
				Trash2Y = 328
				CarX = 2000
				CarY = 2000
			if NewCar == 16:
				Trash2X = 1900
				Trash2Y = 430
				CarX = 2000
				CarY = 2000
			if NewCar == 17:
				CarX = 2100
				CarY = -1000
				Trash1X = 2000
				Trash1Y = 460
				Trash2X = 2000
				Trash2Y = 195
				MeatX = 1800
				MeatY = 444
			if NewCar == 18:
				CarX = 2100
				CarY = -1000
				Trash1X = 2000
				Trash1Y = 340
				Trash2X = 1900
				Trash2Y = 430

		#Devin sprite touched
		if WedgyX <= 400 and y == 170 and WedgyY == 186 and action == 2:
			WedgyY = -1000
			dif += 5
			score_value += 10
			health_value += 1
		if WedgyX <= 400 and y == 300 and WedgyY == 320 and action == 2:
			WedgyY = -1000
			dif += 5
			score_value += 10
			health_value += 1
		if WedgyX <= 400 and y == 430 and WedgyY == 444 and action == 2:
			WedgyY = -1000
			dif += 5
			score_value += 10
			health_value += 1


		if WedgyX <= 400 and y == 170 and WedgyY == 186 and action == 1:
			WedgyY = -1000
			dif = 4
			score_value -= 10
			health_value -= 1
		if WedgyX <= 400 and y == 300 and WedgyY == 320 and action == 1:
			WedgyY = -1000
			dif = 4
			score_value -= 10
			health_value += -1
		if WedgyX <= 400 and y == 430 and WedgyY == 444 and action == 1:
			WedgyY = -1000
			dif = 4
			score_value -= 10
			health_value -= 1



		#If touching Trash1 (The pile of cement so then it respawns and moves the the background again so its not plain and boring)
		if Trash1X <= 400 and y == 170 and Trash1Y == 200:
			Trash1Y = -250
			dif = 4
			if action == 1:
				health_value -= 1
			elif action == 2:
				health_value -= 2
		if Trash1X <= 400 and y == 300 and Trash1Y == 340:
			Trash1Y = -250
			dif = 4
			if action == 1:
				health_value -= 1
			elif action == 2:
				health_value -= 2
		if Trash1X <= 400 and y == 430 and Trash1Y == 460:
			Trash1Y = -250
			dif = 4
			if action == 1:
				health_value -= 1
			elif action == 2:
				health_value -= 2

		#If touching Trash2 (The alcohol pile)
		if Trash2X <= 400 and y == 170 and Trash2Y == 195:
			Trash2Y = -250
			dif = 4
			if action == 1:
				health_value -= 1
			elif action == 2:
				health_value -= 2
		if Trash2X <= 400 and y == 300 and Trash2Y == 328:
			Trash2Y = -250
			dif = 4
			if action == 1:
				health_value -= 1
			elif action == 2:
				health_value -= 2
		if Trash2X <= 400 and y == 430 and Trash2Y == 430:
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
		screen.blit(SeanGraffiti, (sgX, sgY))
		screen.blit(SewerTunnel, (TunnelX, TunnelY))
		screen.blit(SewerLadder, (LadderX, LadderY))
		screen.blit(SewerPipe2, (Pipe2X, Pipe2Y))
		screen.blit(SewerPipe, (Pipe1X, Pipe1Y))
		screen.blit(FrontBarrels, (BarrelX, BarrelY))
		screen.blit(Trash2, (Trash2X, Trash2Y))
		screen.blit(Trash1, (Trash1X, Trash1Y))
		screen.blit(RottenMeat, (RottenMeatX, RottenMeatY))
		screen.blit(GoWeegyGo, (WedgyX, WedgyY))
		screen.blit(HalfaCar, (CarX, CarY))
		screen.blit(Barba, (BarbaX, BarbaY))
		screen.blit(Coin, (COINMOVEX, COINMOVEY))
		screen.blit(Meat, (MeatX, MeatY))
		screen.blit(animation_list[action][frame], (x, y))
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
		
			
			if event.type == pygame.QUIT:
				run = False

		show_score(textX, textY)
		show_health(textXX, textYY)
		pygame.display.update()

pygame.quit()