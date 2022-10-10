import pygame
from settings import *

PINK = 255, 8, 255

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.image = pygame.Surface((64, 64))
        self.image.fill(PINK)
        self.rect = self.image.get_rect(topleft = pos)
