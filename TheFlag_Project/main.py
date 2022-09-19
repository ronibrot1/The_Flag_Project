import pygame
import MineField
import Screen
import Soldier
import constants
import time
import Database

Screen.grass_location()
MineField.create_field_mat()
MineField.mine_location()
MineField.flag_location()


def main():
    run = True
    clock = pygame.time.Clock()
    t = 0
    key_event = 0
    while run:
        clock.tick(constants.FPS)  # keeps the highest speed at which the game operates the same for each computer
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:  # if a key is being pressed execute the following code:
                t = time.time()
                key_event = event.key
                if event.key != pygame.K_RETURN:  # if ENTER wasn't pressed
                    Soldier.soldier_move(event)
                if event.key == pygame.K_RETURN:  # executes "night mode" when ENTER is pressed
                    Screen.dark_mode_grid(Soldier.soldier_place)
                    Screen.block_keyboard()
                    pygame.time.wait(1000)
                    Screen.unblock_keyboard()

            if event.type == pygame.KEYUP:
                t_pressed = time.time() - t
                if pygame.K_1 <= key_event <= pygame.K_9:
                    if t_pressed < 1:
                        Database.save_state(key_event)
                    else:
                        Database.load_state(key_event)

        if Soldier.check_if_soldier_touches_mine(MineField.field_matrix):
            Screen.lose_message()
            break
        elif Soldier.check_if_soldier_touches_flag(MineField.field_matrix):
            Screen.win_message()
            break

        Screen.show_board(Soldier.soldier_place)

    pygame.quit()


if __name__ == "__main__":
    main()
