import constants
import random


holes_list = []
hole_matrix = []


def add_holes_to_display(screen):
    for row in range(constants.NUM_ROWS):
        for column in range(constants.NUM_COLS):
            if hole_matrix[row][column] == 10:  # 10 if first index of mine (from left)
                screen.blit(constants.HOLE, (column * constants.SIZE_CELL, row * constants.SIZE_CELL))


def create_hole_randomly():
    row_to_append = []
    for row in range(constants.NUM_ROWS):
        for column in range(constants.NUM_COLS):
            row_to_append.append(0)
        hole_matrix.append(row_to_append)
        row_to_append = []
    index = 0
    while index != 5:
        random_row = random.randint(4, 20)
        random_col = random.randint(0, 47)
        if hole_matrix[random_row][random_col] == 0 and hole_matrix[random_row][random_col + 1] == 0 and \
                hole_matrix[random_row][random_col + 2] == 0:
            list_to_append = [random_row, random_col]
            holes_list.append(list_to_append)
            hole_matrix[random_row][random_col] = 10
            hole_matrix[random_row][random_col + 1] = 1
            hole_matrix[random_row][random_col + 2] = 1
            index += 1


def check_if_soldier_in_hole(soldier_place):
    if hole_matrix[soldier_place.y // constants.SIZE_CELL + 3][soldier_place.x // constants.SIZE_CELL] == 10:
        change_hole(soldier_place)
        return True
    elif hole_matrix[soldier_place.y // constants.SIZE_CELL + 3][soldier_place.x // constants.SIZE_CELL] == 1:
        change_hole(soldier_place)
        return True
    elif hole_matrix[soldier_place.y // constants.SIZE_CELL + 3][soldier_place.x // constants.SIZE_CELL + 1] == 10:
        change_hole(soldier_place)
        return True
    elif hole_matrix[soldier_place.y // constants.SIZE_CELL + 3][soldier_place.x // constants.SIZE_CELL + 1] == 1:
        change_hole(soldier_place)
        return True
    else:
        return False


def change_hole(soldier_place):
    while True:
        rand_hole = random.randint(0, 4)
        new_hole_x = holes_list[rand_hole][0]
        new_hole_y = holes_list[rand_hole][1]
        if soldier_place.x != new_hole_y * constants.SIZE_CELL and soldier_place.y != new_hole_x * constants.SIZE_CELL:
            soldier_place.x = new_hole_y * constants.SIZE_CELL
            soldier_place.y = (new_hole_x - 4) * constants.SIZE_CELL
            break
