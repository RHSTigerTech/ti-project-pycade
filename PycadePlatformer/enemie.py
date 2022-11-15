import pygame
#import classes
from settings import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        super().__init__()

    #Variables
        #turn inputed values into interal variables
        self.type = type
        self.pos = [pos[0], pos[1]]

        #track enemy direction for movement
        self.direction = pygame.math.Vector2(0,0)
        self.direction.x = -1

        #set rate of gravity
        self.gravity = 0.8

        #for some enemy's to change rate of fire
        self.max_attack_cooldown = 0

        #ememy selector
        if self.type == 'S3AN':
            self.pos = [pos[0] + 16, pos[1]]
            self.image = pygame.image.load('ememy_s3an.png')
            self.pos[1] += 32
            #stats
            self.speed = 1

        elif self.type == 'weegy':
            self.image = pygame.image.load('weegy_gun.png')
            #stats
            self.speed = 0
            self.max_attack_cooldown = 100

        else: #just in case of mis-spelling or error
            self.image = pygame.image.load('num_zero.png')

        #set the attack cooldown to the max, ready for use
        self.attack_cooldown = self.max_attack_cooldown

        #set hitbox of enemy
        self.rect = self.image.get_rect(topleft = self.pos)

    #update position based on level scrolling
    def update(self, x_shift):
        self.rect.x += x_shift

    #applies gravity to enemies that need it
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
    
    #determines if it is time for an ememy to attack w/ attack cooldown
    def attack(self):
        if self.type == 'weegy':
            self.attack_cooldown -= 1
            if self.attack_cooldown == 0:
                self.attack_cooldown = self.max_attack_cooldown
                return True
            else:
                return False
        else:
            return False