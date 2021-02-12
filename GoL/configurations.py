from typing import List, Literal
import numpy as np


class Configurations:

    def __init__(self, n: int, m: int) -> None:
        self.frameConfigs = {}
        self.grid = np.zeros(n*m).reshape(n, m)

    def checkBlock(self, grid: np.ndarray, i: int, j: int) -> None:
        block = np.array([[255, 255, ],
                          [255, 255, ], ])
        self.checkConfig(grid, block, 'block', i, j)

    def checkBeehive(self, grid: np.ndarray, i: int, j: int) -> None:
        beehive = np.array([[0, 255, 255,   0, ],
                            [255, 0,   0, 255, ],
                            [0, 255, 255,   0, ]])
        self.checkConfig(grid, beehive, 'beehive', i, j)

    def checkLoaf(self, grid: np.ndarray, i: int, j: int) -> None:
        loaf = np.array([[0, 255, 255, 0, ],
                         [255, 0,   0, 255, ],
                         [0, 255,   0, 255, ],
                         [0,   0, 255, 0, ]])
        self.checkConfig(grid, loaf, 'loaf', i, j)

    def checkBoat(self, grid: np.ndarray, i: int, j: int) -> None:
        boat = np.array([[255, 255,   0, ],
                         [255,   0, 255, ],
                         [0,   255,   0, ]])
        self.checkConfig(grid, boat, 'boat', i, j)

    def checkTub(self, grid: np.ndarray, i: int, j: int) -> None:
        tub = np.array([[0, 255,   0, ],
                        [255, 0, 255, ],
                        [0, 255,   0, ]])
        self.checkConfig(grid, tub, 'tub', i, j)

    def checkBlinker(self, grid: np.ndarray, i: int, j: int) -> None:
        blinker = [np.array([[255],
                             [255],
                             [255]]),
                   np.array([[255, 255, 255], ]), ]
        for x in blinker:
            if self.checkConfig(grid, x, 'blinker', i, j):
                return

    def checkToad(self, grid: np.ndarray, i: int, j: int) -> None:
        toad = [np.array([[0,   0, 255,   0],
                          [255, 0,   0, 255],
                          [255, 0,   0, 255],
                          [0, 255,   0,   0], ]),
                np.array([[0,   255, 255, 255],
                          [255, 255, 255,   0], ]), ]
        for x in toad:
            if self.checkConfig(grid, x, 'toad', i, j):
                return

    def checkBeacon(self, grid: np.ndarray, i: int, j: int) -> None:
        beacon = [np.array([[255, 255, 0,     0],
                            [255, 255, 0,     0],
                            [0,     0, 255, 255],
                            [0,     0, 255, 255], ]),
                  np.array([[255, 255,   0,   0],
                            [255,   0,   0,   0],
                            [0,     0,   0, 255],
                            [0,     0, 255, 255], ]), ]
        for x in beacon:
            if self.checkConfig(grid, x, 'beacon', i, j):
                return

    def checkGlider(self, grid: np.ndarray, i: int, j: int) -> None:
        glider = [np.array([[0,   255,   0, ],
                            [0,     0, 255, ],
                            [255, 255, 255, ], ]),
                  np.array([[255,   0, 255, ],
                            [0,   255, 255, ],
                            [0,   255,   0, ], ]),
                  np.array([[0,     0, 255, ],
                            [255,   0, 255, ],
                            [0,   255, 255, ], ]),
                  np.array([[255,   0,   0, ],
                            [0,   255, 255, ],
                            [255, 255,   0, ], ]), ]
        for x in glider:
            if self.checkConfig(grid, x, 'glider', i, j):
                return

    def checkLightWeightSpaceship(self, grid: np.ndarray, i: int, j: int) -> None:
        lightWeightSpaceship = [np.array([[255, 0,   0, 255,   0],
                                          [0,   0,   0,   0, 255],
                                          [255, 0,   0,   0, 255],
                                          [0, 255, 255, 255, 255], ]),
                                np.array([[0,     0, 255, 255,   0],
                                          [255, 255,   0, 255, 255],
                                          [255, 255, 255, 255,   0],
                                          [0,   255, 255,   0,   0], ]),
                                np.array([[0,   255, 255, 255, 255],
                                          [255,   0, 0,   0,   255],
                                          [0,     0, 0,   0,   255],
                                          [255,   0, 0, 255,     0], ]),
                                np.array([[0,   255, 255,   0,   0],
                                          [255, 255, 255, 255,   0],
                                          [255, 255,   0, 255, 255],
                                          [0,     0, 255, 255,   0], ]), ]
        for x in lightWeightSpaceship:
            if self.checkConfig(grid, x, 'lightWeightSpaceship', i, j):
                return

    def checkConfig(self, grid: np.ndarray, subGrid: np.ndarray, subGridName: Literal, i, j) -> bool:
        n, m = subGrid.shape

        if np.all(self.grid[i:i+n, j:j+m] == 1):
            return

        if np.array_equal(subGrid, grid[i:i+n, j:j+m]):
            try:
                self.frameConfigs[subGridName] += 1
            except:
                self.frameConfigs[subGridName] = 1

            self.grid[i:i+n, j:j+m] = 1
            return True

        return False

    def checkOthers(self, grid: np.ndarray, i: int, j: int) -> None:
        if grid[i, j] == 0:
            return

        other = self.growing(grid, i, j, 255)

        if len(other) > 0:
            try:
                self.frameConfigs['others'] += 1
            except:
                self.frameConfigs['others'] = 1

    def growing(self, grid: np.ndarray, i: int, j: int, colorVal: int) -> list:
        regionPixels = []
        colaPoints = []

        if self.grid[i, j] == 0:
            regionPixels.append((i, j))
            n, m = grid.shape
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if k == 0 and l == 0:
                        continue
                    if i+k >= 0 and i+k < n and j+l >= 0 and j+l < m:
                        colaPoints.append((i+k, j+l))
            while len(colaPoints) > 0:
                pt1 = colaPoints.pop(0)
                if grid[pt1[0], pt1[1]] == colorVal:
                    if self.grid[pt1[0], pt1[1]] == 0:
                        regionPixels.append(pt1)
                        self.grid[pt1[0], pt1[1]] = 1
                        for k in range(-1, 2):
                            for l in range(-1, 2):
                                if k == 0 and l == 0:
                                    continue
                                if pt1[0]+k >= 0 and pt1[0]+k < n and pt1[1]+l >= 0 and pt1[1]+l < m:
                                    if self.grid[pt1[0]+k, pt1[1]+l] == 0:
                                        colaPoints.append((pt1[0]+k, pt1[1]+l))
        return regionPixels
