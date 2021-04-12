from math import e
from typing import List
from matplotlib.pyplot import sca
from fluid import Fluid
import imageio
import os
import sys

velocities = []
densities = []
""" 

def screen_clear():
    _ = os.system('cls')


def command_line_read_axis(f: Fluid, a: List) -> List[int]:
    print("Give me the position on the grid")
    x = 0
    while True:
        try:
            x = (int)(input("> axis-x: "))
            break
        except:
            print("ERROR: You must introduce a number")
    y = 0
    while True:
        try:
            y = (int)(input("> axis-y: "))
            break
        except:
            print("ERROR: You must introduce a number")
    screen_clear()
    inside = 0
    if a.__contains__((x, y)):
        print("ERROR: There is already a source of velocity in that position")
    elif x > f.size or x < 0 or y > f.size or y < 0:
        print("ERROR: Position out of bounds")
    else:
        inside = 1
    return [x, y, inside]


def command_line_reader(f: Fluid):
    print("Do you want to set sources of density?")
    while True:
        response = input("> y or n: ").lower()
        if response == 'y' or response == 'n':
            break

    screen_clear()
    if response == 'y':
        while True:
            x, y, inside = command_line_read_axis(f, densities)
            if inside:
                densities.append((x, y))
                screen_clear()
            print("Do you want to set another source of density?")
            print("Current sources of density -> ", densities)
            while True:
                response = input("> y or n: ").lower()
                if response == 'y' or response == 'n':
                    break
            screen_clear()
            if response == "n":
                break

    print("Do you want to set sources of velocity?")
    while True:
        response = input("> y or n: ").lower()
        if response == 'y' or response == 'n':
            break

    screen_clear()
    if response == 'y':
        while True:
            x, y, inside = command_line_read_axis(f, velocities)
            if inside:
                velocities.append((x, y))
                screen_clear()
            print("Do you want to set another source of velocity?")
            print("Current sources of velocity -> ", velocities)
            while True:
                response = input("> y or n: ").lower()
                if response == 'y' or response == 'n':
                    break

            screen_clear()
            if response == "n":
                break
 """


def input_file_reader(path: str, f: Fluid) -> None:
    try:
        file = open(path)
    except:
        print("ERROR: File not found")
        return
    n = 0
    # Read sources of density
    while True:
        s = file.readline()
        if s == '':
            n = 0
            break
        else:
            try:
                n = (int)(s)
                break
            except:
                continue
    for _ in range(n):
        s = file.readline()
        if s == '':
            break
        x, y = [(int)(x.replace("\n", "")) for x in s.split(" ")]
        if densities.__contains__((x, y)):
            print(
                "ERROR: There is already a source of density in that position ->", (x, y))
        elif x > f.size or x < 0 or y > f.size or y < 0:
            print("ERROR: Position out of bounds ->", (x, y))
        else:
            densities.append((x, y))
    print("Current sources of density ->", densities)

    # Read sources of velocity
    while True:
        s = file.readline()
        if s == '':
            n = 0
            break
        else:
            try:
                n = (int)(s)
                break
            except:
                continue

    for _ in range(n):
        s = file.readline()
        if s == '':
            break
        x, y = [(int)(x.replace("\n", "")) for x in s.split(" ")]
        if velocities.__contains__((x, y)):
            print(
                "ERROR: There is already a source of velocity in that position ->", (x, y))
        elif x > f.size or x < 0 or y > f.size or y < 0:
            print("ERROR: Position out of bounds ->", (x, y))
        else:
            velocities.append((x, y))
    print("Current sources of velocity ->", velocities)


if __name__ == "__main__":
    try:
        import matplotlib.pyplot as plt
        from matplotlib import animation

        inst = Fluid()
        # Read input from command line
        # command_line_reader(inst)

        # Read input from input file
        input_file_reader(sys.argv[1], inst)

        def update_im(i):
            # We add new density creators in here
            if len(densities) == 0:
                if i == 1:
                    print(
                        "WARNING: Any source of density found, running default density source")
                # add density into a 3*3 square
                inst.density[14:17, 14:17] += 100
            else:
                for density in densities:
                    x, y = density
                    inst.density[y, x] += 100
            # We add velocity vector values in here
            if len(velocities) == 0:
                if i == 1:
                    print(
                        "WARNING: Any source of velocity found, running default velocity source")
                inst.velo[20, 20] = [-2, -2]
            else:
                for velocity in velocities:
                    x, y = velocity
                    inst.velo[y, x] = [-2, -2]
            inst.step()
            im.set_array(inst.density)
            q.set_UVC(inst.velo[:, :, 1], inst.velo[:, :, 0])
            # print(f"Density sum: {inst.density.sum()}")
            im.autoscale()

        fig = plt.figure()

        # plot density
        im = plt.imshow(inst.density, vmax=100, interpolation='bilinear')

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
