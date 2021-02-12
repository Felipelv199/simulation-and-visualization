import numpy as np


class Configurations:

    def __init__(self, n, m) -> None:
        self.frameConfigs = {}
        self.grid = np.zeros(n*m).reshape(n, m)

    def checkBlinker(self, grid: np.ndarray, i: int, j: int) -> None:
        blinker = np.array([[255],
                            [255],
                            [255]])
        self.checkConfig(grid, blinker, 'blinker', i, j)

    def addToad(self, grid: np.ndarray, i: int, j: int) -> None:
        toad = np.array([[0,   0, 255,   0],
                         [255, 0,   0, 255],
                         [255, 0,   0, 255],
                         [0, 255,   0,   0], ])
        n, m = toad.shape
        grid[i:i+n, j:j+m] = toad

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
            self.checkConfig(grid, x, 'beacon', i, j)

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
            self.checkConfig(grid, x, 'glider', i, j)

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
            self.checkConfig(grid, x, 'lightWeightSpaceship', i, j)

    def checkConfig(self, grid, subGrid, subGridName, i, j):
        n, m = subGrid.shape

        if np.all(self.grid[i:i+n, j:j+m] == 1):
            return

        if np.array_equal(subGrid, grid[i:i+n, j:j+m]):
            try:
                self.frameConfigs[subGridName] += 1
            except:
                self.frameConfigs[subGridName] = 1

            self.grid[i:i+n, j:j+m] = 1
