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

# game settings
WIDTH = 1024   # tilesize * 32  32 bloki pa labi
HEIGHT = 576   # tilesize * 18   18 bloki uz leju
FPS = 60
TITLE = 'Pygeon'
BGCOLOR = BROWN

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

WALL_IMG_2 = 'wall_2.png'
WALL_IMG_1 = 'wall_1.png'
WALL_IMG_CORNER = 'wall_corner.png'

# player settings
PLAYER_HEALTH = 3
PLAYER_SPEED = 200
PLAYER_HIT_RECT = pg.Rect(0, 0, 32, 64)
BARREL_OFFSET = vec(0, -18)

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
MOB_SPEED = 100
MOB_HIT_RECT = pg.Rect(0, 0, 32, 32)
MOB_HEALTH = 1
MOB_DAMAGE = 1
MOB_KNOCKBACK = 20

# gun settings
BULLET_IMG = 'bullet.png'
BULLET_SPEED = 300
BULLET_LIFETIME = 1000
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
