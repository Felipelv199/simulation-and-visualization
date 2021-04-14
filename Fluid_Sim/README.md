# Fluid Simulation
This fluid simulation uses the python_realtime_fluidsim project, created by Guilouf.

It simulates the way fluids behave inside a 2D grid. It has two velocity behaviors that act as a force. It impacts the fluid density giving the sense of movement to it. As a user, you need to provide an input file. The description of the format of this input file comes in the following lines. With this file, you can set different densities and velocities with various behaviors inside the grid. You can also give different RGB colors on the file and several objects placed on the simulation grid.
### Dependencies
- Numpy
```
pip install numpy
```
- Matplotlib
```
pip install matplotlib
```
### Input File Format
The first line needs to be a three-spaced integer that represents the RGB colors.
- 0 ≥ r ≤ 255
- 0 ≥ g ≤ 255
- 0 ≥ b ≤ 255
```
r g b
```
The second line represents the number of density sources inside the simulation grid.
- N ≥ 0
```
N
```
The following N lines represent the location of the densities.
- GridSize > 0
- 0 ≥ x ≤ GridSize
- 0 ≥ y ≤ GridSize
```
x y
```
The following line representes the number of velocity sources inside the simulation grid.
- N ≥ 0
```
N
```
The following line represents the number of velocity sources inside the simulation grid.
- 0 ≥ x ≤ GridSize
- 0 ≥ y ≤ GridSize
- Animation Name
  - Name = spinner || waver
- Period
  - P > 0
- Horientation
  - H = 1 || -1 
- Direction
  - D = 1 || -1
- Amplitud
  - a > 0
> Spinner
```
x y Name P D
```
> Waver
```
x y Name H P A D
```
The following line represents the number of objects on the simulation grid.
- N ≥ 0
```
N
```
The following N lines represent the location and properties of the objects.
- 0 ≥ x ≤ GridSize
- 0 ≥ y ≤ GridSize
- Object Name
  - N = square || circle || rectangle
- Width
  - W > 0
- Height
  - H > 0
- Radius
  - R > 0
> Square
```
x y N W
```
> Rectangle
```
x y Name W H
```
> Circle
```
x y Name R
```
So at the end, the file should look like this.
```
r g b
N
x y
N
x y Name P D || x y Name H P A D
N
x y Name W || x y Name W H || x y Name R
```
## Sources of Velocity and Density
## Velocity Fources Animation
## Simulation Color
## Objects
