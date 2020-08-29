#!/bin/python3

import sys

import numpy as np

from dataset import Dataset


def sigmoid(x):
    return 1.0 / (1.0 * np.exp(-x))

def hypothesis(x, theta):
    return sigmoid(x.dot(theta))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise 'Usage: {} dataset_path weights_path'.format(sys.argv[0])

    labels = []
    thetas = []
    with open(sys.argv[2]) as f:
        for line in f:
            label_end = line.find(":")
            labels.append(line[:label_end])
            thetas.append(np.array([float(s) for s in line[label_end + 2:].split(",")]))
    # print(labels)
    # print(thetas)

    d = Dataset(sys.argv[1])

    X = d.df_scores
    X = (X - X.min()) / (X.max() - X.min())
    X = np.hstack([X, np.ones((X.shape[0], 1))])

    with open("houses.csv", "w") as houses_file:
        houses_file.write("Index,Hogwarts House\n")
        for i, x in enumerate(X):
            hs = []
            for l, t in zip(labels, thetas):
                hs.append((l, hypothesis(x, t)))

            predicted, _ = max(hs, key=lambda x: x[1])
            houses_file.write("{},{}\n".format(i, predicted))
