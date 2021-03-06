import sys
import os
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (160, 0, 160)
GREY = (100, 100, 100)

# Main font
if hasattr(sys, "_MEIPASS"):
    FONT_NAME = os.path.join(sys._MEIPASS, 'fonts/good_times.ttf')
    SECOND_FONT_NAME = os.path.join(sys._MEIPASS, 'fonts/hemi_head.ttf')
    THIRD_FONT_NAME = os.path.join(sys._MEIPASS, 'fonts/libel-suit-rg.ttf')
else:
    FONT_NAME = 'fonts/good_times.ttf'
    SECOND_FONT_NAME = 'fonts/hemi_head.ttf'
    THIRD_FONT_NAME = 'fonts/libel-suit-rg.ttf'


FPS = 60

# EPSILON
EPS = 0.000001

# DIMENSION
# http://gamedevelopment.tutsplus.com/articles/quick-tip-what-is-the-best-screen-resolution-for-your-game--gamedev-14723
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_WIDTH = 32
TILE_HEIGHT = 32

# Development mode, DEV or OPT
DEV_MODE = 1
OPT_MODE = 0
MODE = DEV_MODE

# Scenes self.nextScene commands, used to tell SceneHandler what next scene to run after this one ends
TITLE_SCENE = 0
INSTRUCTION_SCENE = 911
CREDIT_SCENE = 1800
CORRIDOR_LEVEL_1 = 1
TEST_TMX_SCENE = 404
GUARD_CORRIDOR_LEVEL = 19
BOMB_CORRIDOR_LEVEL = 20
LASER_CORRIDOR_LEVEL = 29
GUARD_BOSS_LEVEL = 11
BOMB_BOSS_LEVEL = 21
LASER_BOSS_LEVEL = 31
ENDING_SCENE = 99

# Sprite Layer
SPRITE_LAYER = 4

# Facing Sides
RIGHT = 0
LEFT = 1
UP = 2
DOWN = 3

# Boss 2 States
UPDOWN_LASER = 0
RIGHTLEFT_LASER = 1

# Collisions
COLLISION_LAYER = 0
SOLID = 1  # Booléen de GID pour collision
SPIKE = 2
SPRING = 3
ENERGY_CHARGE = 4
NONE = 0  # Pour identifier qu'il n'y a eu aucune collision

# Player jump states
GROUNDED = 0
JUMP = 1
CLIMBING = 2  # When on a ladder

# Physics
GRAVITY = 1
FRICTION = 1

# Projectiles
TARGET_DISTANCE = 40

PLAYER_BULLET_DAMAGE = 10
PLAYER_BULLET_SPEED = 10
PLAYER_BULLET_COOLDOWN = 10

PLAYER_MAX_LIFE = 165
PLAYER_INVINCIBILITY_COOLDOWN = 60
PLAYER_MAX_ENERGY = 40
PLAYER_RECHARGE_COOLDOWN = 10

BOSS_INVINCIBILITY_COOLDOWN = 5

# END SCENE CONDITION
PLAYER_DEAD = 666
BOSS_DEAD = 420

# ANIMATION STATE
ANIMATION_NORMAL = 0
ANIMATION_HEALTHLESS = 1
ANIMATION_POWERLESS = 2
ANIMATION_HEALTHLESS_POWERLESS = 3

# Dimension tile base for icon
TILEDIMX = 32
TILEDIMY = 32

# GUI settings
DIALOG_TEXT_SIZE = 20
INPUT_BOX_FONT = "Arial"
INPUT_BOX_TEXT_SIZE = 20
MENU_FONT = "Arial"
MENU_FONT_COLOR = BLUE
COLOR_POWER_BAR = (100, 50, 138)
COLOR_POWER_BAR_EMPTY = (0, 0, 0, 1)

BACKGROUND_COLOR = (255, 255, 255)

COLOR_MENU_1 = (168,42,42)
COLOR_MENU_2 = (185,204,10)
COLOR_MENU_FONTS = (255, 255, 255)

COLOR_MENU_SELECT_1 = (255,253,87)
COLOR_MENU_SELECT_2 = (0,0,0)
COLOR_MENU_FONTS_SELECT = (0,0,0)
COLORKEY = (1, 1, 1)

LIFE_BAR_COLOR = (171, 0, 0)
POWER_BAR_COLOR = (255, 253, 51)

HUD_HEIGHT = 0

PLAYER_LIFE_WIDTH = SCREEN_WIDTH / 4
PLAYER_LIFE_HEIGHT = SCREEN_HEIGHT/18
PLAYER_LIFE_X = 20
PLAYER_LIFE_Y = 20

PLAYER_ENERGY_WIDTH = PLAYER_LIFE_WIDTH
PLAYER_ENERGY_HEIGHT = PLAYER_LIFE_HEIGHT
PLAYER_ENERGY_X = SCREEN_WIDTH - 20 - PLAYER_ENERGY_WIDTH
PLAYER_ENERGY_Y = PLAYER_LIFE_Y

BOSS_LIFE_WIDTH = SCREEN_WIDTH*3/4
BOSS_LIFE_HEIGHT = SCREEN_HEIGHT/18
BOSS_LIFE_X = SCREEN_WIDTH/2-BOSS_LIFE_WIDTH/2
BOSS_LIFE_Y = SCREEN_HEIGHT*7/8

MESSAGE_BOX_DIMENSION = [SCREEN_WIDTH*4/5,SCREEN_HEIGHT/6]
MESSAGE_BOX_POSITION = [SCREEN_WIDTH/2-MESSAGE_BOX_DIMENSION[0]/2,SCREEN_HEIGHT*4/5]

# To get which mouse button is pressed.
MOUSE_LEFT = 1
MOUSE_RIGHT = 3

# If you add a Tag for debugging, you MUST set it here at 0 for everyone
# You can turn your tag on in your own settings_local.py for personal use

TAG_ALEX = 0
TAG_BP = 0
TAG_MAGNAN = 0
TAG_MARIE = 0
TAG_PHIL = 0

# Load settings_local.py if exist
try:
    from app.settings_local import *
except ImportError:
    pass
