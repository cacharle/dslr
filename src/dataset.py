#!/bin/python3

import sys

import pandas as pd


class Dataset:
    def __init__(self, path):
        self.path = path
        try:
            self.df = pd.read_csv(path)
        except FileNotFoundError:
            raise "Couldn't find dataset at: {}".format(path)
        self.df.drop(columns=['Index'], inplace=True)
        self.df.dropna(axis=1, how="all", inplace=True)
        self.df.dropna(inplace=True)
        self.df.columns = self.df.columns.str.lower()
        self.df.columns = self.df.columns.str.replace(' ', '_')
        self.df.rename(columns={'hogwarts_house': 'house'}, inplace=True)
        self.df.rename(columns={'care_of_magical_creatures': 'magical_creatures'}, inplace=True)
        self.df.rename(columns={'defense_against_the_dark_arts': 'defense_dark_arts'}, inplace=True)

    @property
    def df_scores(self):
        return self.df.loc[:, 'arithmancy':'flying']


if __name__ == "__main__":
    d = Dataset(sys.argv[1])
    print(d.df)
