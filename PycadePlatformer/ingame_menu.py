import pygame
#import classes
from settings import *

class Ingame_Menu(pygame.sprite.Sprite):
    def __init__(self, pos, text, size, title):
        super().__init__()
 
        #turn inputed values into interal variables
        self.title = title
        self.text = text
        self.pos = pos

        slot = ''

        #assign slots
        if self.title == 'coin_val100':
            slot = 'coins'
        if self.title == 'coin_val10':
            slot = 'coins'
        if self.title == 'coin_val1':
            slot = 'coins'
        if self.title == 'charge_0':
            slot = 'charge'
        elif self.title == 'charge_1':
            slot = 'charge'
        elif self.title == 'charge_2':
            slot = 'charge'
        elif self.title == 'charge_3':
            slot = 'charge'
        elif self.title == 'charge_4':
            slot = 'charge'
        
        
        #find the right file for the right space
        self.load_file(self.text, self.pos, slot)

    #update the menu
    def update(self, coin_count):
        coins = coin_count
        slot = ''
        #set spacing on each value
        if self.title == 'coin_val100':
            self.text = coins[0]
            slot = 'coins'
        if self.title == 'coin_val10':
            self.text = coins[1]
            slot = 'coins'
        if self.title == 'coin_val1':
            self.text = coins[2]
            slot = 'coins'
        if self.title == 'charge_0':
            self.text = coins[3]
            slot = 'charge'
        if self.title == 'charge_1':
            self.text = coins[3]
            slot = 'charge'
        if self.title == 'charge_2':
            self.text = coins[3]
            slot = 'charge'
        if self.title == 'charge_3':
            self.text = coins[3]
            slot = 'charge'
        if self.title == 'charge_4':
            self.text = coins[3]
            slot = 'charge'

        #find the file for the new values
        self.load_file(self.text, self.pos, slot)
        
    def load_file(self, text, pos, slot):
        if slot == 'coins':
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
        elif slot == 'charge':
            if text == '0':
                file = 'charge_meter_0.png'
            elif text == '1':
                file = 'charge_meter_1.png'
            elif text == '2':
                file = 'charge_meter_2.png'
            elif text == '3':
                file = 'charge_meter_3.png'
            elif text == '4':
                file = 'charge_meter_4.png'
        elif text == 'coin':
            file = 'base_coin.png'
        else: #Backup error file
            file = 'num_three.png'

        #set image and hitbox to selected file
        self.image = pygame.image.load(file).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)