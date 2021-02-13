# Conway's Game of Life Simulation

This Conway's Game of Life implementation uses python and matplotlib animations to generate a frame per frame simulation. Using his four rules of life, this graphic simulation can use different types of patterns.

## Instructions of Use

To run this program, it is necessary to give an input file, otherwise, it will generate a random grid with random alive cells. The default values are as follows:
- Grid Dimensions: 50 x 50
- Animation Frames Number: 200

### Input File Format

The first line contains two space-separated integers that denote the dimensions of the grid.  
The second line contains an integer that denotes the frame number of the animation.  
The next lines until the end of the file contain the position of the grid live cells. If these positions are out of bounds it will not use that position, and it will move to the next.

If your gonna use an input file you must provide your file relative path:

    python conway.py [FilePath]
    
In case that is an error with the file relative path, it will run the default configuration.

### Output File Format

It will return the numbers of configurations recognized by the program and the ones that are not recognized are classified as other. The numbers will correspond to the times that a configuration appears in the frame and also the final count per configuration.
