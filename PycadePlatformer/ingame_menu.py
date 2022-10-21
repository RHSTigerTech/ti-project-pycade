import pygame
from settings import *

class Ingame_Menu(pygame.sprite.Sprite):
    def __init__(self, pos, text, size, file):
        super().__init__()

        self.text = text
        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect(topleft = pos)
