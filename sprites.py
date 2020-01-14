import pygame as pg
from random import uniform, choice
from settings import *
from gameboard import collide_hit_rect
vec = pg.math.Vector2

def collide_with_walls(sprite, group, dir):
    if dir == 'x':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centerx > sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width / 2
            if hits[0].rect.centerx < sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width / 2
            sprite.vel.x = 0
            sprite.hit_rect.centerx = sprite.pos.x
    if dir == 'y':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centery > sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height / 2
            if hits[0].rect.centery < sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height / 2
            sprite.vel.y = 0
            sprite.hit_rect.centery = sprite.pos.y

def slime_collide_with_walls(sprite, group, dir):
    if dir == 'x':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centerx > sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width / 2
            if hits[0].rect.centerx < sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width / 2
            sprite.vel.x = 0
            sprite.hit_rect.centerx = sprite.pos.x
            sprite.rot += 45
    if dir == 'y':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centery > sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height / 2
            if hits[0].rect.centery < sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height / 2
            sprite.vel.y = 0
            sprite.hit_rect.centery = sprite.pos.y
            sprite.rot += 45

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
        self.last_shot = 0
        self.angle = ANGLE_SOUTH
        self.health = PLAYER_HEALTH

    def get_keys(self):
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()

        if keys[pg.K_a]:
            self.vel.x = -PLAYER_SPEED
            self.direction = WEST
        if keys[pg.K_d]:
            self.vel.x = PLAYER_SPEED
            self.direction = EAST
        if keys[pg.K_w]:
            self.vel.y = -PLAYER_SPEED
            self.direction = NORTH
        if keys[pg.K_s]:
            self.vel.y = PLAYER_SPEED
            self.direction = SOUTH

        if keys[pg.K_a] and keys[pg.K_w]:
            self.direction = NORTHWEST
        if keys[pg.K_d] and keys[pg.K_w]:
            self.direction = NORTHEAST
        if keys[pg.K_a] and keys[pg.K_s]:
            self.direction = SOUTHWEST
        if keys[pg.K_d] and keys[pg.K_s]:
            self.direction = SOUTHEAST

        if keys[pg.K_LEFT]:
            self.direction = WEST
            self.angle = ANGLE_WEST
            now = pg.time.get_ticks()
            if now - self.last_shot > BULLET_RATE:
                self.last_shot = now
                dir = vec(1, 0).rotate(-self.angle)
                pos = self.pos + BARREL_OFFSET.rotate(-self.angle)
                Bullet(self.game, pos, dir)
        if keys[pg.K_RIGHT]:
            self.direction = EAST
            self.angle = ANGLE_EAST
            now = pg.time.get_ticks()
            if now - self.last_shot > BULLET_RATE:
                self.last_shot = now
                dir = vec(1, 0).rotate(-self.angle)
                pos = self.pos + BARREL_OFFSET.rotate(-self.angle)
                Bullet(self.game, pos, dir)
        if keys[pg.K_UP]:
            self.direction = NORTH
            self.angle = ANGLE_NORTH
            now = pg.time.get_ticks()
            if now - self.last_shot > BULLET_RATE:
                self.last_shot = now
                dir = vec(1, 0).rotate(-self.angle)
                pos = self.pos + BARREL_OFFSET.rotate(-self.angle)
                Bullet(self.game, pos, dir)
        if keys[pg.K_DOWN]:
            self.direction = SOUTH
            self.angle = ANGLE_SOUTH
            now = pg.time.get_ticks()
            if now - self.last_shot > BULLET_RATE:
                self.last_shot = now
                dir = vec(1, 0).rotate(-self.angle)
                pos = self.pos + BARREL_OFFSET.rotate(-self.angle)
                Bullet(self.game, pos, dir)

        if keys[pg.K_LEFT] and keys[pg.K_UP]:
            self.direction = NORTHWEST
        if keys[pg.K_RIGHT] and keys[pg.K_UP]:
            self.direction = NORTHEAST
        if keys[pg.K_LEFT] and keys[pg.K_DOWN]:
            self.direction = SOUTHWEST
        if keys[pg.K_RIGHT] and keys[pg.K_DOWN]:
            self.direction = SOUTHEAST

        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071

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
        collide_with_walls(self, self.game.walls, 'x')
        collide_with_walls(self, self.game.gates, 'x')
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, 'y')
        collide_with_walls(self, self.game.gates, 'y')
        self.rect.center = self.hit_rect.center

