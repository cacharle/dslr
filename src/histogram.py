#!/bin/python3

import sys

import matplotlib.pyplot as plt

from dataset import Dataset


def house_hist(ax, d, house_name):
    h = d.df[d.df["house"] == house_name]
    scores = h.loc[:, "arithmancy":"flying"]
    x = (scores - scores.min()) / (scores.max() - scores.min())
    ax.hist(x.values.flatten(), bins=40, rwidth=0.8)
    ax.set_title(house_name)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise "Usage: {} dataset_path".format(sys.argv[0])
    d = Dataset(sys.argv[1])

    fig, axs = plt.subplots(2, 2, sharey=True, tight_layout=True)
    house_hist(axs[0][0], d, "Gryffindor")
    house_hist(axs[0][1], d, "Slytherin")
    house_hist(axs[1][0], d, "Ravenclaw")
    house_hist(axs[1][1], d, "Hufflepuff")
    plt.show()

