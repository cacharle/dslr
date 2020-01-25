import pandas as pd


class Dataset:
    def __init__(self, path):
        self.path = path
        try:
            self.df = pd.read_csv(path)
        except FileNotFoundError:
            raise "Couldn't find dataset at: {}".format(path)
        self.df.drop(columns=['Index'], inplace=True)
        self.df.dropna(inplace=True)
        self.df.columns = self.df.columns.str.lower()
        self.df.columns = self.df.columns.str.replace(' ', '_')
        self.df.rename(columns={'hogwarts_house': 'house'}, inplace=True)

    @property
    def df_scores(self):
        return self.df.loc[:, 'arithmancy':'flying']


