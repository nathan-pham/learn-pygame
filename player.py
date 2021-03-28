import pygame, math
from pygame.locals import *
from engine import Object, Vector
from config import *

SPEED = 2
MAX_SPEED_X = 100
MAX_SPEED_Y = 6
JUMP_SPEED = 6
AIR_CONSTANT = 0.1
GRAVITY = Vector(0, 1)

def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def move(rect, vel, tiles):
    collision_types = {"top": False, "bottom": False, "right": False, "left": False}
    rect.x += vel.x
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if vel.x > 0:
            rect.right = tile.left
            collision_types["right"] = True
        elif vel.x < 0:
            rect.left = tile.right
            collision_types["left"] = True

    rect.y += vel.y
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if vel.y > 0:
            rect.bottom = tile.top
            collision_types["bottom"] = True
        elif vel.y < 0:
            rect.top = tile.bottom
            collision_types["top"] = True

    return rect, collision_types

class Player(Object):
    def __init__(self, sprite_path, x, y):
        super().__init__(sprite_path, x, y)
        self.ground = False

    def apply(self, v):
        self.acc.add(v)

    def render(self, ctx):
        ctx.blit(self.sprite, self.pos.repr())

    def bound(self, tiles):
        player_box, collisions = move(self.box, self.vel, [tile.box for tile in tiles])
        self.box = player_box
        self.pos = Vector(player_box.x, player_box.y)

        if collisions["bottom"]:
            self.vel.y = 0
            self.ground = True
        else:
            self.ground = False

    def update(self, keys):
        drag = self.vel.clone()
        drag_magnitude = (drag.mag() ** 2) * AIR_CONSTANT
        drag.set_mag(-drag_magnitude)
        self.apply(drag)
        
        self.vel.add(self.acc)
        self.vel.x_limit(MAX_SPEED_X)
        self.vel.y_limit(MAX_SPEED_Y)
        self.pos.add(self.vel)
        self.acc.mult(0)

        if keys[K_RIGHT]:
            self.apply(Vector(SPEED, 0))

        if keys[K_LEFT]:
            self.apply(Vector(-SPEED, 0))

        if keys[K_UP] and self.ground:
            self.vel.add(Vector(0, -JUMP_SPEED))
            self.ground = False

        if not self.ground:
            self.apply(GRAVITY)

        self.box.x = self.pos.x
        self.box.y = self.pos.y
