import pygame
import MineField
import Screen
import Soldier
import constants

Screen.grass_location()
MineField.create_field_mat()
MineField.mine_location()
MineField.flag_location()


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(constants.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key != pygame.K_RETURN:  # if ENTER wasn't pressed
                    Soldier.soldier_move(event)
                if event.key == pygame.K_RETURN:
                    Screen.dark_mode_grid(Soldier.soldier_place)
                    Screen.block_keyboard()
                    pygame.time.wait(1000)
                    Screen.unblock_keyboard()

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
