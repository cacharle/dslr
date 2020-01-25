import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from dataset import Dataset
import dslr_stat


class Analysis(Dataset):
    def __init__(self, path):
        super().__init__(path)

    def describe(self):
        desc_df = pd.DataFrame(
            dtype=np.float64,
            columns=[c for c, t in zip(self.df.columns, self.df.dtypes) if t == np.float64],
            index=['Count', 'Mean', 'Std', 'Min', '25%', '50%', '75%', 'Max']
        )
        for col in desc_df.columns:
            desc_df.loc['Count', col] = len(self.df[col])
            desc_df.loc['Mean', col] = dslr_stat.mean(self.df[col])
            desc_df.loc['Std', col] = dslr_stat.std(self.df[col])
            desc_df.loc['Min', col] = dslr_stat.min(self.df[col])
            desc_df.loc['25%', col] = dslr_stat.q25(self.df[col])
            desc_df.loc['50%', col] = dslr_stat.median(self.df[col])
            desc_df.loc['75%', col] = dslr_stat.q75(self.df[col])
            desc_df.loc['Max', col] = dslr_stat.max(self.df[col])
        print(desc_df)

    def hist(self):
        pass

    def scatter(self):
        plt.scatter(self.df['astronomy'], self.df['defense_against_the_dark_arts'])
        plt.show()

    def pair_plot(self):
        scores = self.df_scores
        fig, axis = plt.subplots(nrows=scores.shape[1],
                                 ncols=scores.shape[1])
        for i, col in enumerate(scores.columns):
            for j, pair_col in enumerate(scores.columns):
                ax = axis[i, j]
                if pair_col == col:
                    ax.hist(scores)
                    continue
                ax.scatter(scores[col], scores[pair_col])
        plt.tight_layout()
        plt.show()
