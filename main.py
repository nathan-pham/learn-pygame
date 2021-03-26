import pygame
from engine import World, Object
from player import player

pygame.init()

world = World("Game")
world.append(player)

world.loop()