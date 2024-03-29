from typing import List
from fluid import Fluid
from matplotlib import animation
import matplotlib.pyplot as plt
import math
import sys

velocities_positions = []
velocities_properties = []
densities = []
color = []
objects_positions = []
objects_properties = []


def input_file_reader(path: str, f: Fluid) -> None:
    try:
        file = open(path)
    except:
        print("ERROR: File not found")
        return

    file_lines = file.readlines().copy()

    # Read simulation color
    try:
        s = file_lines.pop(0).split(" ")
        for c in s:
            color.append(int(c))
        n = int(file_lines.pop(0))
    except:
        print("ERROR: No color provided")

    # Read sources of density
    for _ in range(n):
        try:
            s = file_lines.pop(0).split(" ")
            x, y = [int(x) for x in s]
            if densities.__contains__((x, y)):
                print(
                    "ERROR: There is already a source of density in that position ->", (x, y))
            elif x > f.size or x < 0 or y > f.size or y < 0:
                print("ERROR: Position out of bounds ->", (x, y))
            else:
                densities.append((x, y))
        except:
            print("ERROR: The number of densities not matches with the ones provided")

    if len(file_lines) == 0:
        return

    # Read sources of velocity
    n = int(file_lines.pop(0))
    for _ in range(n):
        s = file_lines.pop(0).split(" ")
        x = int(s[0])
        y = int(s[1])
        if velocities_positions.__contains__((x, y)):
            print(
                "ERROR: There is already a source of velocity in that position ->", (x, y))
        elif x > f.size or x < 0 or y > f.size or y < 0:
            print("ERROR: Position out of bounds ->", (x, y))
        else:
            name = s[2]
            if name == "spinner":
                velocities_positions.append((x, y))
                velocities_properties.append((name, int(s[3]), int(s[4])))
            elif name == "waver":
                velocities_positions.append((x, y))
                velocities_properties.append(
                    (name, int(s[3]), int(s[4]), int(s[5]), int(s[6])))

    if len(file_lines) == 0:
        return
    # Read objects
    n = int(file_lines.pop(0))
    for _ in range(n):
        s = file_lines.pop(0).split(" ")
        x = int(s[0])
        y = int(s[1])
        if objects_positions.__contains__((x, y)) or velocities_positions.__contains__((x, y)) or densities.__contains__((x, y)):
            print(
                "ERROR: Object position already in use ->", (x, y))
        elif x > f.size or x < 0 or y > f.size or y < 0:
            print("ERROR: Position object out of bounds ->", (x, y))
        else:
            name = s[2]
            if name == 'square':
                objects_positions.append((x, y))
                objects_properties.append((name, int(s[3])))
            elif name == 'rectangle':
                objects_positions.append((x, y))
                objects_properties.append((name, int(s[3]), int(s[4])))
            elif name == 'circle':
                objects_positions.append((x, y))
                objects_properties.append((name, int(s[3])))
    print("Current sources of density positions ->", densities)
    print("Current sources of velocity positions ->", velocities_positions)
    print("Current objects positions ->", objects_positions)


def get_color_image(c: List[int], intensity: float, m: int, n: int, f: Fluid) -> List[List[int]]:
    pixels = []
    for i in range(m):
        row = []
        for j in range(n):
            r = (c[0] / 255.0) * (f.density[i, j] / intensity)
            g = (c[1] / 255.0) * (f.density[i, j] / intensity)
            b = (c[2] / 255.0) * (f.density[i, j] / intensity)
            r = clamp(float(r), 1, 0)
            g = clamp(float(g), 1, 0)
            b = clamp(float(b), 1, 0)
            row.append([r, g, b])
        pixels.append(row)
    return pixels


def clamp(value: float, maximum: int, minimun: int):
    if value > maximum:
        return maximum
    elif value < minimun:
        return minimun
    return value


def spinner_animation(period: int, direction: int, f: int) -> List[int]:
    angle = math.radians(f*period*direction)
    return [math.sin(angle), math.cos(angle)]


