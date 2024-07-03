"""
==============
stairs(values)
==============

See `~matplotlib.axes.Axes.stairs` when plotting :math:`y` between
:math:`(x_i, x_{i+1})`. For plotting :math:`y` at :math:`x`, see
`~matplotlib.axes.Axes.step`.

.. redirect-from:: /plot_types/basic/step
"""
import matplotlib.pyplot as plt
import numpy as np





import argparse
import os

def save_plot(save_folder, save_filename):
    plt.style.use('_mpl-gallery')

    # make data
    y = [4.8, 5.5, 3.5, 4.6, 6.5, 6.6, 2.6, 3.0]

    # plot
    fig, ax = plt.subplots()

    ax.stairs(y, linewidth=2.5)

    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
        ylim=(0, 8), yticks=np.arange(1, 8))
    save_path = os.path.join(save_folder, f"{save_filename}.png")
    plt.savefig(save_path)
    plt.close(fig)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate and save a matplotlib plot.")
    parser.add_argument("save_folder", help="The folder path where the plot will be saved.")
    parser.add_argument("save_filename", help="The file name for the saved plot, without extension.")
    
    args = parser.parse_args()
    save_plot(args.save_folder, args.save_filename)