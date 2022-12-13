import pygame, sys
from settings import *
from projectiles import Projectile

PINK = 255, 8, 255
CHADWALKRIGHT = ('chad_right_walk1.png', 'chad_right_walk2.png', 'chad_right_walk3.png', 'chad_idle_front.png')
BASEHEALTH = 3
class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.image = pygame.image.load('chad_idle_front.png')
        self.image_name = 'chad_idle_front'

        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2(0,0)
        self.can_jump = False
        self.crouching = False
        self.i_frame = False
        self.jump_speed = -28
        self.speed = PLAYERSPEED
        self.gravity = 3
        self.health = BASEHEALTH
        self.falling = False
        self.attack_cooldown = 20

        self.status = 'chad' #powerup status
        self.shield = 0 #extra health
        self.plunger = False

        self.coin_count = 0
        #counters
        self.step = 0
        self.i_frame_count = 0

    def key_input(self):
        self.keys = pygame.key.get_pressed()

        if self.keys[pygame.K_d]:
            self.direction.x = 1
            self.player_animate()
        elif self.keys[pygame.K_a]:
            self.direction.x = -1
            self.player_animate()
        else:
            self.direction.x = 0
            self.step = 0
        if self.keys[pygame.K_SPACE]:
            if self.crouching == True:
                pass
            elif self.falling == False:
                self.jump()
                self.image = pygame.image.load('chad_jumping_front.png').convert_alpha()
                self.image_name = 'chad_front'
        elif self.keys[pygame.K_s] and self.direction.y == 0:
            if self.crouching == False:
                self.crouching = True
                self.crouch()
            else:
                self.crouching = False
                self.crouch()

        if self.keys[pygame.K_e] and self.crouching == False and self.status == 'plunger':
            self.attack_cooldown -= 1
            # print(self.attack_cooldown)
        #perform an attack when e isn't pressed
        elif self.attack_cooldown < 0:
            self.plunger = True
            self.attack_cooldown = 20 #or maximum cooldown
        else:
            self.attack_cooldown = 20 #or maximum cooldown

    def player_animate(self):
        #set variables
        direct = ""
        #direction check
        if self.direction.x > 0:
            direct = 'right'
        elif self.direction.x < 0:
            direct = 'left'

        # walking animation - right
        if direct == 'right':
            if self.step == 0:
                self.image = pygame.image.load('chad_idle_front.png').convert_alpha()
            elif self.step == 1:
                self.image = pygame.image.load('chad_walk1_right.png').convert_alpha()
            elif self.step == 2:
                self.image = pygame.image.load('chad_walk2_right.png').convert_alpha()
            elif self.step == 3:
                self.image = pygame.image.load('chad_walk3_right.png').convert_alpha()
            elif self.step == 4:
                self.image = pygame.image.load('chad_walk4_right.png').convert_alpha()
            elif self.step == 5:
                self.image = pygame.image.load('chad_walk5_right.png').convert_alpha()
                self.step = 0
        if direct == 'left':
            if self.step == 0:
                self.image = pygame.image.load('chad_idle_front.png').convert_alpha()
            elif self.step == 1:
                self.image = pygame.image.load('chad_walk1_back.png').convert_alpha()
            elif self.step == 2:
                self.image = pygame.image.load('chad_walk2_back.png').convert_alpha()
            elif self.step == 3:
                self.image = pygame.image.load('chad_walk3_back.png').convert_alpha()
            elif self.step == 4:
                self.image = pygame.image.load('chad_walk4_back.png').convert_alpha()
            elif self.step == 5:
                self.image = pygame.image.load('chad_walk5_back.png').convert_alpha()
                self.step = 0
        self.step += 1

        # change image
        # if self.crouching == True:
        #     if direct == 'right':
        #         self.image = pygame.image.load('chad_crouch_front.png').convert_alpha()
        #         self.image_name = 'chad_crouch_front'
        #     else:        
        #         self.image = pygame.image.load('chad_crouch_front.png').convert_alpha()
        #         self.image_name = 'chad_crouch_front'
        # else:
        #     if direct == 'right':
        #         self.image = pygame.image.load('chad_idle_front.png').convert_alpha()
        #         self.image_name = 'chad_front'
        #     else:        
        #         self.image = pygame.image.load('chad_idle_back.png').convert_alpha()
        #         self.image_name = 'chad_back'

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
        if self.attack_cooldown < 0:
            coins = coins + '4'
        elif self.attack_cooldown < 5:
            coins = coins + '3'
        elif self.attack_cooldown < 10:
            coins = coins + '2'
        elif self.attack_cooldown < 15:
            coins = coins + '1'
        elif self.attack_cooldown < 20:
            coins = coins + '0'
        else:
            coins = coins + '0'
        return coins

    def jump(self):
        self.direction.y = self.jump_speed
        self.falling = True

    def damage(self, amount):
        if self.i_frame == False:
            self.health -= amount
            self.i_frame_count = 30
            self.i_frame = True

    def powerup(self, power):
        if power =='plunger':
            self.shield = 2
            self.status = 'plunger'
        elif power == 'heart':
            self.health += 1

    def immune(self):
        
        if self.i_frame_count == 0:
            self.i_frame = False
        else:
            self.i_frame_count -= 1