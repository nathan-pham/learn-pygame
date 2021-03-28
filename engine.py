import pygame, math, sys
from pygame.locals import *
from config import *

# main engine
class Engine:
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
    display = pygame.Surface(WINDOW_SCALE)

    def __init__(self, app_name):
        pygame.display.set_caption(app_name or WINDOW_NAME)
    
    def loop(self, update):
        while True:
            events = pygame.event.get()

            for event in events:
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            update(self.display, pygame.key.get_pressed())

            self.screen.blit(pygame.transform.scale(self.display, WINDOW_SIZE), (0, 0))
            pygame.display.update()
            self.clock.tick(FRAME_RATE)

# boiler plate for Objects
class Object:
    def __init__(self, sprite_path, x, y):
        self.sprite = pygame.image.load(sprite_path) if isinstance(sprite_path, str) else sprite_path
        self.box = self.sprite.get_rect()
        self.box.x = x
        self.box.y = y
        self.pos = Vector(x, y)
        self.vel = Vector(0, 0)
        self.acc = Vector(0, 0)

    # blank render, requires screen or context
    def render(self, ctx):
        pass

    # blank update, requires keys
    def update(self, keys):
        pass

    # internal update
    def _update(self):
        pass

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
        if abs(self.y) > max:
            clone = Vector(0, self.y)
            clone.set_mag(max)
            self.y = clone.y

    def normalize(self):
        m = self.mag()
        if m != 0:
            self.div(m)

    def clone(self):
        return Vector(self.x, self.y)