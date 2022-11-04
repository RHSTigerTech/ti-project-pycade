import pygame
from settings import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        super().__init__()

        self.type = type
        self.pos = [pos[0] + 16, pos[1]]
        self.direction = pygame.math.Vector2(0,0)
        self.direction.x = -1
        self.speed = 1

        #ememy selector
        if self.type == 'S3AN':
            self.image = pygame.image.load('ememy_s3an.png')
            self.pos[1] += 32
        else:
            self.image = pygame.image.load('num_zero.png')

        self.rect = self.image.get_rect(topleft = self.pos)
        

    def update(self, x_shift):
        self.rect.x += x_shift
    
    def collide(self):
        print('collide')
        if self.direction.x < 0:
            return 'left'
        elif self.direction.x > 0:
            return 'right'