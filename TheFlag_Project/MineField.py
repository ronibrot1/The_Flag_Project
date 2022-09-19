import constants
import random

field_matrix = []


def create_field_mat():  # creates an "empty" matrix for the field.
    for row in range(constants.NUM_ROWS):
        row_to_append = []
        for column in range(constants.NUM_COLS):
            row_to_append.append(constants.EMPTY)
        field_matrix.append(row_to_append)


def mine_location():  # generates up to 20 locations for the mines
    index = 0
    while index < 20:
        rand_num_row = random.randint(0, 24)
        rand_num_col = random.randint(0, 47)
        if field_matrix[rand_num_row][rand_num_col] == constants.EMPTY and field_matrix[rand_num_row][rand_num_col + 1]\
                == constants.EMPTY and field_matrix[rand_num_row][rand_num_col + 2] == constants.EMPTY:
            field_matrix[rand_num_row][rand_num_col] = constants.FIRST_INDEX_OF_MINE
            field_matrix[rand_num_row][rand_num_col + 1] = constants.MINE_INDEX
            field_matrix[rand_num_row][rand_num_col + 2] = constants.MINE_INDEX
            index += 1


def flag_location():
    for row in range(constants.NUM_ROWS - 3, constants.NUM_ROWS):
        for column in range(constants.NUM_COLS - 4, constants.NUM_COLS):
            field_matrix[row][column] = constants.FLAG_INDEX


def add_mines_to_display(screen):  # this function will be used when ENTER is pressed. prints the mines
    for row in range(constants.NUM_ROWS):
        for column in range(constants.NUM_COLS):
            if field_matrix[row][column] == constants.FIRST_INDEX_OF_MINE:
                screen.blit(constants.MINE, (column * constants.SIZE_CELL, row * constants.SIZE_CELL))
