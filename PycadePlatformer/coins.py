import pygame
from settings import *

class Coin(pygame.sprite.Sprite):
    def __init__(self, pos, size, value):
        super().__init__()

        self.value = value #amount of currency per coin
        self.size = size #size of coin
        
        self.image = pygame.Surface((size, size))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect(topleft = pos)


    def update(self, x_shift):
        self.rect.x += x_shift
