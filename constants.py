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
WORD_MAX_TIME = 400

HARD_LOCATIONS = [
    (1050, 200),
    (2600, 300),
    (2600, 800),
    (100, 550),
    (100, 800),
    (1250, 1000),
    (1700, 1450),
    (1800, 200)
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