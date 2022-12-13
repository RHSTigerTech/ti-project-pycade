import pygame
from settings import *

#variables

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, lev_type, tile_type):
        super().__init__()

        self.type = tile_type
        self.image = self.image = pygame.Surface((size, size))

        positon = [pos[0], pos[1]]
        
        #determine ground tile texture:
        if lev_type == 'Grass':
            if tile_type == 'ground':
                self.image = pygame.image.load('ground_dirt.png').convert_alpha()
            elif tile_type == 'top':
                self.image = pygame.image.load('groundtop_dirt.png').convert_alpha()
            elif tile_type == 'bridge':
                self.image = pygame.image.load('bridge.png').convert_alpha()
            elif tile_type == 'spike':
                self.image = pygame.image.load('spikes_20x64.png').convert_alpha()
                positon[1] += 44
            elif tile_type == 'stone':
                self.image = pygame.image.load('stone.png').convert_alpha()
            

        #non-level dependant tiles
        if self.image == 0:
            if tile_type == '0':
                self.image = pygame.Surface((size, size))
                self.image.fill(RED)
            else:
                self.image = pygame.Surface((size, size))
                self.image.fill(RED)
        elif self.type == 'crate':
            self.image = pygame.image.load('crate.png').convert_alpha()
        elif self.type == 'half_crate':
            positon[1] += 32
            self.image = pygame.image.load('half_crate.png').convert_alpha()

        #set hitbox
        self.rect = self.image.get_rect(topleft = positon)

    def update(self, x_shift):
        self.rect.x += x_shift

        