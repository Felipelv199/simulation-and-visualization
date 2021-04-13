from typing import List
from fluid import Fluid
import numpy as np
import math
import imageio
import sys

velocities = []
densities = []
color = []


def input_file_reader(path: str, f: Fluid) -> None:
    try:
        file = open(path)
    except:
        print("ERROR: File not found")
        return

    # Read simulation color
    s = file.readline().split(" ")
    for c in s:
        color.append(int(c))
    n = int(file.readline())

    # Read sources of density
    for _ in range(n):
        s = file.readline().split(" ")
        x, y = [int(x) for x in s]
        if densities.__contains__((x, y)):
            print(
                "ERROR: There is already a source of density in that position ->", (x, y))
        elif x > f.size or x < 0 or y > f.size or y < 0:
            print("ERROR: Position out of bounds ->", (x, y))
        else:
            densities.append((x, y))
    print("Current sources of density ->", densities)

    # Read sources of velocity
    n = int(file.readline())
    for _ in range(n):
        s = file.readline().split(" ")
        x = int(s[0])
        y = int(s[1])
        if velocities.__contains__((x, y)):
            print(
                "ERROR: There is already a source of velocity in that position ->", (x, y))
        elif x > f.size or x < 0 or y > f.size or y < 0:
            print("ERROR: Position out of bounds ->", (x, y, p))
        else:
            name = s[2]
            if name == "spinner":
                velocities.append((x, y, name, int(s[3]), int(s[4])))
            elif name == "waver":
                velocities.append(
                    (x, y, name, int(s[3]), int(s[4]), int(s[5])))
    print("Current sources of velocity ->", velocities)


def get_color_image(c: List[int], intensity: float, m: int, n: int, f: Fluid) -> List[List[int]]:
    pixels = []
    for i in range(m):
        row = []
        for j in range(n):
            r = (c[0] / 255.0) * (f.density[i, j] / intensity)
            g = (c[1] / 255.0) * (f.density[i, j] / intensity)
            b = (c[2] / 255.0) * (f.density[i, j] / intensity)
            row.append([r, g, b])
        pixels.append(row)
    return pixels


def spinner_animation(period: int, direction: int, f: int) -> List[int]:
    angle = math.radians(f*period*direction)
    return [math.sin(angle), math.cos(angle)]


def waver_animation(period: float, amplitud: float, direction: int, f: int) -> List[int]:
    angle = math.sin(f*period*math.pi/amplitud)
    return [math.sin(angle), direction*math.cos(angle)]


if __name__ == "__main__":
    try:
        import matplotlib.pyplot as plt
        from matplotlib import animation

        inst = Fluid()

        # Read input file
        try:
            input_file_reader(sys.argv[1], inst)
        except:
            print('ERROR: Any command line arguments detected')

        def update_im(i):
            # We add new density creators in here
            if len(densities) == 0:
                if i == 1:
                    print(
                        "WARNING: Any source of density found, running default density source")
            else:
                for density in densities:
                    x, y = density
                    inst.density[y, x] += 100

            # We add velocity vector values in here
            if len(velocities) == 0:
                if i == 1:
                    print(
                        "WARNING: Any source of velocity found, running default velocity source")
            else:
                for velocity in velocities:
                    x = velocity[0]
                    y = velocity[1]
                    name = velocity[2]
                    if name == "spinner":
                        inst.velo[y, x] = spinner_animation(
                            velocity[3], velocity[4], i)
                    elif name == "waver":
                        inst.velo[y, x] = waver_animation(
                            velocity[3], velocity[4],  velocity[5], i)
            inst.step()

            # Object assignation to the grid
            for i in range(25, 30):
                for j in range(25, 30):
                    inst.density[i, j] = 0
                    inst.velo[i, j, 0] = 0
                    inst.velo[i, j, 1] = 0

            # Calculus and assignation of the color to the image
            m, n = inst.density.shape
            maxs = []
            for i in range(m):
                maxs.append(max(inst.density[i]))
            image = get_color_image(color, max(maxs), m, n, inst)

            # Update the outputs
            im.set_array(image)
            q.set_UVC(inst.velo[:, :, 1], inst.velo[:, :, 0])
            im.autoscale()

        fig = plt.figure()

        # plot density
        im = plt.imshow(inst.density, vmax=100,
                        interpolation='bilinear')

        # plot vector field
        q = plt.quiver(inst.velo[:, :, 1],
                       inst.velo[:, :, 0], scale=10, angles='xy')
        anim = animation.FuncAnimation(fig, update_im, interval=0)
        # anim.save("movie.mp4", fps=30, extra_args=['-vcodec', 'libx264'])
        plt.show()

    except ImportError:

        frames = 30

        flu = Fluid()

        video = np.full((frames, flu.size, flu.size), 0, dtype=float)

        for step in range(0, frames):
            flu.density[4:7, 4:7] += 100  # add density into a 3*3 square
            flu.velo[5, 5] += [1, 2]

            flu.step()
            video[step] = flu.density

        imageio.mimsave('./video.gif', video.astype('uint8'))
