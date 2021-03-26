import pygame, sys
from pygame.locals import * 

pygame.init()

WINDOW_SIZE = (400, 400)
WINDOW_NAME = "My First Pygame Window"

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
pygame.display.set_caption(WINDOW_NAME)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()