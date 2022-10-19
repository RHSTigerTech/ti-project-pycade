import pygame
from settings import *

class Ingame_Menu(pygame.sprite.Sprite):
    def __init__(self, coins, time, lives, score):
        super().__init__()
        self.coins = coins
        self.time = time
        self.lives = lives
        self.score = score
    
        self.coin_image = pygame.image.load('numzero.png')
        self.coin_rect = self.image.get_rect(topleft = 0)