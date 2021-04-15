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
  - Name = square || circle || rectangle
- Width
  - W > 0
- Height
  - H > 0
- Radius
  - R > 0
> Square
```
x y Name W
```
> Rectangle
```
x y Name W H
```
> Circle
```
x y Name R
```
So at the end, the file should look kind of this.
```
r g b
N
x y
N
x y Name P D
x y Name H P A D
N
x y Name W
x y Name W H
x y Name R
```
## Density Sources
They are distinguish from the background with a different color, they appear in the position that you place them on the grid. Some cells of the grid may have a more strong color than the others, this is becouse of the current density that cell has. The greater the density the stronger the color will be and when the difference between the bigger density and the smaller is incresasing the smaller will be decreasing.

![image](https://user-images.githubusercontent.com/47803931/114804871-43ce9c80-9d5f-11eb-92ae-35b5b417cf3e.png)
![image](https://user-images.githubusercontent.com/47803931/114805077-9445fa00-9d5f-11eb-9d92-d8ca5a147030.png)
## Velocity Sources
They interact with the density sources, affecting the densities in each grid. They can move the density changing its position and decreasing its value on the original grid, passing part of it to another grid.
## Velocity Sources Animation
You can achieve these effects by modifying the direction of the velocity forces applied to the densities.

On this simulation, you can add to the grid two animations:
- Waver
- Spinner

The following lines show how each one behaves.

>Spinner

![image](https://github.com/Felipelv199/simulation-and-visualization/blob/feature/fluid-simulation/Fluid_Sim/media/spinner-ex-1.gif)
![image](https://github.com/Felipelv199/simulation-and-visualization/blob/feature/fluid-simulation/Fluid_Sim/media/spinner-ex-2.gif)
>Waver

![image](https://github.com/Felipelv199/simulation-and-visualization/blob/feature/fluid-simulation/Fluid_Sim/media/waver-ex-1.gif)
![image](https://github.com/Felipelv199/simulation-and-visualization/blob/feature/fluid-simulation/Fluid_Sim/media/waver-ex-2.gif)
![image](https://github.com/Felipelv199/simulation-and-visualization/blob/feature/fluid-simulation/Fluid_Sim/media/waver-ex-3.gif)
![image](https://github.com/Felipelv199/simulation-and-visualization/blob/feature/fluid-simulation/Fluid_Sim/media/waver-ex-4.gif)
## Simulation Color
## Objects
