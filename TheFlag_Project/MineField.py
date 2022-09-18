import constants
import random

field_matrix = []


def create_field_mat():  # creates an "empty" matrix for the field.
    for row in range(constants.NUM_ROWS):
        row_to_append = []
        for column in range(constants.NUM_COLS):
            row_to_append.append(0)
        field_matrix.append(row_to_append)


def mine_location():  # generates up to 20 locations for the mines
    index = 0
    while index < 20:
        rand_num_row = random.randint(0, 24)
        rand_num_col = random.randint(0, 47)
        if field_matrix[rand_num_row][rand_num_col] == 0 and field_matrix[rand_num_row][rand_num_col + 1] == 0 and \
                field_matrix[rand_num_row][rand_num_col + 2] == 0:
            field_matrix[rand_num_row][rand_num_col] = 10  # is "10" in order to make the printing of mines easier
            field_matrix[rand_num_row][rand_num_col + 1] = 1
            field_matrix[rand_num_row][rand_num_col + 2] = 1
            index += 1


def flag_location():  # enters "2" in the field matrix where the flag is stationed
    for row in range(constants.NUM_ROWS - 3, constants.NUM_ROWS):
        for column in range(constants.NUM_COLS - 4, constants.NUM_COLS):
            field_matrix[row][column] = 2


def add_mines_to_display(screen):  # this function will be used when ENTER is pressed. prints the mines
    for row in range(constants.NUM_ROWS):
        for column in range(constants.NUM_COLS):
            if field_matrix[row][column] == 10:  # since an image appears from left to right its only necessary to print it in the leftest one out of three
                screen.blit(constants.MINE, (column * constants.SIZE_CELL, row * constants.SIZE_CELL))
