import pygame, os, sys, random
from picture import Picture, QUOTES

pygame.font.init()
 
#redirect to image folder:
os.chdir('Arcade_Project_Images')

#set base size of window:
SCREENWIDTH = 1200
SCREENHEIGHT = 768
size = SCREENWIDTH, SCREENHEIGHT

SCREEN = pygame.display.set_mode(size)

#variables:
bg_color1 = (1,5,32)



#add images to menu:
menu = pygame.sprite.Group()

message = random.choice(QUOTES)


img_list = [
    ('title.jpeg', (600,100)),
    ('box.jpeg', (600,240)),
    (message, (600,240)),
    ('Crocketdile4.jpg', (600, 800)),
    ('chads_quest_small.png', (300,800))
]
for i in img_list:
    item = Picture(i[0], i[1])
    menu.add(item)

    menu.add()

#main loop for menu:
def main():
    SCREEN.fill(bg_color1)

    #quit the game
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            sys.exit()
    
    for pic in menu.sprites():
        pic.animate()

    #update the screen textures
    menu.draw(SCREEN)
    # quotes()
    pygame.display.update() 

while True:
    main()