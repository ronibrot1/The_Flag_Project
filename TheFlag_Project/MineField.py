import Soldier
import constants
import random


field_matrix = []


def create_field_mat():
    for row in range(constants.NUM_ROWS):
        row_to_append = []
        for column in range(constants.NUM_COLS):
            row_to_append.append(0)
        field_matrix.append(row_to_append)


def mine_location():
    index = 0
    while index < 20:
        rand_num_row = random.randint(0, 23)
        rand_num_col = random.randint(0, 47)
        if field_matrix[rand_num_row][rand_num_col] == 0:
            field_matrix[rand_num_row][rand_num_col] = 10
            field_matrix[rand_num_row][rand_num_col - 1] = 1
            field_matrix[rand_num_row][rand_num_col + 1] = 1
        index += 1


def flag_location(screen):
    for row in range(constants.NUM_ROWS - 3, constants.NUM_ROWS):
        for column in range(constants.NUM_COLS - 4, constants.NUM_COLS):
            field_matrix[row][column] = 2
    screen.blit(constants.FLAG,
                ((constants.NUM_COLS - 4) * constants.SIZE_CELL, (constants.NUM_ROWS - 3) * constants.SIZE_CELL))


def grass_location(grass_matrix):
    for row in range(constants.NUM_ROWS):
        row_to_append = []
        for column in range(constants.NUM_COLS):
            row_to_append.append(0)
        grass_matrix.append(row_to_append)

    index = 0
    while index < 20:
        rand_num_row = random.randint(0, 23)
        rand_num_col = random.randint(0, 47)
        if grass_matrix[rand_num_row][rand_num_col] == 0:
            grass_matrix[rand_num_row][rand_num_col] = 1
        index += 1


def add_mines_to_display(screen):
    for row in range(constants.NUM_ROWS):
        for column in range(constants.NUM_COLS):
            if field_matrix[row][column] == 10:
                screen.blit(constants.MINE, (column * constants.SIZE_CELL, row * constants.SIZE_CELL))
    screen.blit(constants.SOLDIER_NIGHT, (soldier.x, soldier.y))

Soldier.soldier_check(field_matrix)