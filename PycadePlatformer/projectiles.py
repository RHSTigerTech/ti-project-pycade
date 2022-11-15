import pygame
#import classes
from settings import *

class Projectile(pygame.sprite.Sprite):
    def __init__(self, pos, type, direction, speed):
        super().__init__()

        #turn inputed values into interal variables
        self.type = type
        self.direction = direction
        self.speed = speed

        #placeholder for image variable
        self.image = 0

        #projectile selector
        if type == 'peely':
            self.image = pygame.image.load('peely_bullet.png')
        else: #Backup image incase of error
            self.image = pygame.image.load('num_zero.png')

        #hitbox maker
        self.rect = self.image.get_rect(topleft = pos)

    #update pos based on level scroll
    def update(self, x_shift):
        self.rect.x += x_shift