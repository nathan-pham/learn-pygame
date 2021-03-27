import pygame
from engine import World, Object
from player import player
from config import *

class Test(Object):
    def __init__(self):
        super().__init__("assets/learn-pygame-sprite.png", 150, 150)

    def render(self, ctx):
        ctx.blit(self.sprite, self.pos.repr())

test_rect = Test()

pygame.init()
world = World("Game")

def update(ctx, keys):
    ctx.fill(BG_COLOR)

    if player.box.colliderect(test_rect.box):
        pygame.draw.rect(ctx, (255, 0, 0), test_rect.box)
    else:
        pygame.draw.rect(ctx, (0, 0, 0), test_rect.box)
    
    player.render(ctx)
    player.update(keys)



world.loop(update)