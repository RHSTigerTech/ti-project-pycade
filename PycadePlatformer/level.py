import pygame
#import classes
from settings import *
from tiles import Tile
from enemie import Enemy
from coins import Coin
from ingame_menu import Ingame_Menu
from player import Player
from enemie import Enemy
from projectiles import Projectile

class Level:
    def __init__(self, leveldata, surface):
        #set up all variables
        self.displaysurface = surface
        self.leveldata = leveldata
        self.world_shift = -8
        
        #placeholders
        self.plunger = 0
        self.player_sprite = 0

    #draw the upper screen menu
    def setupMenu(self):
        self.menu = pygame.sprite.Group()
        #the layout of the menu
        user_menu = [
            ((4 ,4), 'coin', 32, 'coin'),
            ((36 ,4), '0', 32, 'coin_val100'),
            ((68,4), '0', 32, 'coin_val10'),
            ((100,4), '0', 32, 'coin_val1'),
            ((136, 4), '0', 32, 'charge_0')
        ]
        #add all values to group

        for digit in user_menu:
            menu_piece = Ingame_Menu(digit[0], digit[1], digit[2], digit[3])
            self.menu.add(menu_piece)

    #setup a level
    def setupLevel(self, layout, lev_type):
    #variables
        #Groups
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.mobs = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        #offseting the y value because [0] is first value
        tileYCount = -1
        #setup upper menu
        self.setupMenu()

        #turns strings in list into cells on the level
        for row in layout:
            tileXCount = -1
            tileYCount += 1
            for cell in row:
                tileXCount += 1
                #multiplys pos by tilesize to get proper grid
                x = tileXCount * tilesize
                y = tileYCount * tilesize
                #puts proper objects in tile spaces based on a value
                if cell == "X":
                    tile = Tile((x,y), tilesize, lev_type, "ground")
                    self.tiles.add(tile)
                elif cell == "x":
                    tile = Tile((x,y), tilesize, lev_type, "top")
                    self.tiles.add(tile)
                elif cell == 'b':
                    tile = Tile((x,y), tilesize, lev_type, "bridge")
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
                elif cell == 'p':
                    coin = Coin((x,y), 64, 'plunger')
                    self.items.add(coin)
                elif cell == "P":
                    self.player_sprite = Player((x,y))
                    self.player.add(self.player_sprite)
                elif cell == 'S':
                    mob = Enemy((x,y), 'S3AN')
                    self.mobs.add(mob)
                elif cell == 'w':
                    mob = Enemy((x,y), 'weegy')
                    self.mobs.add(mob)
                elif cell == '0':
                    tile = Tile((x,y + 64), tilesize, lev_type, '0')
                    self.tiles.add(tile)

    #level scroll
    def scroll(self):
        #shortened down variables
        player = self.player_sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player.health > 0: #if player isn't dead
            #if player is near edge, scroll screen instead of move player
            if player_x < 350 and direction_x < 0:
                self.world_shift = 8
                player.speed = 0
            elif player_x > 850 and direction_x > 0:
                self.world_shift = -8
                player.speed = 0
            else: #player moves, not scroll
                self.world_shift = 0
                if player.falling == False:
                    player.speed = 8
                elif player.direction.y < 0:
                    player.speed = 6
    #check for horizontal collisions       
    def horizontal_movement_collisions(self):
        player = self.player_sprite
        if player.health > 0:
            player.rect.x += player.direction.x * player.speed
        for mob in self.mobs.sprites():
                mob.rect.x += mob.direction.x * mob.speed
            
        
        #Player vs Tiles
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if sprite.type == '0':
                    player.health = 0
                    self.player.remove(player)    
                elif player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.direction.x = 0
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.direction.x = 0
                
        #Mobs vs Tiles
        for sprite_mob in self.mobs.sprites():
            for sprite in self.tiles.sprites():
                if sprite.rect.colliderect(sprite_mob.rect):
                    if sprite_mob.direction.x < 0:
                        sprite_mob.rect.left = sprite.rect.right
                        sprite_mob.direction.x = 1      
                    elif sprite_mob.direction.x > 0:
                        sprite_mob.rect.right = sprite.rect.left
                        sprite_mob.direction.x = -1

        #Player vs Mobs - Death
        for mob in self.mobs.sprites():
            if player.rect.colliderect(mob):
                player.damage(1)
        
        #player vs Plunger
        for bullet in self.bullets.sprites():
            if player.rect.colliderect(bullet.rect) and bullet.cooldown < 0:
                if bullet.type == 'plunger':
                    if player.direction.x < 0:
                        player.rect.left = bullet.rect.right
                        player.direction.x = 0     
                    elif player.direction.x > 0:
                        player.rect.right = bullet.rect.left
                        player.direction.x = 0
    #check for vertical collisions                
    def vertical_movement_collisions(self):
        player = self.player_sprite
        self.player_sprite.apply_gravity()
        for mob in self.mobs.sprites():
            mob.apply_gravity()

        #Player vs Tiles - No death
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if sprite.type == '0':
                    player.health = 0
                    self.player.remove(player)
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                elif player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.falling = False
        #Mob vs Tiles
        for mob in self.mobs.sprites():
            for sprite in self.tiles.sprites():
                if mob.rect.colliderect(sprite):
                    if mob.direction.y < 0:
                        mob.rect.top = sprite.rect.bottom
                        mob.direction.y = 0
                    elif mob.direction.y > 0:
                        mob.rect.bottom = sprite.rect.top
                        mob.direction.y = 0

        #Player Vs Mobs - Killing Mobs/Death
        for mob in self.mobs.sprites():
            
            if player.rect.colliderect(mob):
                #Enemy falls on head
                if player.direction.y <= 0:
                    player.damage(1)
                elif player.direction.y > 0.8:
                    mob.remove(self.mobs)

        #player vs plunger
        for bullet in self.bullets.sprites():
            if player.rect.colliderect(bullet.rect) and bullet.cooldown < 0:
                if bullet.type == 'plunger':
                    if player.direction.y < 0:
                        player.rect.top = bullet.rect.bottom
                        player.direction.y = 0
                    elif player.direction.y > 0:
                        player.rect.bottom = bullet.rect.top
                        player.direction.y = 0
                        player.falling = False
    #check for collecting items
    def item_collisions(self):
        player = self.player_sprite
        #move bullets
        for bullet in self.bullets.sprites():
            
            bullet.rect.x += bullet.direction.x * bullet.speed        
        #coin / powerups
        for sprite in self.items.sprites():
            if sprite.rect.colliderect(player.rect):
                if sprite.value == 'plunger':
                    player.powerup(sprite.value)
                else:
                    self.player_sprite.coin_count += sprite.value
                self.items.remove(sprite)
        #bullets hitting walls
        for bullet in self.bullets.sprites():
            for tile in self.tiles.sprites():
                if bullet.rect.colliderect(tile.rect):
                    if bullet.type != 'plunger':
                        self.bullets.remove(bullet)
                        print('remove bullet')
                    else:

                        if bullet.direction.x < 0:
                            bullet.rect.left = tile.rect.right
                            bullet.direction.x = 0
                        elif bullet.direction.x > 0:
                            bullet.rect.right = tile.rect.left
                            bullet.direction.x = 0
        #bullet hitting player
        for bullet in self.bullets.sprites():
            if bullet.rect.colliderect(player.rect):
                if bullet.type != 'plunger':
                    player.damage(1)
                    self.bullets.remove(bullet)
                    
        #bullet hitting mob
        for mob in self.mobs.sprites():
            for bullet in self.bullets.sprites():
                if bullet.rect.colliderect(mob.rect):
                    if bullet.type == 'plunger':
                        self.mobs.remove(mob)
        
        #bullet hitting coins
        for bullet in self.bullets.sprites():
            for coin in self.items.sprites():
                if bullet.rect.colliderect(coin.rect):
                    if coin.value == 'plunger':
                        player.powerup(coin.value)
                    else:
                        player.coin_count += sprite.value
                    self.items.remove(coin)

    #check for an enemy attack
    def attacks(self):
        player = self.player_sprite
        #add bullets to screen
        for mob in self.mobs.sprites():
            if mob.attack() == True:
                if mob.type == 'weegy':
                    projectile = Projectile((mob.rect.x, mob.rect.y + 25), 'peely', mob.direction.x, 5)
                    self.bullets.add(projectile)
        
        if player.plunger == True:
            player.plunger = False
            for plunger in self.bullets.sprites():
                self.bullets.remove(plunger)
            self.plunger = Projectile((player.rect.x,player.rect.y), 'plunger', player.direction.x, 50)
            if self.plunger.type == 'plunger':
                if player.image_name == 'chad_front':
                    self.plunger.direction.x = 1
                elif player.image_name == 'chad_back':
                    self.plunger.direction.x = -1
            self.bullets.add(self.plunger)

    #run the game    
    def run(self):
        
        #collisions and movement
        self.horizontal_movement_collisions()
        self.player_sprite.key_input()
        self.vertical_movement_collisions()
        self.item_collisions()
        self.scroll()

        #Run Attacks
        self.attacks()
        self.player_sprite.immune()

        #update objects
        self.tiles.update(self.world_shift)
        self.items.update(self.world_shift)
        self.mobs.update(self.world_shift)
        self.bullets.update(self.world_shift)

        #draw the menu
        self.menu.update(self.player_sprite.get_coin_count())
        pygame.draw.rect(self.displaysurface, GREY, ((0,0),(1200,40)))
        self.menu.draw(self.displaysurface)

        #draw everything else
        self.tiles.draw(self.displaysurface)
        self.items.draw(self.displaysurface)
        self.player.draw(self.displaysurface)
        self.mobs.draw(self.displaysurface)
        self.bullets.draw(self.displaysurface)
