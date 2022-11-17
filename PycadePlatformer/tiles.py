import pygame
from settings import *

#variables

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, lev_type, tile_type):
        super().__init__()

        self.type = tile_type
        self.image = self.image = pygame.Surface((size, size))
        
        #determine ground tile texture:
        if lev_type == 'Grass':
            if tile_type == 'ground':
                self.image = pygame.image.load('ground_dirt.png')
            elif tile_type == 'top':
                self.image = pygame.image.load('groundtop_dirt.png')
            elif tile_type == 'bridge':
                self.image = pygame.image.load('bridge.png')

        #non-level dependant tiles
        else:
            if tile_type == '0':
                self.image = pygame.Surface((size, size))
                self.image.fill(RED)
            
            else:
                self.image = pygame.Surface((size, size))
                self.image.fill(RED)
            
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        self.rect.x += x_shift

        