#!/bin/python3

import sys

import pandas as pd
import matplotlib.pyplot as plt

from dataset import Dataset


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise "Usage: {} dataset_path".format(sys.argv[0])
    d = Dataset(sys.argv[1])
    pd.plotting.scatter_matrix(d.df_scores, s=2, alpha=0.8)
    plt.show()

