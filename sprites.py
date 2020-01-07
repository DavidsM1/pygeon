import pygame as pg
from settings import *
from gameboard import collide_hit_rect
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img_s
        self.rect = self.image.get_rect()
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.vel = vec(0, 0)
        self.pos = vec(x, y) * TILESIZE
        self.direction = SOUTH

    def get_keys(self):
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vel.x = -PLAYER_SPEED
            self.direction = WEST
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vel.x = PLAYER_SPEED
            self.direction = EAST
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vel.y = -PLAYER_SPEED
            self.direction = NORTH
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel.y = PLAYER_SPEED
            self.direction = SOUTH
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071
        if (keys[pg.K_LEFT] or keys[pg.K_a]) and (keys[pg.K_UP] or keys[pg.K_w]):
            self.direction = NORTHWEST
        if (keys[pg.K_RIGHT] or keys[pg.K_d]) and (keys[pg.K_UP] or keys[pg.K_w]):
            self.direction = NORTHEAST
        if (keys[pg.K_LEFT] or keys[pg.K_a]) and (keys[pg.K_DOWN] or keys[pg.K_s]):
            self.direction = SOUTHWEST
        if (keys[pg.K_RIGHT] or keys[pg.K_d]) and (keys[pg.K_DOWN] or keys[pg.K_s]):
            self.direction = SOUTHEAST

    def rotate_player(self):
        if self.direction == SOUTH:
            self.image = self.game.player_img_s
        elif self.direction == NORTH:
            self.image = self.game.player_img_n
        elif self.direction == EAST:
            self.image = self.game.player_img_e
        elif self.direction == WEST:
            self.image = self.game.player_img_w
        elif self.direction == NORTHWEST:
            self.image = self.game.player_img_nw
        elif self.direction == SOUTHWEST:
            self.image = self.game.player_img_sw
        elif self.direction == NORTHEAST:
            self.image = self.game.player_img_ne
        elif self.direction == SOUTHEAST:
            self.image = self.game.player_img_se

    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False, collide_hit_rect)
            if hits:
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.hit_rect.width / 2
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right + self.hit_rect.width / 2
                self.vel.x = 0
                self.hit_rect.centerx = self.pos.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False, collide_hit_rect)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.hit_rect.height / 2
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom + self.hit_rect.height / 2
                self.vel.y = 0
                self.hit_rect.centery = self.pos.y

    def enter_door(self, dir, camera):
        if dir == 'x':
            enters = pg.sprite.spritecollide(self, self.game.doors, False, collide_hit_rect)
            if enters:
                if self.vel.x > 0:
                    self.pos.x += TILESIZE * 5
                    camera.update('right')
                if self.vel.x < 0:
                    self.pos.x -= TILESIZE * 5
                    camera.update('left')
        if dir == 'y':
            enters = pg.sprite.spritecollide(self, self.game.doors, False, collide_hit_rect)
            if enters:
                if self.vel.y > 0:
                    self.pos.y += TILESIZE * 5
                    camera.update('down')
                if self.vel.y < 0:
                    self.pos.y -= TILESIZE * 5
                    camera.update('up')

    def update(self):
        self.get_keys()
        self.rotate_player()
        self.pos += self.vel * self.game.dt
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.hit_rect.centerx = self.pos.x
        self.collide_with_walls('x')
        self.hit_rect.centery = self.pos.y
        self.collide_with_walls('y')
        self.rect.center = self.hit_rect.center

class Mob(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs
        self.game = game
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = game.mob_img
        self.rect = self.image.get_rect()
        self.pos = vec(x, y) * TILESIZE
        self.rect.center = self.pos

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y, type = 1):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        if type == 2:
            self.image = game.wall_img_2
        elif type == 3:
            self.image = game.wall_img_2
            self.image = pg.transform.rotate(self.image, 90)
        elif type == 4:
            self.image = game.wall_img_2
            self.image = pg.transform.rotate(self.image, 180)
        elif type == 5:
            self.image = game.wall_img_2
            self.image = pg.transform.rotate(self.image, 270)
        elif type == 6:
            self.image = game.wall_img_1
            self.image = pg.transform.rotate(self.image, 90)
        else:
            self.image = game.wall_img_1
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Door(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.doors
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
