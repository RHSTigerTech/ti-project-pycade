import pygame
from settings import *

class Ingame_Menu(pygame.sprite.Sprite):
    def __init__(self, pos, text, size, title):
        super().__init__()

        self.title = title
        self.text = text
        self.pos = pos
        

        self.load_file(self.text, self.pos)

    def update(self, coin_count):
        coins = coin_count
        if self.title == 'coin_val100':
            self.text = coins[2]
        if self.title == 'coin_val10':
            self.text = coins[1]
        if self.title == 'coin_val1':
            self.text = coins[0]
        else:
            self.text = '4'

        self.load_file(self.text, self.pos)
        
    def load_file(self, text, pos):
        if text == '0':
            file = 'num_zero.png'
        elif text == '1':
            file = 'num_one.png'
        elif text == '2':
            file = 'num_two.png'
        elif text == '3':
            file = 'num_three.png'
        elif text == '4':
            file = 'num_four.png'
        elif text == '5':
            file = 'num_five.png'
        elif text == '6':
            file = 'num_six.png'
        elif text == '7':
            file = 'num_seven.png'
        elif text == '8':
            file = 'num_eight.png'
        elif text == '9':
            file = 'num_nine.png'
        elif text == 'coin':
            file = 'base_coin.png'
        else:
            file = 'num_three.png'


        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect(topleft = pos)