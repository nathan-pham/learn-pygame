import pygame
from pygame.locals import *
from engine import Object 

class Player(Object):
    def __init__(self, sprite_path):
        self.sprite = pygame.image.load(sprite_path)
        self.pos = [50, 50]

    def render(self, ctx):
        ctx.blit(self.sprite, self.pos)

player = Player("assets/learn-pygame-sprite.png")

