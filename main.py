import pygame, sys
from pygame.locals import * 

pygame.init()
pygame.display.set_caption("Pygame Platformer")
clock = pygame.time.Clock()

WINDOW_SIZE = (400, 400)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)