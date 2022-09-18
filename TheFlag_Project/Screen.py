import pygame
import constants

def create_board():
    WIN = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
    WIN.fill(constants.SCREEN_COLOR)
    pygame.display.set_caption("The Flag Game")
    WIN.blit(constants.SOLDIER, (300,100))
    pygame.display.update()


def game_grid():
    pass

