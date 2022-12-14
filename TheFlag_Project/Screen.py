import pygame
import constants
import random
import MineField
import Soldier
import keyboard
import Teleport

# generates a screen with the wanted dimensions
screen = pygame.display.set_mode((constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))
pygame.display.set_caption("The Flag")  # changes window title to "The Flag"
pygame.init()
font = pygame.font.SysFont(constants.FONT_NAME, 20)  # receives font name and the font size
message_first_part = font.render('Welcome to the Flag Game.', True, constants.WHITE)  # creates two messages that will
message_second_part = font.render('Have fun!', True, constants.WHITE)                   # appear on screen if called
grass_matrix = []


def show_board(soldier_place):  # function in charge of showing the game board (field itself)
    screen.fill(constants.GREEN)  # makes the background green
    print_grass()
    Teleport.add_holes_to_display(screen)
    screen.blit(message_first_part, (2 * constants.SIZE_CELL, 1 * constants.SIZE_CELL))
    screen.blit(message_second_part, (2 * constants.SIZE_CELL, 2 * constants.SIZE_CELL))
    screen.blit(constants.FLAG,
                (constants.WINDOW_WIDTH - constants.FLAG_WIDTH, constants.WINDOW_HEIGHT - constants.FLAG_HEIGHT))
    screen.blit(constants.SOLDIER, (soldier_place.x, soldier_place.y))

    pygame.display.update()


def grass_location():  # function which generates the location of 20 grass
    for row in range(constants.NUM_ROWS):
        row_to_append = []
        for column in range(constants.NUM_COLS):
            row_to_append.append(constants.EMPTY)
        grass_matrix.append(row_to_append)

    index = 0
    while index < 20:
        rand_num_row = random.randint(0, 23)
        rand_num_col = random.randint(0, 47)
        if grass_matrix[rand_num_row][rand_num_col] == constants.EMPTY:
            grass_matrix[rand_num_row][rand_num_col] = constants.GRASS_INDEX
        index += 1


def print_grass():  # function that prints the grass onto the board
    for row in range(constants.NUM_ROWS):
        for column in range(constants.NUM_COLS):
            if grass_matrix[row][column] == constants.GRASS_INDEX:
                screen.blit(constants.GRASS, (column * constants.SIZE_CELL, row * constants.SIZE_CELL))


def dark_mode_grid(soldier_place):  # function changes the screen to "night mode"
    screen.fill(constants.WHITE)
    for i in range(constants.NUM_ROWS):
        for j in range(constants.NUM_COLS):
            pygame.draw.rect(screen, constants.BLACK,
                             (j * constants.SIZE_CELL, i * constants.SIZE_CELL, constants.SIZE_CELL - 1,
                              constants.SIZE_CELL - 1))  # create a grid
    MineField.add_mines_to_display(screen)
    screen.blit(constants.SOLDIER_NIGHT, (soldier_place.x, soldier_place.y))

    pygame.display.update()


def dark_mode_screen():  # in charge of creating the night mode screen
    screen.fill(constants.WHITE)
    for i in range(constants.NUM_ROWS):
        for j in range(constants.NUM_COLS):
            pygame.draw.rect(screen, constants.BLACK,
                             (j * constants.SIZE_CELL, i * constants.SIZE_CELL, constants.SIZE_CELL - 1,
                              constants.SIZE_CELL - 1))  # fills cells within the white background and crates a grid
    MineField.add_mines_to_display(screen)  # prints mines


def block_keyboard():  # used to restrict player movement after ENTER was pressed
    keyboard.block_key("down")
    keyboard.block_key("up")
    keyboard.block_key("left")
    keyboard.block_key("right")


def unblock_keyboard():  # re-enables player movement after the duration of "night mode" ended
    keyboard.unblock_key("down")
    keyboard.unblock_key("up")
    keyboard.unblock_key("left")
    keyboard.unblock_key("right")


def lose_message():  # when the soldier touched a mine with his legs
    dark_mode_screen()  # screen is similar to night mode
    screen.blit(constants.EXPLOSION, (Soldier.soldier_place.x, Soldier.soldier_place.y))  # add an explosion
    pygame.display.update()
    pygame.time.wait(1000)
    dark_mode_screen()   # clears display from explosion in order to show an injured soldier
    screen.blit(constants.INJURED_SOLDIER, (Soldier.soldier_place.x, Soldier.soldier_place.y))  # add an injured soldier
    pygame.display.update()
    pygame.time.wait(1000)
    draw_message(constants.LOSE_MESSAGE, constants.LOSE_FONT_SIZE,
                 constants.LOSE_COLOR, constants.LOSE_LOCATION)


def win_message():  # print winning message
    show_board(Soldier.soldier_place)
    draw_message(constants.WIN_MESSAGE, constants.WIN_FONT_SIZE,
                 constants.WIN_COLOR, constants.WIN_LOCATION)


def draw_message(message, font_size, color, location):  # in charge of rendering the messages themselves
    font_message = pygame.font.SysFont(constants.FONT_NAME, font_size)
    text_img = font_message.render(message, True, color)
    screen.blit(text_img, location)
    pygame.display.update()
    pygame.time.wait(3000)
