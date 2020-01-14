import pygame as pg
vec = pg.math.Vector2

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BROWN = (106, 55, 5)
DARKGREEN = (33, 85, 85)
OLIVEGREEN = (67,120,29)

# game settings
WIDTH = 1024   # tilesize * 32  32 bloki pa labi
HEIGHT = 576   # tilesize * 18   18 bloki uz leju
FPS = 60
TITLE = 'Pygeon'
BGCOLOR = OLIVEGREEN

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

WALL_IMG_2 = 'wall_2_s.png'

WALL_IMG_1 = 'wall_1_h.png'

PILLAR_S = 'pillar_s.png'
PILLAR_N = 'pillar_n.png'
PILLAR_E = 'pillar_e.png'
PILLAR_W = 'pillar_w.png'

PILLAR_WALL_H = 'pillar_wall_h.png'
PILLAR_WALL_V = 'pillar_wall_v.png'

FLOOR_IMG = 'floor.png'

WALL_IMG_CORNER = 'wall_corner.png'

DOORS_H = 'doors_h.png'
DOORS_V = 'doors_v.png'

# player settings
PLAYER_HEALTH = 3
PLAYER_SPEED = 200
PLAYER_HIT_RECT = pg.Rect(0, 0, 32, 64)
BARREL_OFFSET = vec(0, 0)

PLAYER_IMG_S = 'p_s.png'
PLAYER_IMG_SE = 'p_se.png'
PLAYER_IMG_N = 'p_n.png'
PLAYER_IMG_NW = 'p_nw.png'
PLAYER_IMG_W = 'p_w.png'
PLAYER_IMG_NE = 'p_ne.png'
PLAYER_IMG_E = 'p_e.png'
PLAYER_IMG_SW = 'p_sw.png'

# MOB settings
MOB_IMG = 'enemy_bench.png'
MOB_SPEEDS = [100, 125, 75, 150]
MOB_HIT_RECT = pg.Rect(0, 0, 32, 32)
MOB_HEALTH = 10
MOB_DAMAGE = 1
MOB_KNOCKBACK = 20
AVOID_RADIUS = 50

# BOSS settings
BOSS_IMG = 'boss_couch.png'
BOSS_HEALTH = 1
BOSS_DAMAGE = 1
BOSS_HIT_RECT = pg.Rect(0, 0, 384, 192)
BOSS_KNOCKBACK = 60
BOSS_BULLET_RATE = 800
BOSS_BULLET_LIFETIME = 10000
BOSS_BULLET_SPEED = 120

BOSS_BAR_LENGTH = 980
BOSS_BAR_HEIGHT = 20

# SLIME settings
SLIME_IMG = 'enemy_slime.png'
SLIME_SPEED = 160
SLIME_HIT_RECT = pg.Rect(0, 0, 32, 32)
SLIME_HEALTH = 8
SLIME_DAMAGE = 1
SLIME_KNOCKBACK = 0
# gun settings
BULLET_IMG = 'bullet.png'
BULLET_SPEED = 300
BULLET_LIFETIME = 2000
BULLET_RATE = 400
GUN_SPREAD = 5
BULLET_DAMAGE = 1

# directions
NORTH = 0
NORTHEAST = 1
EAST = 2
SOUTHEAST = 3
SOUTH = 4
SOUTHWEST = 5
WEST = 6
NORTHWEST = 7

# angles
ANGLE_EAST = 0
ANGLE_NORTHEAST = 45
ANGLE_NORTH = 90
ANGLE_NORTHWEST = 135
ANGLE_WEST = 180
ANGLE_SOUTHWEST = 225
ANGLE_SOUTH = 270
ANGLE_SOUTHEAST = 315
