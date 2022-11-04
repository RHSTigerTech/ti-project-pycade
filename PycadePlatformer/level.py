import pygame
from tiles import Tile
from enemie import Enemy
from coins import Coin
from ingame_menu import Ingame_Menu
from settings import *
from player import *
from enemie import *
class Level:
    def __init__(self, leveldata, surface):
        self.displaysurface = surface
        self.leveldata = leveldata
        self.world_shift = -8
        self.player_sprite = 0

    def setupMenu(self):
        self.menu = pygame.sprite.Group()
        user_menu = [
            ((4 ,4), 'coin', 32, 'coin'),
            ((36 ,4), '0', 32, 'coin_val100'),
            ((68,4), '0', 32, 'coin_val10'),
            ((100,4), '0', 32, 'coin_val1'),
        ]

        for digit in user_menu:
            menu_piece = Ingame_Menu(digit[0], digit[1], digit[2], digit[3])
            self.menu.add(menu_piece)


    def setupLevel(self, layout, lev_type):
        self.setupMenu()
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.mobs = pygame.sprite.Group()
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
                    tile = Tile((x,y), tilesize, lev_type, "ground")
                    self.tiles.add(tile)
                elif cell == "x":
                    tile = Tile((x,y), tilesize, lev_type, "top")
                    self.tiles.add(tile)
                elif cell == "C":
                    coin = Coin((x,y), 0, 1)
                    self.items.add(coin)
                elif cell == "M":
                    coin = Coin((x,y), 0, 10)
                    self.items.add(coin)
                elif cell == "O":
                    coin = Coin((x,y), 0, 100)
                    self.items.add(coin)
                elif cell == "D":
                    coin = Coin((x - 16,y), 64, 1)
                    self.items.add(coin)
                    coin = Coin((x + 16,y), 64, 1)
                    self.items.add(coin)
                elif cell == "P":
                    self.player_sprite = Player((x,y))
                    self.player.add(self.player_sprite)
                elif cell == 'S':
                    mob = Enemy((x,y), 'S3AN')
                    self.mobs.add(mob)

    def scroll(self):
        player = self.player_sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < 350 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > 850 and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 16
            
    def horizontal_movement_collisions(self):
        player = self.player_sprite
        player.rect.x += player.direction.x * player.speed
        

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):    
                    if player.direction.x < 0:
                        player.rect.left = sprite.rect.right
                        player.direction.x = 0
                    elif player.direction.x > 0:
                        player.rect.right = sprite.rect.left
                        player.direction.x = 0

        for sprite_mob in self.mobs.sprites():
            for sprite in self.tiles.sprites():
                if sprite.rect.colliderect(sprite_mob.rect):
                    if sprite_mob.collide() == 'left':
                        sprite_mob.rect.left = sprite.rect.right
                        sprite_mob.direction.x = 0
                    elif sprite_mob.collide() == 'right':
                        sprite_mob.rect.right = sprite.rect.left
                        sprite_mob.direction.x = 0
                else:
                    sprite_mob.rect.x += sprite_mob.direction.x * sprite_mob.speed
                    pass

    def vertical_movement_collisions(self):
        player = self.player_sprite
        self.player_sprite.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                elif player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
    
    def item_collisions(self):
        player = self.player_sprite

        for sprite in self.items.sprites():
            if sprite.rect.colliderect(player.rect):
                self.player_sprite.coin_count += sprite.value
                self.items.remove(sprite)


    def run(self):
        
        #level

        #player
        self.horizontal_movement_collisions()
        self.player_sprite.key_input()
        self.vertical_movement_collisions()

        self.item_collisions()

        self.scroll()
        self.tiles.update(self.world_shift)
        self.items.update(self.world_shift)
        self.mobs.update(self.world_shift)

        #draw the menu
        self.menu.update(self.player_sprite.get_coin_count())
        pygame.draw.rect(self.displaysurface, GREY, ((0,0),(1200,40)))
        self.menu.draw(self.displaysurface)

        self.tiles.draw(self.displaysurface)
        self.items.draw(self.displaysurface)
        self.player.draw(self.displaysurface)
        self.mobs.draw(self.displaysurface)
