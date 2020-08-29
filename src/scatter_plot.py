#!/bin/python3

import sys

import matplotlib.pyplot as plt

from dataset import Dataset


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise "Usage: {} dataset_path".format(sys.argv[0])
    d = Dataset(sys.argv[1])
    plt.scatter(d.df['astronomy'], d.df['defense_dark_arts'], s=5)
    plt.xlabel('astronomy')
    plt.ylabel('defense_dark_arts')
    plt.show()
