# https://stackoverflow.com/questions/9215658/plot-a-circle-with-pyplot

import os
import glob
import matplotlib.pyplot as plt


def clear_dir(dir):
    files = glob.glob(os.path.join(os.path.dirname(os.path.realpath(__file__)), dir, '*.*'))
    images = glob.glob(os.path.join(os.path.dirname(os.path.realpath(__file__)), dir, '*.png'))
    assert len(files) == len(images)

    for image in images:
        # print(image)
        os.remove(image)

def plot_circles(circles, min_fun_vals, xlim=(0, 10), ylim=(0, 10), 
                 savefolder=os.path.join('circles', 'results'), iteration=None,
                 clear_dir_on_new=False, title=None):

    # circle1 = plt.Circle((0, 0), 0.2, color='r')
    # circle2 = plt.Circle((0.5, 0.5), 0.2, color='blue')
    # circle3 = plt.Circle((1, 1), 0.2, color='g', clip_on=False)
    if clear_dir_on_new:
        clear_dir(savefolder)

    circle_plots = []

    for (x, y), r, lat_cluster_id in circles:
        circle_plot = plt.Circle((x, y), r, color='r', fill=False)
        circle_plots.append(circle_plot)

    if min_fun_vals is not None:
        for min_fun_val in min_fun_vals:
            if isinstance(min_fun_val['p'], list):
                for p in min_fun_val['p']:
                    circle_plots.append(
                        plt.Circle(p, 0.2, color='blue', fill=False)
                    )
            else:
                circle_plots.append(
                    plt.Circle(min_fun_val['p'], 0.2, color='blue', fill=False)
                )

    fig, ax = plt.subplots()
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    for circle_plot in circle_plots:
        ax.add_artist(circle_plot)

    ax.set_aspect('equal')

    if title is None:
        if iteration is None:
            title = 'plotcircles.png'
        else:
            title = 'plotcircles iter %d.png' % (iteration,)

    fig.savefig(os.path.join(savefolder, title))
    # fig.savefig('circles/results/%s' % (title,))