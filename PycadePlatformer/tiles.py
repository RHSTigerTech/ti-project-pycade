import pygame

#variables
GROUND = 74, 170, 189

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, lev_type, tile_type):
        super().__init__()

        self.type = tile_type
        
        #determine ground tile texture:
        if lev_type == 'Grass':
            if tile_type == 'ground':
                self.image = pygame.image.load('ground_dirt.png')
            elif tile_type == 'top':
                self.image = pygame.image.load('groundtop_dirt.png')

        #non-level dependant tiles
        if tile_type == 'death_tile':
            self.image = pygame.Surface((size, size))
            self.image.fill(GROUND)
        else:
            self.image = pygame.Surface((size, size))
            self.image.fill(GROUND)
            
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        self.rect.x += x_shift

        