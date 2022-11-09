import pygame
from settings import *

class Projectile(pygame.sprite.Sprite):
    def __init__(self, pos, type, direction):
        super().__init__()
        self.type = type
        self.direction = self.direction = pygame.math.Vector2(0,0)
        self.direction.x = -1

        self.image = 0

        #projectile selector
        if type == 'peely':
            self.image = pygame.image.load('peely_bullet.png')
        else:
            self.image = pygame.image.load('num_zero.png')

    def update(self):
        pass