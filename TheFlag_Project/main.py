import pygame
import Screen
import constants

def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(constants.FPS)
        Screen.create_board()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()


if __name__ == "__main__":
    main()