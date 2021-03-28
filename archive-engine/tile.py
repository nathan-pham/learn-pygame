from engine import Object

class Tile(Object):
    def __init__(self, tile, x, y):
        super().__init__(tile, x, y)

    def render(self, ctx):
        ctx.blit(self.sprite, self.pos.repr())