import pygame
from CrocketdileScrollsewer import *
import random

Tunnel = pygame.image.load('sewerTunnel.png')

x = 0
y = 300
STEP = 1
TunnelX = 400
TunnelY = 1800
TunnelSpot = random.randint(1, 3)
print(TunnelSpot)

TunnelRect = Tunnel.get_rect()
TunnelRect.center = (TunnelX, TunnelY)
score = 0


run = True
while run:

    TunnelX -= STEP

    if TunnelX <= -100:
        TunnelSpot = random.randint(1, 3)
        if TunnelSpot == 1:
            TunnelX = 1800
            TunnelY = 250
    
    #screen.blit(Tunnel, (TunnelX, TunnelY))

