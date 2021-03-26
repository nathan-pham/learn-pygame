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
                object.events(self.objects, events)
                object.render(self.screen)
                object.update(self.objects)

            for event in events:
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.clock.tick(FRAME_RATE)

class KeyMap:
    internal = {}

    def __getitem__(self, key):
        try:
            return self.internal[str(key)]
        except KeyError:
            return False

    def __setitem__(self, key, value):
        self.internal[str(key)] = value

class Object:
    keys = KeyMap()

    # blank render, requires screen or context
    def render(self, ctx):
        pass

    # blank update, requires world objects
    def update(self, objects):
        pass

    # internal event manager
    def events(self, objects, events):
        for event in events:
            if hasattr(event, "key") and hasattr(event, "type"):
                self.keys[event.key] = event.type == KEYDOWN
                