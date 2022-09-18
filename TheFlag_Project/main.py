import pygame

import MineField
import Screen
import Soldier
import constants

def main():
    run = True
    clock = pygame.time.Clock()
    Screen.show_board(Soldier.soldier)
    MineField.grass_location(Screen.grass_matrix)
    Screen.print_grass()
    MineField.create_field_mat()
    MineField.mine_location()
    MineField.flag_location(Screen.screen)
    Screen.dark_mode_grid(Screen.screen)

    pygame.display.update()
    while run:
        clock.tick(constants.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()


if __name__ == "__main__":
    main()