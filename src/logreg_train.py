#!/bin/python3

import sys

import pandas as pd
import numpy as np

from dataset import Dataset


def sigmoid(x):
    return 1.0 / (1.0 * np.exp(-x))

def hypothesis(x, theta):
    return sigmoid(x.dot(theta))

def gradient(ys, xs, theta):
    g = np.zeros(len(xs[0]))
    for j in range(len(theta)):
        g[j] = sum([(hypothesis(x, theta) - y) * x[j] for y, x in zip(ys, xs)]) / len(xs)
    return g

def gradient_descent(ys, xs, alpha, epoch):
    theta = np.random.randn(len(xs[0]))
    for i in range(epoch):
        print("Gradient descent: {:02}%\r".format(int((i / epoch) * 100.0)), end="")
        theta = theta - alpha * gradient(ys, xs, theta)
    return theta

def train(ys, xs):
    thetas = []
    # print(np.unique(ys))
    for trained in np.unique(ys):
        print(f"Trainning against {trained}")
        ys_ally = ys.copy()
        ys_ally[ys == trained] = 0 # opposite?
        ys_ally[ys != trained] = 1
        thetas.append((trained, gradient_descent(ys_ally, xs, 1, 100)))
    return thetas

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise 'Usage: {} dataset_path'.format(sys.argv[0])
    d = Dataset(sys.argv[1])

    X = d.df_scores.values
    X = np.hstack([X, np.ones((X.shape[0], 1))])
    X = (X - X.min()) / (X.max() - X.min())
    Y = d.df["house"].values

    thetas = train(Y, X)

    with open("weights", "w") as f:
        for label, t in thetas:
            f.write("{}: {}\n".format(label, ','.join([str(x) for x in t])))
