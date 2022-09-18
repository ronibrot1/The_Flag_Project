import os
import pygame.image

SIZE_CELL = 20
NUM_ROWS, NUM_COLS = 25, 50
WINDOW_WIDTH, WINDOW_HEIGHT = NUM_COLS * SIZE_CELL, NUM_ROWS * SIZE_CELL

GREEN = (0, 102, 0)
BLUE = (50, 61, 138)
WHITE = (255, 255, 255)
BLACK = (40, 40, 40)

FPS = 60

SOLDIER_IMAGE = pygame.image.load((os.path.join('bin', 'soldier.png')))
SOLDIER_IMAGE_NIGHT = pygame.image.load((os.path.join('bin', 'soldier_night.png')))
SOLDIER_WIDTH, SOLDIER_HEIGHT = 2 * SIZE_CELL, 4 * SIZE_CELL
SOLDIER = pygame.transform.scale(SOLDIER_IMAGE, (SOLDIER_WIDTH, SOLDIER_HEIGHT))
SOLDIER_NIGHT = pygame.transform.scale(SOLDIER_IMAGE_NIGHT, (SOLDIER_WIDTH, SOLDIER_HEIGHT))

FLAG_IMAGE = pygame.image.load((os.path.join('bin', 'flag.png')))
FLAG_WIDTH, FLAG_HEIGHT = 4 * SIZE_CELL, 3 * SIZE_CELL
FLAG = pygame.transform.scale(FLAG_IMAGE, (FLAG_WIDTH, FLAG_HEIGHT))

GRASS_IMAGE = pygame.image.load((os.path.join('bin', 'grass.png')))
GRASS_WIDTH, GRASS_HEIGHT = 3 * SIZE_CELL, 2 * SIZE_CELL
GRASS = pygame.transform.scale(GRASS_IMAGE, (GRASS_WIDTH, GRASS_HEIGHT))

MINE_IMAGE = pygame.image.load((os.path.join('bin', 'mine.png')))
MINE_WIDTH, MINE_HEIGHT = 3 * SIZE_CELL, 1 * SIZE_CELL
MINE = pygame.transform.scale(MINE_IMAGE, (MINE_WIDTH, MINE_HEIGHT))

FONT_NAME = "Calibri"

LOSE_MESSAGE = "You Lost!"
LOSE_FONT_SIZE = int(0.15 * WINDOW_WIDTH)
LOSE_COLOR = BLACK
LOSE_LOCATION = 0.2 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (LOSE_FONT_SIZE / 2)

WIN_MESSAGE = "You Won!"
WIN_FONT_SIZE = LOSE_FONT_SIZE
WIN_COLOR = BLACK
WIN_LOCATION = 0.2 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (WIN_FONT_SIZE / 2)
