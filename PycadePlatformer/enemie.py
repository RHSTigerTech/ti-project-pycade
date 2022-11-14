import pygame
from settings import *
from projectiles import Projectile

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        super().__init__()

        self.type = type
        self.pos = [pos[0], pos[1]]
        self.direction = pygame.math.Vector2(0,0)
        self.direction.x = -1

        self.gravity = 0.8
        self.max_attack_cooldown = 0

        self.bullets = pygame.sprite.Group()

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
            self.max_attack_cooldown = 25
        else:
            self.image = pygame.image.load('num_zero.png')

        self.attack_cooldown = self.max_attack_cooldown


        self.rect = self.image.get_rect(topleft = self.pos)

    def update(self, x_shift):
        self.rect.x += x_shift


    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
    
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






        # bullet = Projectile(self.pos, 'peely', self.direction.x)
        # self.bullets.add(bullet)