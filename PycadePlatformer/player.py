import pygame, sys
from settings import *

PINK = 255, 8, 255

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.image = pygame.image.load('chad_idle_front.png')

        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2(0,0)
        self.can_jump = False
        self.jump_speed = -16
        self.speed = 8
        self.gravity = 0.8

        self.coin_count = 0

    def key_input(self):
        self.keys = pygame.key.get_pressed()

        # if self.can_jump == False:
        if self.keys[pygame.K_d]:
            self.direction.x = 1
            self.image = pygame.image.load('chad_idle_front.png')
        elif self.keys[pygame.K_a]:
            self.direction.x = -1
            self.image = pygame.image.load('chad_idle_back.png')
        else:
            self.direction.x = 0
        if self.keys[pygame.K_SPACE]:
            self.jump()
            self.image = pygame.image.load('chad_jumping_front.png')
            
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        
    def get_coin_count(self):
        coins = str(self.coin_count)

        while len(coins) < 3:
            coins = '0' + coins

        return coins
    
    def jump(self):
        self.direction.y = self.jump_speed
