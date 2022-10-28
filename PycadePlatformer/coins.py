import pygame
from settings import *

class Coin(pygame.sprite.Sprite):
    def __init__(self, pos, size, value):
        super().__init__()

        self.value = value #amount of currency per coin
        self.size = size #size of coin

        #change pos to a list, then offset coin to middle of tile
        self.pos = [pos[0], pos[1]]
        self.pos[0] += 16
        self.pos[1] += 16
        
        if str(self.value) == '1':
            self.image = pygame.image.load('single_coin.png')
        elif str(self.value) == '10':
            self.image = pygame.image.load('mega_coin.png')
            self.pos = pos
        else:
            self.image = pygame.image.load('omega_coin.png')

        self.rect = self.image.get_rect(topleft = self.pos)


    def update(self, x_shift):
        self.rect.x += x_shift
