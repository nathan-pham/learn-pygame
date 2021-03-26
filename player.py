import pygame
from pygame.locals import *
from engine import Object 

class Player(Object):
    speed = 4
    
    def __init__(self, sprite_path):
        self.sprite = pygame.image.load(sprite_path)
        self.location = [50, 50]

    def render(self, ctx):
        ctx.blit(self.sprite, self.location)

    def update(self, objects):
        if self.keys[K_RIGHT]:
            self.location[0] += 1

player = Player("assets/learn-pygame-sprite.png")

