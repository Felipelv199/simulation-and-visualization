"""
conway.py 
A simple Python/matplotlib implementation of Conway's Game of Life.
"""

from io import FileIO
import sys
import argparse
from typing import IO
import numpy as np
import matplotlib.image as mltimg
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from numpy.core.fromnumeric import repeat
from configurations import Configurations


def update(frameNum: int, img: mltimg.AxesImage, grid: np.ndarray, N: int, M: int):
    # copy grid since we require 8 neighbors for calculation
    # and we go line by line
    newGrid = iterateGrid(grid)
    # TODO: Implement the rules of Conway's Game of Life

    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,


def checkRulesOfLife(grid: np.ndarray, i: int, j: int) -> int:
    live_neighbors = 0
    n, m = grid.shape
    for y in range(-1, 2):
        for x in range(-1, 2):
            if y == 0 and x == 0:
                continue
            if i+y < 0 or i+y >= n or j+x < 0 or j+x >= m:
                continue
            if grid[i+y, j+x] == 255:
                live_neighbors += 1
    if grid[i, j] == 255 and (live_neighbors == 2 or live_neighbors == 3):
        return 255
    elif grid[i, j] == 0 and live_neighbors == 3:
        return 255
    return 0


def iterateGrid(grid: np.ndarray) -> np.ndarray:
    newGrid = np.copy(grid)
    n, m = grid.shape
    configs = Configurations(n, m)
    for y in range(0, n):
        for x in range(0, m):
            newGrid[y, x] = checkRulesOfLife(grid, y, x)
            configs.checkLightWeightSpaceship(grid, y, x)
            configs.checkGlider(grid, y, x)
            configs.checkBeacon(grid, y, x)
            configs.checkBlinker(grid, y, x)
    print(configs.frameConfigs)
    return newGrid


def readInput(f: IO):
    N, M = [int(x) for x in f.readline().split(' ')]
    FRAMES = int(f.readline())
    grid = np.zeros(N*M).reshape(N, M)

    while True:
        l = f.readline()
        if not l:
            break
        x, y = [int(x) for x in l.split(' ')]
        n, m = grid.shape
        if x >= 0 and x < n and y >= 0 and y < m:
            grid[x, y] = 255

    iterateGrid(grid)

    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, M,),
                                  frames=FRAMES, interval=1, repeat=True)
    plt.show()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Runs Conway's Game of Life system.py.")

    file = None
    try:
        file = open(sys.argv[1])
    except:
        print('An error has occurred')

    if file:
        readInput(file)


if __name__ == '__main__':
    main()
