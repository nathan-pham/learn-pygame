import pygame, math
from pygame.locals import *
from engine import Object, Vector
from config import *

SPEED = 2
MAX_SPEED_X = 4
MAX_SPEED_Y = 15
JUMP_SPEED = 15
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
    hit_list = collision_test(rect, tiles)

    testv = vel.clone()
    testv.normalize()

    if (testv.mag() == 0): 
        return rect, collision_types

    while len(hit_list) > 0:
        rect.x -= testv.x
        rect.y -= testv.y
        hit_list = collision_test(rect, tiles)

    rect.x += 1
    collision_types["right"] = len(collision_test(rect, tiles)) > 0
    rect.x -= 2
    collision_types["left"] = len(collision_test(rect, tiles)) > 0
    rect.x += 1

    rect.y += 1
    collision_types["bottom"] = len(collision_test(rect, tiles)) > 0
    rect.y -= 2
    collision_types["top"] = len(collision_test(rect, tiles)) > 0
    rect.y += 1
    
    return rect, collision_types

class Player(Object):
    moving_right = False
    moving_left = False
    ground = False

    def __init__(self, sprite_path, x, y):
        super().__init__(sprite_path, x, y)

    def apply(self, v):
        self.acc.add(v)

    def render(self, ctx):
        ctx.blit(self.sprite, self.pos.repr())

    def bound(self, tiles):
        player_box, collisions = move(self.box, self.vel, [tile.box for tile in tiles])
        self.box = player_box
        self.pos = Vector(player_box.x, player_box.y)

        if collisions["bottom"]:
            self.vel.y = 0 # if this isn't included I go up like a ramp
            self.ground = True

        # do I add ground = False here since there aren't collisions?
        # it seems to glitch out :(

    def move(self, keys):
        if keys[K_RIGHT]:
            self.apply(Vector(SPEED, 0))

        if keys[K_LEFT]:
            self.apply(Vector(-SPEED, 0))


    def update(self):
        drag = self.vel.clone()
        drag_magnitude = (drag.mag() ** 2) * AIR_CONSTANT
        drag.set_mag(-drag_magnitude) 
        self.apply(drag)
        
        self.vel.add(self.acc)
        self.vel.x_limit(MAX_SPEED_X)
        self.vel.y_limit(MAX_SPEED_Y)
        self.pos.add(self.vel)
        self.acc.mult(0)

        if not self.ground:
            self.apply(GRAVITY)

        self.box.x = self.pos.x
        self.box.y = self.pos.y
