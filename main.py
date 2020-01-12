import sys
import pygame as pg
from os import path
from settings import *
from sprites import *
from gameboard import *
from pygame.locals import *

# HUD functions
def draw_player_health(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 20
    fill = pct * BAR_LENGTH
    outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pg.Rect(x, y, fill, BAR_HEIGHT)
    if pct > 0.6:
        col = GREEN
    elif pct > 0.3:
        col = YELLOW
    else:
        col = RED
    pg.draw.rect(surf, col, fill_rect)
    pg.draw.rect(surf, WHITE, outline_rect, 2)

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | FULLSCREEN)
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')
        self.map = Map(path.join(game_folder, 'map.txt'))
        self.player_img_s = pg.image.load(path.join(img_folder, PLAYER_IMG_S)).convert_alpha()
        self.player_img_s = pg.transform.scale(self.player_img_s, (TILESIZE, TILESIZE * 2))
        self.player_img_n = pg.image.load(path.join(img_folder, PLAYER_IMG_N)).convert_alpha()
        self.player_img_n = pg.transform.scale(self.player_img_n, (TILESIZE, TILESIZE * 2))
        self.player_img_e = pg.image.load(path.join(img_folder, PLAYER_IMG_E)).convert_alpha()
        self.player_img_e = pg.transform.scale(self.player_img_e, (TILESIZE, TILESIZE * 2))
        self.player_img_w = pg.image.load(path.join(img_folder, PLAYER_IMG_W)).convert_alpha()
        self.player_img_w = pg.transform.scale(self.player_img_w, (TILESIZE, TILESIZE * 2))
        self.player_img_se = pg.image.load(path.join(img_folder, PLAYER_IMG_SE)).convert_alpha()
        self.player_img_se = pg.transform.scale(self.player_img_se, (TILESIZE, TILESIZE * 2))
        self.player_img_sw = pg.image.load(path.join(img_folder, PLAYER_IMG_SW)).convert_alpha()
        self.player_img_sw = pg.transform.scale(self.player_img_sw, (TILESIZE, TILESIZE * 2))
        self.player_img_ne = pg.image.load(path.join(img_folder, PLAYER_IMG_NE)).convert_alpha()
        self.player_img_ne = pg.transform.scale(self.player_img_ne, (TILESIZE, TILESIZE * 2))
        self.player_img_nw = pg.image.load(path.join(img_folder, PLAYER_IMG_NW)).convert_alpha()
        self.player_img_nw = pg.transform.scale(self.player_img_nw, (TILESIZE, TILESIZE * 2))
        self.wall_img_1 = pg.image.load(path.join(img_folder, WALL_IMG_1)).convert_alpha()
        self.wall_img_2 = pg.image.load(path.join(img_folder, WALL_IMG_2)).convert_alpha()
        self.wall_img_corner = pg.image.load(path.join(img_folder, WALL_IMG_CORNER)).convert_alpha()
        self.mob_img = pg.image.load(path.join(img_folder, MOB_IMG)).convert_alpha()
        self.bullet_img = pg.image.load(path.join(img_folder, BULLET_IMG)).convert_alpha()

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.doors = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        self.gates = pg.sprite.Group()
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == '2':
                    Wall(self, col, row, 2)
                if tile == '3':
                    Wall(self, col, row, 3)
                if tile == '4':
                    Wall(self, col, row, 4)
                if tile == '5':
                    Wall(self, col, row, 5)
                if tile == '6':
                    Wall(self, col, row, 6)
                if tile == '7':
                    Wall(self, col, row, 7)
                if tile == 'D':
                    Door(self, col, row)
                if tile == 'M':
                    Mob(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
                if tile == 'G':
                    Gate(self, col, row)
        self.camera = Camera(self, WIDTH, HEIGHT)

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.player.enter_door('x', self.camera)
        self.player.enter_door('y', self.camera)
        self.all_sprites.update()
        # player gets hit
        hits = pg.sprite.spritecollide(self.player, self.mobs, False, collide_hit_rect)
        for hit in hits:
            self.player.health -= MOB_DAMAGE
            hit.vel = vec(0, 0)
            if self.player.health <= 0:
                self.playing = False
        if hits:
            self.player.pos += vec(MOB_KNOCKBACK, 0).rotate(-hits[0].rot)
        # bullets hit mobs
        hits = pg.sprite.groupcollide(self.mobs, self.bullets, False, True)
        for hit in hits:
            hit.health -= BULLET_DAMAGE
            hit.vel = vec(0, 0)

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        # pg.draw.rect(self.screen, WHITE, self.player.hit_rect, 2)
        # HUD
        draw_player_health(self.screen, 20, 10, self.player.health / PLAYER_HEALTH)
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()
