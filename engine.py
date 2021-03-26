import pygame, math, sys
from pygame.locals import *
from config import *

# main engine
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
            self.screen.fill(BG_COLOR)
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

# Object utility class
class KeyMap:
    internal = {}

    def __getitem__(self, key):
        try:
            return self.internal[str(key)]
        except KeyError:
            return False

    def __setitem__(self, key, value):
        self.internal[str(key)] = value

# boiler plate for Objects
class Object:
    keys = KeyMap()

    # blank render, requires screen or context
    def render(self, ctx):
        pass

    # blank update, requires world objects & context
    def update(self, objects):
        pass

    # internal event manager
    def events(self, objects, events):
        for event in events:
            if hasattr(event, "key") and hasattr(event, "type"):
                self.keys[event.key] = event.type == KEYDOWN

# Vector abstraction    
class Vector:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def repr(self):
        return (self.x, self.y)

    def add(self, v):
        self.x += v.x
        self.y += v.y

    def sub(self, v):
        self.x -= v.x
        self.y -= v.y
    
    def mult(self, n):
        self.x *= n
        self.y *= n

    def div(self, n):
        self.x /= n
        self.y /= n

    def mag(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def set_mag(self, m):
        self.normalize()
        self.mult(m)

    def limit(self, max):
        if self.mag() > max:
            self.set_mag(max)

    def x_limit(self, max):
        if abs(self.x) > max:
            clone = Vector(self.x, 0)
            clone.set_mag(max)
            self.x = clone.x

    def y_limit(self, max):
        if abs(self.y) > max and self.y != 0:
            clone = Vector(0, self.y)
            clone.set_mag(max)
            self.y = clone.y

    def normalize(self):
        m = self.mag()
        if m != 0:
            self.div(m)

    def clone(self):
        return Vector(self.x, self.y)