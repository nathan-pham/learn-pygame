import pygame
from pygame.locals import *
from engine import Object, Vector

SPEED = 1
MAX_SPEED = 5

class Player(Object):
    def __init__(self, sprite_path):
        self.sprite = pygame.image.load(sprite_path)
        self.pos = Vector(50, 50)
        self.vel = Vector(0, 0)
        self.acc = Vector(0, 0)

    def apply(self, v):
        self.acc.add(v)

    def render(self, ctx):
        ctx.blit(self.sprite, self.pos.repr())

    def update(self, objects):
        air_resistance = self.vel.clone()
        air_resistance.set_mag(-0.1)

        self.vel.add(self.acc)
        self.vel.add(air_resistance)
        self.vel.limit(MAX_SPEED)
        self.pos.add(self.vel)
        self.acc.mult(0)

        if self.keys[K_RIGHT]:
            self.apply(Vector(SPEED, 0))
        if self.keys[K_LEFT]:
            self.apply(Vector(-SPEED, 0))

player = Player("assets/learn-pygame-sprite.png")

