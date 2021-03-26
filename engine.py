import pygame, sys
from pygame.locals import *

WINDOW_SIZE = (400, 400)
WINDOW_NAME = "Pygame Window"
FRAME_RATE = 60

class World:
    objects = []
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

    def __init__(self, app_name):
        pygame.display.set_caption(app_name or WINDOW_NAME)

    def append(self, object):
        self.objects.append(object)

    def loop(self):
        while True:
            events = pygame.event.get()

            for object in self.objects:
                object.render(self.screen)
                object.update(self.objects)
                object.events(self.objects, events)

            for event in events:
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.clock.tick(FRAME_RATE)

class Object:
    def render(self, ctx):
        pass

    def update(self, objects):
        pass

    def key_down(self):
        pass

    def key_up(self):
        pass

    def events(self, objects, events):
        for event in events:
            if event.type == KEYDOWN:
                self.key_down()
            elif event.type == KEYUP:
                self.key_up()