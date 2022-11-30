import pygame
from settings import *

class Popup(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        super().__init__()

        self.pos = pos
        self.type = type

        #load correct image
        img = ''

        if type == 'logo':
            img = 'logo.png'
        else:
            img = 'num_zero.png'

        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        self.rect.x += x_shift