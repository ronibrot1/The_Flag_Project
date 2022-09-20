import pygame
import MineField
import Screen
import Soldier
import constants
import time
import Database
import Teleport
import Guard

Screen.grass_location()
MineField.create_field_mat()
MineField.mine_location()
MineField.flag_location()
Teleport.create_hole_randomly()


def main():
    run = True
    clock = pygame.time.Clock()
    t = 0
    key_event = 0
    direction = True
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

        if not Teleport.check_if_soldier_in_hole(Soldier.soldier_place):
            if Soldier.check_if_soldier_touches_mine(MineField.field_matrix):
                Screen.lose_message()
                break
            elif Soldier.check_if_soldier_touches_flag(MineField.field_matrix):
                Screen.win_message()
                break

        Screen.show_board(Soldier.soldier_place)

        if Guard.check_soldier_guard_collide():
            Screen.lose_message()
            break

        if direction:
            Guard.move_guard_right(Screen.screen)
            if Guard.guard_place.x == constants.WINDOW_WIDTH - constants.GUARD_WIDTH:
                direction = False
        else:
            Guard.move_guard_left(Screen.screen)
            if Guard.guard_place.x == 0:
                direction = True

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
