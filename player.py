import pygame
from pygame.locals import *
from engine import Object, Vector
from config import *

SPEED = 2
MAX_SPEED = 5
MAX_SPEED_X = 5
MAX_SPEED_Y = 15
JUMP_HEIGHT = 10
AIR_RESISTANCE = 0.5
GRAVITY = Vector(0, 1)

class Player(Object):
    def __init__(self, sprite_path):
        self.sprite = pygame.image.load(sprite_path)
        self.pos = Vector(50, 50)
        self.vel = Vector(0, 0)
        self.acc = Vector(0, 0)
        self.jump = False

    def apply(self, v):
        self.acc.add(v)

    def render(self, ctx):
        ctx.blit(self.sprite, self.pos.repr())

    def bound(self):
        if self.pos.y >= WINDOW_SIZE[1] - self.sprite.get_height():
            self.pos.y = WINDOW_SIZE[1] - self.sprite.get_height()
            self.jump = True

    def update(self, objects):
        air_resistance = self.vel.clone()
        air_resistance.set_mag(-AIR_RESISTANCE)

        self.vel.add(self.acc)
        self.vel.add(air_resistance)
        self.vel.x_limit(MAX_SPEED_X)
        self.vel.y_limit(MAX_SPEED_Y)
        self.pos.add(self.vel)
        self.acc.mult(0)

        if self.keys[K_RIGHT]:
            self.apply(Vector(SPEED, 0))

        if self.keys[K_LEFT]:
            self.apply(Vector(-SPEED, 0))

        if self.keys[K_UP] and self.jump:
            self.apply(Vector(0, -JUMP_HEIGHT))
            self.jump = False

        self.apply(GRAVITY)
        self.bound()

player = Player("assets/learn-pygame-sprite.png")

