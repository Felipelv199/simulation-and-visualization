"""
conway.py 
A simple Python/matplotlib implementation of Conway's Game of Life.
"""

import sys
import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def addBlinker(grid: np.ndarray, i: int, j: int) -> None:
    blinker = np.array([[255], [255], [255]])
    n, m = blinker.shape
    grid[i:i+n, j:j+m] = blinker


def checkRulesOfLife(grid: np.ndarray, i: int, j: int) -> int:
    live_neighbors = 0
    for y in range(-1, 2):
        for x in range(-1, 2):
            if y == 0 and x == 0:
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
    for y in range(1, n-1):
        for x in range(1, m-1):
            newGrid[y, x] = checkRulesOfLife(grid, y, x)
    return newGrid


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Runs Conway's Game of Life system.py.")
    N = 10
    grid = np.array([])
    grid = np.zeros(N*N).reshape(N, N)
    addBlinker(grid, 2, 2)

    fig, ax = plt.subplots()
    ax.imshow(grid, interpolation='nearest')
    plt.show()

    grid = np.copy(iterateGrid(grid))

    fig, ax = plt.subplots()
    ax.imshow(grid, interpolation='nearest')
    plt.show()

    grid = np.copy(iterateGrid(grid))

    fig, ax = plt.subplots()
    ax.imshow(grid, interpolation='nearest')
    plt.show()


# call main
if __name__ == '__main__':
    main()
