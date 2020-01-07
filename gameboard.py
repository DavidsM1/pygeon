import pygame as pg
from settings import *

def collide_hit_rect(one, two):
    return one.hit_rect.colliderect(two.rect)

class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line)

        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE

class TiledMap:
    def __init__(self, filename):
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm

    def render(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid

class Camera:
    def __init__(self, width, height, x=0, y=0):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, direction):
        if direction == 'right':
            self.x -= WIDTH
        elif direction == 'left':
            self.x += WIDTH
        elif direction == 'down':
            self.y -= HEIGHT
        elif direction == 'up':
            self.y += HEIGHT
        self.camera = pg.Rect(self.x, self.y, self.width, self.height)
