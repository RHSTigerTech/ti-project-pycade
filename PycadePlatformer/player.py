import pygame, sys
from settings import *

PINK = 255, 8, 255

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.image = pygame.Surface((32, 64))
        self.image.fill(PINK)
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
        if self.keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif self.keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
        if self.keys[pygame.K_SPACE]:
            self.jump()
            
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        
    def get_coin_count(self):
        return self.coin_count
    
    def jump(self):
        self.direction.y = self.jump_speed
