import imageio
from fluid import Fluid

if __name__ == "__main__":
    try:
        import matplotlib.pyplot as plt
        from matplotlib import animation

        inst = Fluid()

        def update_im(i):
            # We add new density creators in here
            inst.density[14:17, 14:17] += 100  # add density into a 3*3 square
            # We add velocity vector values in here
            inst.velo[20, 20] = [-2, -2]
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
        #anim.save("movie.mp4", fps=30, extra_args=['-vcodec', 'libx264'])
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
