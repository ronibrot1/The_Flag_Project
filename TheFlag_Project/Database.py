import ast
import math
import os.path
import pandas as pd
import pygame
import constants
import MineField
import Screen
import Soldier
import Guard
import Teleport


def init_module():  # creates an empty 9 rows data frame
    df = pd.DataFrame(index=[1, 2, 3, 4, 5, 6, 7, 8, 9],
                      columns=[constants.SOLDIER_MEMORY_X, constants.SOLDIER_MEMORY_Y,
                               constants.MINE_MEMORY, constants.GRASS_MEMORY, constants.GUARD_MEMORY_X,
                               constants.GUARD_MEMORY_Y, constants.HOLE_MEMORY])
    df.to_csv(constants.CSV_FILE, index=False)


def save_state(key_event):  # saves data to data frame
    if not os.path.exists(constants.CSV_FILE):
        init_module()
    df = pd.read_csv(constants.CSV_FILE)
    row = key_event - pygame.K_1
    df.loc[row, constants.SOLDIER_MEMORY_X] = str(int(Soldier.soldier_place.x))
    df.loc[row, constants.SOLDIER_MEMORY_Y] = str(int(Soldier.soldier_place.y))
    df.loc[row, constants.MINE_MEMORY] = str(MineField.field_matrix)
    df.loc[row, constants.GRASS_MEMORY] = str(Screen.grass_matrix)
    df.loc[row, constants.GUARD_MEMORY_X] = str(int(Guard.guard_place.x))
    df.loc[row, constants.GUARD_MEMORY_Y] = str(int(Guard.guard_place.y))
    df.loc[key_event - 49, constants.HOLE_MEMORY] = str(Teleport.hole_matrix)
    df.to_csv(constants.CSV_FILE, index=False)


def load_state(key_event):  # loads data from data frame
    if not os.path.exists(constants.CSV_FILE):
        init_module()
    df = pd.read_csv(constants.CSV_FILE)
    row = key_event - pygame.K_1
    if not math.isnan(df.loc[row, constants.SOLDIER_MEMORY_X]):
        Soldier.soldier_place.x = int(df.loc[row, constants.SOLDIER_MEMORY_X])
        Soldier.soldier_place.y = int(df.loc[row, constants.SOLDIER_MEMORY_Y])
        MineField.field_matrix = ast.literal_eval(df.loc[row, constants.MINE_MEMORY])
        Screen.grass_matrix = ast.literal_eval(df.loc[row, constants.GRASS_MEMORY])
        Guard.guard_place.x = int(df.loc[key_event - 49, constants.GUARD_MEMORY_X])
        Guard.guard_place.y = int(df.loc[key_event - 49, constants.GUARD_MEMORY_Y])
        Teleport.hole_matrix = ast.literal_eval(df.loc[key_event - 49, constants.HOLE_MEMORY])
