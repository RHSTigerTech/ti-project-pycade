import pygame
#import classes
from settings import *

class Projectile(pygame.sprite.Sprite):
    def __init__(self, pos, type, direction, speed):
        super().__init__()

        #turn inputed values into interal variables
        self.type = type
        self.direction = pygame.math.Vector2(0,0)
        self.speed = speed

        self.direction.x = direction

        
        #placeholders
        self.cooldown = 0
        self.image = 0
        self.lifespan = 0

        #projectile selector
        if type == 'peely':
            self.image = pygame.image.load('peely_bullet.png')
            self.cooldown = 0
            self.lifespan = 100
        elif type == 'plunger':
            self.image = pygame.image.load('plunger_right.png')
            self.cooldown = 10
            self.lifespan = 1000
        else: #Backup image incase of error
            self.image = pygame.image.load('num_zero.png').convert_alpha()

        #hitbox maker
        self.rect = self.image.get_rect(topleft = pos)

    #update pos based on level scroll
    def update(self, x_shift):
        self.rect.x += x_shift

        if self.type == 'plunger':
            if self.direction.x > 0:
                self.image = pygame.image.load('plunger_right.png').convert_alpha()
            elif self.direction.x < 0:
                self.image = pygame.image.load('plunger_left.png').convert_alpha()
            self.lifespan = 1000
        elif self.lifespan > 0:
            self.lifespan -= 1
        if self.cooldown >= 0:
            self.cooldown -= 1