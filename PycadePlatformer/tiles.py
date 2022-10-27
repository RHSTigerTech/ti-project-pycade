import pygame

#variables
GROUND = 74, 170, 189

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, lev_type, tile_type):
        super().__init__()
        
        #determine ground tile texture:
        if lev_type == 'Grass':
            self.image = pygame.image.load('ground_dirt.png')
            self.rect = self.image.get_rect(topleft = pos)
            if tile_type == 'top':
                self.image = pygame.image.load('groundtop_dirt.png')
                self.rect = self.image.get_rect(topleft = pos)
        else:
            self.image = pygame.Surface((size, size))
            self.image.fill(GROUND)
            self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        self.rect.x += x_shift

        