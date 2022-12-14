import pygame
from settings import *

class Popup(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        super().__init__()

        self.pos = pos
        self.type = type

        #load correct image
        img = ''

        # pygame.font.__init__('arial')
        self.font = pygame.font.Font('freesansbold.ttf', 50)

        if type == 'logo':
            img = 'logo.png'
            self.image = pygame.image.load(img).convert_alpha()
        elif type == 'shop_bg':
            img = 'e-phone.png'
            self.image = pygame.image.load(img).convert_alpha()
        elif type == 'coin':
            img = 'mega_coin.png'
            self.image = pygame.image.load(img).convert_alpha()
        elif type == 'slot1':
            self.image = self.font.render('Extra Health', True, (255, 255, 255))
        elif type == 'slot2':
            self.image = self.font.render('Extra Life', True, (255, 255, 255))
        elif type == 'slot3':
            self.image = self.font.render('Plunger Powerup', True, (255, 255, 255))
        elif type == 'slot4':
            self.image = self.font.render('Extra Score', True, (255, 255, 255))
            

        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        self.rect.x += x_shift