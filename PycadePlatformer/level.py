import pygame
from tiles import Tile
from settings import tilesize
from player import *

class Level:
    def __init__(self, leveldata, surface):
        self.displaysurface = surface
        self.leveldata = leveldata
        self.world_shift = -5
        self.player_sprite = 0


    def setupLevel(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.Group()
        tileYCount = -1
        for row in layout:
            tileXCount = -1
            tileYCount += 1
            for cell in row:
                tileXCount += 1
                # print(tileXCount)
                x = tileXCount * tilesize
                y = tileYCount * tilesize
                if cell == "X":
                    tile = Tile((x,y), tilesize)
                    self.tiles.add(tile)
                elif cell == "P":
                    self.player_sprite = Player((x,y))
                    self.player.add(self.player_sprite)

    def scroll(self):
        player = self.player_sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < 200 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > 1000 and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 16
            

    def run(self):
        self.player_sprite.apply_gravity()
        self.player_sprite.key_input()

        self.scroll()
        self.tiles.update(self.world_shift)
        self.player.update()

        self.tiles.draw(self.displaysurface)
        self.player.draw(self.displaysurface)
