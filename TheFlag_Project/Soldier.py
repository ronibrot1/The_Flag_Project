import pygame
import constants

soldier = constants.SOLDIER
soldier_place = pygame.Rect(soldier.x, soldier.y, constants.SOLDIER_WIDTH, constants.SOLDIER_HEIGHT)

def soldier_check(field_matrix):
    if field_matrix[soldier.x, soldier.y + 3] == 1 or field_matrix[soldier.x, soldier.y] == 10:
        lost()
    if field_matrix[soldier.x + 1, soldier.y + 3] == 1 or field_matrix[soldier.x, soldier.y] == 10:
        lost()
    if field_matrix[soldier.x, soldier.y] == 2:
        won()
    if field_matrix[soldier.x + 1, soldier.y] == 2:
        won()
    if field_matrix[soldier.x, soldier.y + 1] == 2:
        won()
    if field_matrix[soldier.x + 1, soldier.y + 1] == 2:
        won()
    if field_matrix[soldier.x, soldier.y + 2] == 2:
        won()
    if field_matrix[soldier.x + 1, soldier.y + 2] == 2:
        won()


