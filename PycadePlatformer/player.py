import pygame, sys
from settings import *

PINK = 255, 8, 255
CHADWALKRIGHT = ('chad_right_walk1.png', 'chad_right_walk2.png', 'chad_right_walk3.png', 'chad_idle_front.png')

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.image = pygame.image.load('chad_idle_front.png')

        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2(0,0)
        self.can_jump = False
        self.crouching = False
        self.jump_speed = -16
        self.speed = 8
        self.gravity = 0.8

        self.coin_count = 0
        #counters
        self.walking_count = 0

    def key_input(self):
        self.keys = pygame.key.get_pressed()

        # if self.can_jump == False:
        if self.keys[pygame.K_d]:
            self.direction.x = 1
            self.player_animate()
        elif self.keys[pygame.K_a]:
            self.direction.x = -1
            self.player_animate()
        else:
            self.direction.x = 0
        if self.keys[pygame.K_SPACE]:
            if self.crouching == True:
                pass
            elif self.direction.y == 0:
                self.jump()
                self.image = pygame.image.load('chad_jumping_front.png')
        elif self.keys[pygame.K_s] and self.direction.y == 0:
            if self.crouching == False:
                self.crouching = True
                self.crouch()
            else:
                self.crouching = False
                self.crouch()

    def player_animate(self):
        #set variables
        direct = ""
        #direction check
        if self.direction.x > 0:
            direct = 'right'
        elif self.direction.x < 0:
            direct = 'left'

        # change image
        if self.crouching == True:
            if direct == 'right':
                self.image = pygame.image.load('chad_crouch_front.png')
            else:        
                self.image = pygame.image.load('chad_crouch_front.png')
        else:
            if direct == 'right':
                self.image = pygame.image.load('chad_idle_front.png')
            else:        
                self.image = pygame.image.load('chad_idle_back.png')

    def crouch(self):

        if self.crouching == True:
            self.image = pygame.image.load('chad_crouch_front.png')
            self.rect = self.image.get_rect(topleft = (self.rect.x, self.rect.y + 32))
        else:
            self.image = pygame.image.load('chad_idle_front.png')
            self.rect = self.image.get_rect(topleft = (self.rect.x, self.rect.y - 32))

        #stop crouch
        if self.direction.y != 0:
            self.image = pygame.image.load('chad_idle_front.png')
            self.rect = self.image.get_rect(topleft = (self.rect.x, self.rect.y - 32))    
            
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
