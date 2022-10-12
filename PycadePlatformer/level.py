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

    def run(self):
        self.player_sprite.move()

        self.tiles.update(self.world_shift)
        self.player.update()

        self.tiles.draw(self.displaysurface)
        self.player.draw(self.displaysurface)
