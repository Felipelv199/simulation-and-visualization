

import numpy as np


def addBlinker(grid: np.ndarray, i: int, j: int) -> None:
    blinker = np.array([[255],
                        [255],
                        [255]])
    n, m = blinker.shape
    grid[i:i+n, j:j+m] = blinker


def addToad(grid: np.ndarray, i: int, j: int) -> None:
    toad = np.array([[0,   0, 255,   0],
                     [255, 0,   0, 255],
                     [255, 0,   0, 255],
                     [0, 255,   0,   0], ])
    n, m = toad.shape
    grid[i:i+n, j:j+m] = toad


def addBeacon(grid: np.ndarray, i: int, j: int) -> None:
    beacon = np.array([[255,  255, 0, 0],
                       [255,  255, 0, 0],
                       [0,    0, 255, 255],
                       [0,    0, 255, 255], ])
    n, m = beacon.shape
    grid[i:i+n, j:j+m] = beacon


def addGlider(grid: np.ndarray, i: int, j: int) -> None:
    glider = np.array([[0,   255,   0, ],
                       [0,     0, 255, ],
                       [255, 255, 255, ], ])
    n, m = glider.shape
    grid[i:i+n, j:j+m] = glider


def addLightWeightSpaceship(grid: np.ndarray, i: int, j: int) -> None:
    lightWeightSpaceship = np.array([[255, 0, 0, 255, 0],
                                     [0,   0, 0, 0, 255],
                                     [255, 0, 0, 0, 255],
                                     [0, 255, 255, 255, 255], ])
    n, m = lightWeightSpaceship.shape
    grid[i:i+n, j:j+m] = lightWeightSpaceship


def checkBlinker(grid: np.ndarray, i: int, j: int, dic: dict) -> None:
    blinker = np.array([[255],
                        [255],
                        [255]])
    n, m = blinker.shape
    flag = np.array_equal(grid[i:i+n, j:j+m], blinker)
    if flag:
        dic['blinker'] += 1
