import pygame
from engine import Engine, Object, Vector
from player import Player
from tile import Tile
from config import *
from pygame.locals import *

pygame.init()

player_img = pygame.image.load("assets/player.png")
player_img.set_colorkey((255, 255, 255))

grass_img = pygame.image.load("assets/grass.png")
dirt_img = pygame.image.load("assets/dirt.png")

TILE_SIZE = grass_img.get_width()

game_map = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','2','2','2','2','2','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2'],
            ['1','1','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']]

player = Player(player_img, 50, 50)
world = Engine("Platformer Game")
tiles = []

for y in range(len(game_map)):
    for x in range(len(game_map[y])):
        tile = game_map[y][x]
        tile_size = (x * TILE_SIZE, y * TILE_SIZE)
        if tile == '1':
            tiles.append(Tile(dirt_img, *tile_size))
        elif tile == '2':
            tiles.append(Tile(grass_img, *tile_size))

def update(ctx, keys):
    ctx.fill(BG_COLOR)

    player.update()
    player.move(keys)
    player.bound(tiles)
    player.render(ctx)

    for tile in tiles:
        tile.render(ctx)

world.loop(update)