class Mob(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs
        self.game = game
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = game.mob_img
        self.rect = self.image.get_rect()
        self.hit_rect = MOB_HIT_RECT.copy()
        self.hit_rect.center = self.rect.center
        self.pos = vec(x, y) * TILESIZE
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.rect.center = self.pos
        self.rot = 0
        self.health = MOB_HEALTH
        self.visible = False
        self.speed = choice(MOB_SPEEDS)

    def avoid_mobs(self):
        for mob in self.game.mobs:
            if mob != self:
                dist = self.pos - mob.pos
                if 0 < dist.length() < AVOID_RADIUS:
                    self.acc += dist.normalize()

    def update(self):
        if self.visible:
            self.rot = (self.game.player.pos - self.pos).angle_to(vec(1, 0))
            self.image = pg.transform.rotate(self.game.mob_img, self.rot)
            self.rect = self.image.get_rect()
            self.rect.center = self.pos
            self.acc = vec(1, 0).rotate(-self.rot)
            self.avoid_mobs()
            self.acc.scale_to_length(self.speed)
            self.acc += self.vel * -1
            self.vel += self.acc * self.game.dt
            self.pos += self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2 #equation of motion
            self.hit_rect.centerx = self.pos.x
            collide_with_walls(self, self.game.walls, 'x')
            collide_with_walls(self, self.game.gates, 'x')
            self.hit_rect.centery = self.pos.y
            collide_with_walls(self, self.game.walls, 'y')
            collide_with_walls(self, self.game.gates, 'y')
            self.rect.center = self.hit_rect.center
            if self.health <= 0:
                self.kill()
                self.game.camera.visible_enemies -= 1
                if self.game.camera.visible_enemies < 0:
                    self.game.camera.visible_enemies = 0

class Boss(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.bosses
        self.game = game
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = game.boss_img
        self.rect = self.image.get_rect()
        self.hit_rect = BOSS_HIT_RECT.copy()
        self.hit_rect.center = self.rect.center
        self.pos = vec(x, y) * TILESIZE
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.rect.center = self.pos
        self.rot = 0
        self.health = BOSS_HEALTH
        self.last_shot = 0
        self.visible = False

    def update(self):
        if self.visible:
            self.rot = (self.game.player.pos - self.pos).angle_to(vec(1, 0))
            if self.health <= 0:
                self.kill()
                self.game.camera.visible_enemies -= 1
                if self.game.camera.visible_enemies < 0:
                    self.game.camera.visible_enemies = 0
            now = pg.time.get_ticks()
            if now - self.last_shot > BOSS_BULLET_RATE:
                self.last_shot = now
                dir = vec(1, 0).rotate(-self.rot)
                pos = self.pos + BARREL_OFFSET.rotate(-self.rot)
                BossBullet(self.game, pos, dir)
                dir = vec(1,0).rotate(-self.rot + 25)
                BossBullet(self.game, pos, dir)
                dir = vec(1,0).rotate(-self.rot - 25)
                BossBullet(self.game, pos, dir)
                dir = vec(1,0).rotate(-self.rot - 50)
                BossBullet(self.game, pos, dir)
                dir = vec(1,0).rotate(-self.rot + 50)
                BossBullet(self.game, pos, dir)
class Slime(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.slimes
        self.game = game
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = game.slime_img
        self.rect = self.image.get_rect()
        self.hit_rect = SLIME_HIT_RECT.copy()
        self.hit_rect.center = self.rect.center
        self.pos = vec(x, y) * TILESIZE
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.rect.center = self.pos
        self.rot = 45
        self.health = SLIME_HEALTH
        self.visible = False

    def update(self):
        if self.visible:
            #self.rot = self.pos.angle_to(vec(1, 0))
            #self.image = pg.transform.rotate(self.game.slime_img, self.rot)
            self.rect = self.image.get_rect()
            self.rect.center = self.pos
            self.acc = vec(SLIME_SPEED, 0).rotate(-self.rot)
            self.acc += self.vel * -1
            self.vel += self.acc * self.game.dt
            self.pos += self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2 #equation of motion
            self.hit_rect.centerx = self.pos.x
            slime_collide_with_walls(self, self.game.walls, 'x')
            slime_collide_with_walls(self, self.game.gates, 'x')
            self.hit_rect.centery = self.pos.y
            slime_collide_with_walls(self, self.game.walls, 'y')
            slime_collide_with_walls(self, self.game.gates, 'y')
            self.rect.center = self.hit_rect.center
            if self.health <= 0:
                self.kill()
                self.game.camera.visible_enemies -= 1
                if self.game.camera.visible_enemies < 0:
                    self.game.camera.visible_enemies = 0
        if self.rot >= 360:
            self.rot -= 360

class Bullet(pg.sprite.Sprite):
    def __init__(self, game, pos, dir):
        self.game = game
        self.groups = game.all_sprites, game.bullets
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = game.bullet_img
        self.rect = self.image.get_rect()
        self.pos = vec(pos)
        self.rect.center = pos
        spread = uniform(-GUN_SPREAD, GUN_SPREAD)
        self.vel = dir.rotate(spread) * BULLET_SPEED
        self.spawn_time = pg.time.get_ticks()

    def update(self):
        self.pos += self.vel * self.game.dt
        self.rect.center = self.pos
        if pg.sprite.spritecollideany(self, self.game.walls):
            self.kill()
        if pg.time.get_ticks() - self.spawn_time > BULLET_LIFETIME:
            self.kill()

class BossBullet(pg.sprite.Sprite):
    def __init__(self, game, pos, dir):
        self.game = game
        self.groups = game.all_sprites, game.boss_bullets
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = game.boss_bullet_img
        self.rect = self.image.get_rect()
        self.pos = vec(pos)
        self.rect.center = pos
        spread = uniform(-GUN_SPREAD, GUN_SPREAD)
        self.vel = dir.rotate(spread) * BOSS_BULLET_SPEED
        self.spawn_time = pg.time.get_ticks()

    def update(self):
        self.pos += self.vel * self.game.dt
        self.rect.center = self.pos
        if pg.sprite.spritecollideany(self, self.game.walls):
            self.kill()
        if pg.time.get_ticks() - self.spawn_time > BOSS_BULLET_LIFETIME:
            self.kill()

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
        elif type == 7:
            self.image = game.wall_img_corner
        elif type == 8:
            self.image = game.pillar_img_s
        elif type == 9:
            self.image = game.pillar_img_n
        elif type == 0:
            self.image = game.pillar_img_e
        elif type == '-':
            self.image = game.pillar_img_w
        elif type == '=':
            self.image = game.pillar_wall_img_h
        elif type == 'Q':
            self.image = game.pillar_wall_img_v
        else:
            self.image = game.wall_img_1
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Door(pg.sprite.Sprite):
    def __init__(self, game, x, y, vertical = 0):
        self.groups = game.all_sprites, game.doors
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        if vertical:
            self.image = game.door_img_v
        else:
            self.image = game.door_img_h
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Floor(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.floor
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.floor_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Gate(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.gates
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(DARKGREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.pos = vec(x, y) * TILESIZE
        self.visible = False

    def update(self):
        if self.game.camera.visible_enemies == 0 and self.visible:
            self.kill()
