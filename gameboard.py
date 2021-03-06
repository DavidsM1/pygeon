import pygame as pg
from settings import *
vec = pg.math.Vector2

def collide_hit_rect(one, two):
    return one.hit_rect.colliderect(two.rect)

def check_visibility(entity, camera):
    if (camera.x < entity.pos.x < camera.x + WIDTH) and (camera.y < entity.pos.y < camera.y + HEIGHT):
        return True
    return False


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
    def __init__(self, game, width, height, x=0, y=0):
        self.camera = pg.Rect(0, 0, width, height)
        self.game = game
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.pos = vec(x, y) * TILESIZE
        self.visible_enemies = 0
        for mob in self.game.mobs:
            if check_visibility(mob, self):
                mob.visible = True
                self.visible_enemies += 1
            else:
                mob.visible = False
        for gate in self.game.gates:
            if check_visibility(gate, self):
                gate.visible = True
        for slime in self.game.slimes:
            if check_visibility(slime, self):
                slime.visible = True
                self.visible_enemies += 1
            else:
                slime.visible = False
        for boss in self.game.bosses:
            if check_visibility(boss, self):
                boss.visible = True
                self.visible_enemies += 1
            else:
                boss.visible = False
    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, direction):
        if direction == 'right':
            self.x += WIDTH
            self.camera.move_ip(-WIDTH, 0)
        elif direction == 'left':
            self.x -= WIDTH
            self.camera.move_ip(WIDTH, 0)
        elif direction == 'down':
            self.y += HEIGHT
            self.camera.move_ip(0, -HEIGHT)
        elif direction == 'up':
            self.y -= HEIGHT
            self.camera.move_ip(0, HEIGHT)

        for mob in self.game.mobs:
            if check_visibility(mob, self):
                mob.visible = True
                self.visible_enemies += 1
            else:
                mob.visible = False

        for gate in self.game.gates:
            if check_visibility(gate, self):
                gate.visible = True

        for slime in self.game.slimes:
            if check_visibility(slime, self):
                slime.visible = True
                self.visible_enemies += 1
            else:
                slime.visible = False

        for boss in self.game.bosses:
            if check_visibility(boss, self):
                boss.visible = True
                self.visible_enemies += 1
            else:
                boss.visible = False
