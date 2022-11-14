import pygame
from settings import *

class Projectile(pygame.sprite.Sprite):
    def __init__(self, pos, type, direction, speed):
        super().__init__()
        self.type = type
        self.direction = direction

        self.image = 0
        self.speed = speed

        #projectile selector
        if type == 'peely':
            self.image = pygame.image.load('peely_bullet.png')
        else:
            self.image = pygame.image.load('num_zero.png')

        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        self.rect.x += x_shift