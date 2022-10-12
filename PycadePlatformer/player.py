import pygame, sys
from settings import *

PINK = 255, 8, 255

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.image = pygame.Surface((64, 64))
        self.image.fill(PINK)
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2(0,0)
        self.can_jump = False
        self.jump_speed = -16
        self.speed = 16

    def move(self):
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if self.jump == False:
                if keys[pygame.K_RIGHT]:
                    self.direction.x = 1
                elif keys[pygame.K_LEFT]:
                    self.direction.x = -1
                else:
                    self.direction.x = 0
                if keys[pygame.K_SPACE]:
                    self.can_jump = False

            if event.type == pygame.QUIT:
                sys.exit()
            

    def update(self):
        self.rect.x += self.direction * self.speed

    def jump(self):
        self.direction.y = self.jump_speed
        pass
