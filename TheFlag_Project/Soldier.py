import pygame
import constants

soldier = constants.SOLDIER
soldier_place = pygame.Rect(0, 0, constants.SOLDIER_WIDTH, constants.SOLDIER_HEIGHT)


def check_if_soldier_touches_mine(field_matrix):  # checks if the soldier's legs touched a mine. soldier's legs are 2 columns and 1 row
    if field_matrix[soldier_place.y // constants.SIZE_CELL + 3][soldier_place.x // constants.SIZE_CELL] == 10:
        return True
    elif field_matrix[soldier_place.y // constants.SIZE_CELL + 3][soldier_place.x // constants.SIZE_CELL] == 1:
        return True
    elif field_matrix[soldier_place.y // constants.SIZE_CELL + 3][soldier_place.x // constants.SIZE_CELL + 1] == 10:
        return True
    elif field_matrix[soldier_place.y // constants.SIZE_CELL + 3][soldier_place.x // constants.SIZE_CELL + 1] == 1:
        return True
    else:
        return False


def check_if_soldier_touches_flag(field_matrix):  # soldier's body is 4 rows and 2 column
    for row in range(4):
        for column in range(2):
            if field_matrix[soldier_place.y // constants.SIZE_CELL + row][
             soldier_place.x // constants.SIZE_CELL + column] == 2:
                return True
    return False


def soldier_move(event):  # keeps the soldier within the limits of the screen and updates the soldier's location
    if event.key == pygame.K_LEFT and soldier_place.x - 1 * constants.SIZE_CELL >= 0:
        soldier_place.x -= 1 * constants.SIZE_CELL
    if event.key == pygame.K_RIGHT and soldier_place.x + 1 * constants.SIZE_CELL <= \
            constants.WINDOW_WIDTH - 2 * constants.SIZE_CELL:
        soldier_place.x += 1 * constants.SIZE_CELL
    if event.key == pygame.K_UP and soldier_place.y - 1 * constants.SIZE_CELL >= 0:
        soldier_place.y -= 1 * constants.SIZE_CELL
    if event.key == pygame.K_DOWN and soldier_place.y + 1 * constants.SIZE_CELL <= \
            constants.WINDOW_HEIGHT - 4 * constants.SIZE_CELL:
        soldier_place.y += 1 * constants.SIZE_CELL
        