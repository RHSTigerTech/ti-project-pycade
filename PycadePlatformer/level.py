import pygame
from tiles import Tile
from settings import tilesize
from player import *

class Level:
    def __init__(self, leveldata, surface):
        self.displaysurface = surface
        self.leveldata = leveldata

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
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)

    def run(self):
        self.tiles.update(10)
        # self.tiles.update(10)
        # self.tiles.update(10)
        self.tiles.draw(self.displaysurface)
        self.player.draw(self.displaysurface)
