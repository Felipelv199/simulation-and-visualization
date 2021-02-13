from typing import Literal
import numpy as np


class Configurations:
    """
    A class used to hold and validate Game of Life configurations

    Attributes
    ----------
    frameConfigs: dict
        The configurations and number of appearance in the grid per frame
    grid: ndarray
        A grid that represents the positions already checked

    Methods
    -------
    checkBlock() -> None
    checkBeehive() -> None
    checkLoaf() -> None
    checkBoat() -> None
    checkTub() -> None
    checkBlinker() -> None
    checkToad() -> None
    checkBeacon() -> None
    checkGlider() -> None
    checkLightWeightSpaceship() -> None
    checkConfig() -> bool
        Returns a bool depending if the configuration was found or not
    checkOthers() -> None
    growing() -> list
        Returns a list containing the points of the detected region
    """

    def __init__(self, n: int, m: int) -> None:
        self.frameConfigs = {}
        self.grid = np.zeros(n*m).reshape(n, m)

    def checkBlock(self, grid: np.ndarray, i: int, j: int) -> None:
        """
            Holds and validates if the block configuration appears in the grid

            Parameters
            ----------
            grid: np.ndarray
                GoL grid
            i: int
                Row position of the current pixel
            j: int
                Col position of the current pixel
        """
        block = np.array([[255, 255, ],
                          [255, 255, ], ])
        self.checkConfig(grid, block, 'Block', i, j)

    def checkBeehive(self, grid: np.ndarray, i: int, j: int) -> None:
        """
            Holds and validates if the beehive configuration appears in the grid

            Parameters
            ----------
            grid: np.ndarray
                GoL grid
            i: int
                Row position of the current pixel
            j: int
                Col position of the current pixel
        """
        beehive = np.array([[0, 255, 255,   0, ],
                            [255, 0,   0, 255, ],
                            [0, 255, 255,   0, ]])
        self.checkConfig(grid, beehive, 'Beehive', i, j)

    def checkLoaf(self, grid: np.ndarray, i: int, j: int) -> None:
        """
            Holds and validates if the loaf configuration appears in the grid

            Parameters
            ----------
            grid: np.ndarray
                GoL grid
            i: int
                Row position of the current pixel
            j: int
                Col position of the current pixel
        """
        loaf = np.array([[0, 255, 255, 0, ],
                         [255, 0,   0, 255, ],
                         [0, 255,   0, 255, ],
                         [0,   0, 255, 0, ]])
        self.checkConfig(grid, loaf, 'Loaf', i, j)

    def checkBoat(self, grid: np.ndarray, i: int, j: int) -> None:
        """
            Holds and validates if the boat configuration appears in the grid

            Parameters
            ----------
            grid: np.ndarray
                GoL grid
            i: int
                Row position of the current pixel
            j: int
                Col position of the current pixel
        """
        boat = np.array([[255, 255,   0, ],
                         [255,   0, 255, ],
                         [0,   255,   0, ]])
        self.checkConfig(grid, boat, 'Boat', i, j)

    def checkTub(self, grid: np.ndarray, i: int, j: int) -> None:
        """
        Holds and validates if the tub configuration appears in the grid

            Parameters
            ----------
            grid: np.ndarray
                GoL grid
            i: int
                Row position of the current pixel
            j: int
                Col position of the current pixel
        """
        tub = np.array([[0, 255,   0, ],
                        [255, 0, 255, ],
                        [0, 255,   0, ]])
        self.checkConfig(grid, tub, 'Tub', i, j)

    def checkBlinker(self, grid: np.ndarray, i: int, j: int) -> None:
        """
            Holds the blinker configurations and validates if any are in the grid

            Parameters
            ----------
            grid: np.ndarray
                GoL grid
            i: int
                Row position of the current pixel
            j: int
                Col position of the current pixel
        """
        blinker = [np.array([[255],
                             [255],
                             [255]]),
                   np.array([[255, 255, 255], ]), ]
        for x in blinker:
            if self.checkConfig(grid, x, 'Blinker', i, j):
                return

    def checkToad(self, grid: np.ndarray, i: int, j: int) -> None:
        """
            Holds the toad configurations and validates if any are in the grid

            Parameters
            ----------
            grid: np.ndarray
                GoL grid
            i: int
                Row position of the current pixel
            j: int
                Col position of the current pixel
        """
        toad = [np.array([[0,   0, 255,   0],
                          [255, 0,   0, 255],
                          [255, 0,   0, 255],
                          [0, 255,   0,   0], ]),
                np.array([[0,   255, 255, 255],
                          [255, 255, 255,   0], ]), ]
        for x in toad:
            if self.checkConfig(grid, x, 'Toad', i, j):
                return

    def checkBeacon(self, grid: np.ndarray, i: int, j: int) -> None:
        """
            Holds the beacon configurations and validates if any are in the grid

            Parameters
            ----------
            grid: np.ndarray
                GoL grid
            i: int
                Row position of the current pixel
            j: int
                Col position of the current pixel
        """
        beacon = [np.array([[255, 255, 0,     0],
                            [255, 255, 0,     0],
                            [0,     0, 255, 255],
                            [0,     0, 255, 255], ]),
                  np.array([[255, 255,   0,   0],
                            [255,   0,   0,   0],
                            [0,     0,   0, 255],
                            [0,     0, 255, 255], ]), ]
        for x in beacon:
            if self.checkConfig(grid, x, 'Beacon', i, j):
                return

    def checkGlider(self, grid: np.ndarray, i: int, j: int) -> None:
        """
            Holds the glider configurations and validates if any are in the grid

            Parameters
            ----------
            grid: np.ndarray
                GoL grid
            i: int
                Row position of the current pixel
            j: int
                Col position of the current pixel
        """
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
            if self.checkConfig(grid, x, 'Glider', i, j):
                return

    def checkLightWeightSpaceship(self, grid: np.ndarray, i: int, j: int) -> None:
        """
            Holds the lightWeightSpaceship configurations and validates if any are in the grid

            Parameters
            ----------
            grid: np.ndarray
                GoL grid
            i: int
                Row position of the current pixel
            j: int
                Col position of the current pixel
        """
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
            if self.checkConfig(grid, x, 'LightWeightSpaceship', i, j):
                return

    def checkConfig(self, grid: np.ndarray, subGrid: np.ndarray, subGridName: Literal, i: int, j: int) -> bool:
        """
            Checks if the provided configuration appears in the grid, and updates the frameConfigs counter of the corresponding configuration

            Parameters
            ----------
            grid: np.ndarray
                GoL grid
            subGrid: np.ndarray
                Grid that represents a configuration
            subGridName: string
                Configuration grid name
            i: int
                Row position of the current pixel
            j: int
                Col position of the current pixel

            Returns
            -------
            bool
                A value depending if the configuration was found or not
        """
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
        """
            Check and detect the configuration that not corresponds to the previous ones and updates the frameConfigs counter of Others

            Parameters
            ----------
            grid: np.ndarray
                GoL grid
            i: int
                Row position of the current pixel
            j: int
                Col position of the current pixel
        """
        if grid[i, j] == 0:
            return

        other = self.growing(grid, i, j, 255)

        if len(other) > 0:
            try:
                self.frameConfigs['Others'] += 1
            except:
                self.frameConfigs['Others'] = 1

    def growing(self, grid: np.ndarray, i: int, j: int, colorVal: int) -> list:
        """
            Detects the points that are part of a configuration different from the previous ones

            Parameters
            ----------
            grid: np.ndarray
                GoL grid
            i: int
                Row position of the current pixel
            j: int
                Col position of the current pixel
            colorVal:
                Color that will discriminate the neighbors

            Returns
            -------
            list
                A list containing the points of the detected region
        """
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
