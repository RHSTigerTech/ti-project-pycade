import pygame

#variables
GROUND = 74, 170, 189

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        
        self.image = pygame.Surface((size, size))
        self.image.fill(GROUND)
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        self.rect.x = self.rect.x + x_shift

        