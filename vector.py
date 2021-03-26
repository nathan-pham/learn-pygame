from math import sqrt

class Vector:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def repr(self):
        return (self.x, self.y)

    def arr(self):
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
        return sqrt(self.x ** 2 + self.y ** 2)

    def set_mag(self, m):
        self.normalize()
        self.mult(m)

    def limit(self, max):
        if(self.mag() > max):
            self.set_mag(max)

    def normalize(self):
        m = self.mag()
        if m != 0:
            self.div(m)

    def clone(self):
        return Vector(self.x, self.y)