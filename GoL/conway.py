"""
conway.py
A simple Python/matplotlib implementation of Conway's Game of Life.
"""

import sys
import argparse
from typing import IO
import numpy as np
import matplotlib.image as mltimg
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from configurations import Configurations


def checkRulesOfLife(grid: np.ndarray, i: int, j: int) -> int:
    # Game of Life Rules
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

    # Returns an int value that activates or deactivates the life of one pixel in the image
    if grid[i, j] == 255 and (live_neighbors == 2 or live_neighbors == 3):
        return 255
    elif grid[i, j] == 0 and live_neighbors == 3:
        return 255
    return 0


def updateConfigCounter(grid: np.ndarray, conf: dict, file: IO, frame: int) -> None:
    n, m = grid.shape
    configs = Configurations(n, m)

    # Count the number of configurations in the resultant grid
    for y in range(0, n):
        for x in range(0, m):
            configs.checkLightWeightSpaceship(grid, y, x)
            configs.checkGlider(grid, y, x)
            configs.checkBeacon(grid, y, x)
            configs.checkToad(grid, y, x)
            configs.checkBlinker(grid, y, x)
            configs.checkTub(grid, y, x)
            configs.checkBoat(grid, y, x)
            configs.checkLoaf(grid, y, x)
            configs.checkBeehive(grid, y, x)
            configs.checkBlock(grid, y, x)
            configs.checkOthers(grid, y, x)

    # Update configurations final count and add frame configurations count to the output
    for x in configs.frameConfigs:
        try:
            conf[x] += configs.frameConfigs[x]
        except:
            conf[x] = configs.frameConfigs[x]
        file.write(' {:^7}| {:<13} | {:>6}\n'.format(
            frame, x, configs.frameConfigs[x]))
    file.write(' --------------------------------\n')


def iterateGrid(grid: np.ndarray, conf: dict, file: IO, frame: int) -> np.ndarray:
    # Apply Game of Life rules to the grid
    newGrid = np.copy(grid)
    n, m = grid.shape

    for y in range(0, n):
        for x in range(0, m):
            newGrid[y, x] = checkRulesOfLife(grid, y, x)

    updateConfigCounter(grid, conf, file, frame)

    # Return the updated grid
    return newGrid


def update(frameNum: int, img: mltimg.AxesImage, grid: np.ndarray, initialGrid: np.ndarray, framesTotal: int, configurations: dict, file: IO) -> mltimg.AxesImage:
    newGrid = iterateGrid(grid, configurations, file, frameNum)

    # Update frame image
    img.set_data(newGrid)

    if frameNum == framesTotal-1:
        # Restart grid to initial values
        grid[:] = initialGrid[:]
        plt.close()
    else:
        # Update grid values
        grid[:] = newGrid[:]
    return img,


def randomGrid(N: int, M: int) -> np.ndarray:
    # Returns a grid of NxN random values
    return np.random.choice([255, 0], N*M, p=[0.2, 0.8]).reshape(N, M)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Runs Conway's Game of Life system.py.")

    # Animation, Grid and Configuration values declaration
    N = 0
    M = 0
    FRAMES = 0
    grid = np.array([])
    configurationsCount = {}

    # Animation and Grid values initialization
    try:
        file = open(sys.argv[1])
        N, M = [int(x) for x in file.readline().split(' ')]
        FRAMES = int(file.readline())
        grid = np.zeros(N*M).reshape(N, M)

        while True:
            l = file.readline()
            if not l:
                break
            x, y = [int(x) for x in l.split(' ')]
            n, m = grid.shape
            if x >= 0 and x < n and y >= 0 and y < m:
                grid[x, y] = 255
        print('Using input file')
    except:
        N = 50
        M = 50
        FRAMES = 20
        grid = randomGrid(N, M)
        print('Using default values')

    # Create and give format to the output file
    exitFile = open('output.out', 'w+')
    exitFile.write('  FRAME | CONFIGURATION | NUMBER \n')
    exitFile.write(' ================================\n')

    # Animation configuration, initialization, and displayed
    fig, ax = plt.subplots()
    img = ax.imshow(grid, cmap='gray', interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, np.copy(grid), FRAMES, configurationsCount, exitFile,),
                                  frames=FRAMES, interval=10, repeat=False)
    plt.show()

    # Update final count per configuration
    for x in configurationsCount:
        exitFile.write(
            '  FINAL | {:<13} | {:>6}\n'.format(x, configurationsCount[x]))
    exitFile.write(' --------------------------------\n')
    exitFile.close()


if __name__ == '__main__':
    main()
