import pygame, random, math, os
import Crocodile2

# from pygame import mixer

pygame.init()

#redirects file finder to folder
os.chdir('Crocketdile_images')

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
HalfaCar = pygame.image.load("halfAcar.png")
GoWeegyGo = pygame.image.load("Wedgysavehim.png")
Heart = pygame.image.load("heart.png")
Barba = pygame.image.load("barberCoin.png")

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
COINMOVEY = 400
COINMOVEX = 1800
MeatX = 1000
MeatY = 900
Trash1X = 1000
Trash1Y = -2000
Trash2X = 1000
Trash2Y = -305
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
CarX = 100
CarY = 80200
WedgyX = 1500
WedgyY = -666
HeartX = -100
HeartY = -40
BarbaX = 10
BarbaY = 10


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
		CarX -= dif
		Trash1X -= dif
		Trash2X -= dif
		WedgyX -= dif


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
		
		if CarX <= -250:
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
				
		#Health Cap
		if health_value > 5:
			health_value = 5

		
		#If meat goes off screen
		if MeatX <= -150:
			MeatY = -100

		if Trash1X <= -170:
			Trash1Y = -900

		if Trash2X <= -240:
			Trash2Y = -900


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
		
		#If Meat Touches
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

		#If Car is Touched
		if CarX <= 300 and y == 170 and CarY == 200:
			dif = 4
			score_value -= 15
			if action == 1:
				health_value -= 1
			elif action == 2:
				health_value -= 3
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
				health_value -= 3
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
				health_value -= 3
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



		#If touching Trash1 (The pile of cement stuff)
		if Trash1X <= 400 and y == 170 and Trash1Y == 200:
			Trash1Y = -250
			dif = 4
			if action == 1:
				health_value -= 1
			elif action == 2:
				health_value -= 3
		if Trash1X <= 400 and y == 300 and Trash1Y == 340:
			Trash1Y = -250
			dif = 4
			if action == 1:
				health_value -= 1
			elif action == 2:
				health_value -= 3
		if Trash1X <= 400 and y == 430 and Trash1Y == 460:
			Trash1Y = -250
			dif = 4
			if action == 1:
				health_value -= 1
			elif action == 2:
				health_value -= 3

		#If touching Trash2 (The alcohol pile)
		if Trash2X <= 400 and y == 170 and Trash2Y == 195:
			Trash2Y = -250
			dif = 4
			if action == 1:
				health_value -= 1
			elif action == 2:
				health_value -= 3
		if Trash2X <= 400 and y == 300 and Trash2Y == 328:
			Trash2Y = -250
			dif = 4
			if action == 1:
				health_value -= 1
			elif action == 2:
				health_value -= 3
		if Trash2X <= 400 and y == 430 and Trash2Y == 430:
			Trash2Y = -250
			dif = 4
			if action == 1:
				health_value -= 1
			elif action == 2:
				health_value -= 3


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
		screen.blit(GoWeegyGo, (WedgyX, WedgyY))
		screen.blit(HalfaCar, (CarX, CarY))
		screen.blit(Barba, (BarbaX, BarbaY))
		screen.blit(Coin, (COINMOVEX, COINMOVEY))
		screen.blit(Meat, (MeatX, MeatY))
		screen.blit(animation_list[action][frame], (x, y))
		screen.blit(Heart, (HeartX, HeartY))


		if health_value <= 0:
			dif = 0
			scroll = 0
			bg = pygame.image.load('gameOver_screen.jpg').convert()
			bg_width = bg.get_width()


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




		#event handler and Crockettdile Movement
		for event in pygame.event.get():
			keys = pygame.key.get_pressed()
			if keys[pygame.K_w]:
				y -= 65
			if keys[pygame.K_s]:
				y += 65

			#eating motion
			if keys[pygame.K_SPACE]:
				# print('space')
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