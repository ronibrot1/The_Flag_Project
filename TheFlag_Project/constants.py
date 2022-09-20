import os
import pygame

SIZE_CELL = 20
NUM_ROWS, NUM_COLS = 25, 50
WINDOW_WIDTH, WINDOW_HEIGHT = NUM_COLS * SIZE_CELL, NUM_ROWS * SIZE_CELL

GREEN = (0, 102, 0)
WHITE = (255, 255, 255)
BLACK = (40, 40, 40)

FPS = 15

EMPTY = 0
MINE_INDEX = 1
FIRST_INDEX_OF_MINE = 10
GRASS_INDEX = 1
FLAG_INDEX = 2

SOLDIER_IMAGE = pygame.image.load((os.path.join('bin', 'soldier.png')))
SOLDIER_WIDTH, SOLDIER_HEIGHT = 2 * SIZE_CELL, 4 * SIZE_CELL
SOLDIER = pygame.transform.scale(SOLDIER_IMAGE, (SOLDIER_WIDTH, SOLDIER_HEIGHT))

SOLDIER_NIGHT_IMAGE = pygame.image.load((os.path.join('bin', 'soldier_night.png')))
SOLDIER_NIGHT = pygame.transform.scale(SOLDIER_NIGHT_IMAGE, (SOLDIER_WIDTH, SOLDIER_HEIGHT))

GUARD_IMAGE = pygame.image.load((os.path.join('bin', 'guard.png')))
GUARD_WIDTH, GUARD_HEIGHT = 2 * SIZE_CELL, 4 * SIZE_CELL
GUARD_L = pygame.transform.scale(GUARD_IMAGE, (GUARD_WIDTH, GUARD_HEIGHT))

GUARD_IMAGE_R = pygame.transform.flip(GUARD_IMAGE, True, False)
GUARD_R = pygame.transform.scale(GUARD_IMAGE_R, (GUARD_WIDTH, GUARD_HEIGHT))

INJURED_SOLDIER_IMAGE = pygame.image.load((os.path.join('bin', 'injury.png')))
INJURED_SOLDIER = pygame.transform.scale(INJURED_SOLDIER_IMAGE, (SOLDIER_WIDTH, SOLDIER_HEIGHT))

FLAG_IMAGE = pygame.image.load((os.path.join('bin', 'flag.png')))
FLAG_WIDTH, FLAG_HEIGHT = 4 * SIZE_CELL, 3 * SIZE_CELL
FLAG = pygame.transform.scale(FLAG_IMAGE, (FLAG_WIDTH, FLAG_HEIGHT))

GRASS_IMAGE = pygame.image.load((os.path.join('bin', 'grass.png')))
GRASS_WIDTH, GRASS_HEIGHT = 3 * SIZE_CELL, 2 * SIZE_CELL
GRASS = pygame.transform.scale(GRASS_IMAGE, (GRASS_WIDTH, GRASS_HEIGHT))

MINE_IMAGE = pygame.image.load((os.path.join('bin', 'mine.png')))
MINE_WIDTH, MINE_HEIGHT = 3 * SIZE_CELL, 1 * SIZE_CELL
MINE = pygame.transform.scale(MINE_IMAGE, (MINE_WIDTH, MINE_HEIGHT))

EXPLOSION_IMAGE = pygame.image.load((os.path.join('bin', 'explosion.png')))
EXPLOSION_WIDTH, EXPLOSION_HEIGHT = 3 * SIZE_CELL, 4 * SIZE_CELL
EXPLOSION = pygame.transform.scale(EXPLOSION_IMAGE, (EXPLOSION_WIDTH, EXPLOSION_HEIGHT))

HOLE_IMAGE = pygame.image.load((os.path.join('bin', 'hole.png')))
HOLE_WIDTH, HOLE_HEIGHT = 3 * SIZE_CELL, 1 * SIZE_CELL
HOLE = pygame.transform.scale(HOLE_IMAGE, (HOLE_WIDTH, HOLE_HEIGHT))

FONT_NAME = "Calibri"

LOSE_MESSAGE = "You Lost!"
LOSE_FONT_SIZE = int(0.15 * WINDOW_WIDTH)
LOSE_COLOR = WHITE
LOSE_LOCATION = 0.2 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (LOSE_FONT_SIZE / 2)

WIN_MESSAGE = "You Won!"
WIN_FONT_SIZE = LOSE_FONT_SIZE
WIN_COLOR = BLACK
WIN_LOCATION = 0.2 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (WIN_FONT_SIZE / 2)

CSV_FILE = 'the_flag_memory.csv'
SOLDIER_MEMORY_X = "soldier_place_x"
SOLDIER_MEMORY_Y = "soldier_place_y"
MINE_MEMORY = "mine_matrix"
GRASS_MEMORY = "grass_matrix"
