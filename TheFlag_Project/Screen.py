import pygame
import MineField
import constants


grass_matrix = []
screen = pygame.display.set_mode((constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))


def show_board(soldier):
    screen.fill(constants.GREEN)
    pygame.display.set_caption("The Flag Game")
    screen.blit(constants.SOLDIER, (0, 0))
    pygame.display.update()


def print_grass():
    for row in range(constants.NUM_ROWS):
        for column in range(constants.NUM_COLS):
            if grass_matrix[row][column] == 1:
                screen.blit(constants.GRASS, (column * constants.SIZE_CELL, row * constants.SIZE_CELL))
    pygame.display.update()


def dark_mode_grid(screen):
    screen.fill(constants.WHITE)
    for i in range(constants.NUM_ROWS):
        for j in range(constants.NUM_COLS):
            pygame.draw.rect(screen, constants.BLACK,
                             (j * constants.SIZE_CELL, i * constants.SIZE_CELL, constants.SIZE_CELL - 1,
                              constants.SIZE_CELL - 1))
    MineField.add_mines_to_display(screen)
    pygame.display.update()
