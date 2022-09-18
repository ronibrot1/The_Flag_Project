import os
import pygame


WIDTH = 1000
HEIGHT = 500
SCREEN_COLOR = (0, 102, 0)
FPS = 60
SOLDIER_IMAGE = pygame.image.load(os.path.join('bin', 'soldier.png'))
SOLDIER = pygame.transform.scale(SOLDIER_IMAGE, (40, 80))
WOUNDED_SOLDIER_IMAGE = pygame.image.load(os.path.join('bin', 'injury.png'))
GRASS_IMAGE = pygame.image.load(os.path.join('bin', 'grass.png'))
FLAG_IMAGE = pygame.image.load(os.path.join('bin', 'flag.png'))
MINE_IMAGE = pygame.image.load(os.path.join('bin', 'mine.png'))
EXPLOSION_IMAGE = pygame.image.load(os.path.join('bin', 'explotion.png'))