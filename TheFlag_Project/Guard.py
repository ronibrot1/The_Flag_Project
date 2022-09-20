import Soldier
import constants
import pygame

guard = constants.GUARD_R
guard_place = pygame.Rect(0, constants.WINDOW_HEIGHT // 2 - constants.GUARD_HEIGHT - 10, constants.GUARD_WIDTH,
                          constants.GUARD_HEIGHT)


def move_guard_right(screen):
    guard_place.x += 1 * constants.SIZE_CELL
    screen.blit(constants.GUARD_R, (guard_place.x, guard_place.y))


def move_guard_left(screen):
    guard_place.x -= 1 * constants.SIZE_CELL
    screen.blit(constants.GUARD_L, (guard_place.x, guard_place.y))


def check_soldier_guard_collide():
    soldier_places = []
    guard_places = []
    for row in range(4):
        for column in range(2):
            soldier_places.append([Soldier.soldier_place.x + column * constants.SIZE_CELL,
                                   Soldier.soldier_place.y + row * constants.SIZE_CELL])
    for row in range(4):
        for column in range(2):
            guard_places.append([guard_place.x + column * constants.SIZE_CELL,
                                 guard_place.y + row * constants.SIZE_CELL])

    for index_soldier in soldier_places:
        for index_guard in guard_places:
            if index_soldier[0] == index_guard[0] and index_soldier[1] == index_guard[1]:
                return True
    return False