def waver_animation(horientation: int, period: float, amplitud: float, direction: int, f: int) -> List[int]:
    angle = math.sin(f*period*math.pi/amplitud)
    if horientation == 1:
        return [math.sin(angle), direction*math.cos(angle)]
    else:
        return [direction*math.cos(angle), math.sin(angle)]


def add_rectangle(w: int, h: int, x0: int, y0: int, fluid: Fluid):
    difH = int(h/2)
    difW = int(w/2)
    for i in range(y0-difH, y0+difH):
        for j in range(x0-difW, x0+difW):
            fluid.density[i, j] = 0
            fluid.velo[i, j, 0] = 0
            fluid.velo[i, j, 1] = 0


def add_square(w: int, x0: int, y0: int, fluid: Fluid):
    dif = int(w/2)
    for i in range(y0-dif, y0+dif):
        for j in range(x0-dif, x0+dif):
            fluid.density[i, j] = 0
            fluid.velo[i, j, 0] = 0
            fluid.velo[i, j, 1] = 0


def add_circle(r: int, x0: int, y0: int, fluid: Fluid):
    dif = r+1
    for i in range(y0-dif, y0+dif):
        for j in range(x0-dif, x0+dif):
            x = j-x0
            y = i-y0
            d = math.sqrt(x**2+y**2)
            if abs(d-r) < .6:
                fluid.density[i, j] = 0
                fluid.velo[i, j, 0] = 0
                fluid.velo[i, j, 1] = 0


if __name__ == "__main__":

    inst = Fluid()

    # Read input file
    file_name = sys.argv[1]
    try:
        input_file_reader(sys.argv[1], inst)
    except:
        input_file_reader("example_input.txt", inst)
        print('ERROR: Something went wrong when reading the file')

    def update_im(frame):
        # We add new density creators in here
        if len(densities) == 0:
            if frame == 1:
                print(
                    "WARNING: Any source of density found, running default density source")
        else:
            for density in densities:
                x, y = density
                inst.density[y, x] += 100

        # We add velocity vector values in here
        if len(velocities_positions) == 0:
            if frame == 1:
                print(
                    "WARNING: Any source of velocity found, running default velocity source")
        else:
            for i in range(len(velocities_positions)):
                x, y = velocities_positions[i]
                velocity = velocities_properties[i]
                name = velocity[0]
                if name == "spinner":
                    inst.velo[y, x] = spinner_animation(
                        velocity[1], velocity[2], frame)
                elif name == "waver":
                    inst.velo[y, x] = waver_animation(
                        velocity[1], velocity[2],  velocity[3],  velocity[4], frame)
        inst.step()

        # Object assignation to the grid
        for i in range(len(objects_positions)):
            x, y = objects_positions[i]
            obj = objects_properties[i]
            name = obj[0]
            if name == 'square':
                add_square(obj[1], x, y, inst)
            elif name == 'rectangle':
                add_rectangle(obj[1], obj[2], x, y, inst)
            elif name == 'circle':
                add_circle(obj[1], x, y, inst)

        # Calculate and assign the image color
        m, n = inst.density.shape
        density_values = []
        for i in range(m):
            for j in range(n):
                if inst.density[i, j] != 0:
                    density_values.append(inst.density[i, j])
        image = get_color_image(color, max(density_values), m, n, inst)

        # Update the outputs
        im.set_array(image)
        q.set_UVC(inst.velo[:, :, 1], inst.velo[:, :, 0])
        im.autoscale()

    fig = plt.figure()

    # Plot density
    im = plt.imshow(inst.density, vmax=100,
                    interpolation='bilinear')

    # Plot vector field
    q = plt.quiver(inst.velo[:, :, 1],
                   inst.velo[:, :, 0], scale=10, angles='xy')
    anim = animation.FuncAnimation(
        fig, update_im, interval=1, save_count=500)

    # Write and creates mp4 video file
    """ writervideo = animation.FFMpegWriter(fps=30)
    anim.save("movie.mp4", writer=writervideo) """

    # Write and creates gif image file
    """ pillow = animation.PillowWriter(fps=30)
    anim.save("movie.gif", pillow) """

    plt.show()
