# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"

# Constants used to scale our sprites from their original size
CHARACTER_SCALING = .5
SPRITE_SCALING = 1
TILE_SCALING = 0.5
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = SPRITE_PIXEL_SIZE * TILE_SCALING

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 10
GRAVITY = 1
PLAYER_JUMP_SPEED = 20
WORD_MAX_TIME = 200

HARD_LOCATIONS = [
    (1050, 200),
    (2600, 300),
    (2600, 800),
    (100, 550),
    (100, 800),
    (1250, 1000),
    (1700, 1450),
    (1800, 200),
    (800, 500),
    (550, 300),
    (830, 930),
    (1700, 1250),
    (3100, 1400),
    (3000, 1600),
    (2925, 2400),
    (2255, 2600),
    (2500, 850),
    (1530, 2600),
    (100, 2600),
    (1540, 2945),
    (1760, 2945),
    (500, 2000),
    (1300, 2000),
    (3140, 3140)
]

MED_LOCATIONS = [
    (1475, 625),
    (135, 625),
    (135, 1350),
    (800, 1450),
    (1475, 1350),
    (800,800),
    (800, 550),
    (425, 400),
    (1185, 400),
    ]

EASY_LOCATIONS = [
    (325,75),
    (325,250),
    (325,500),
    (325,725),
    (550,350),
    (75,600)
]