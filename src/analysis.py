import numpy as np
import pandas as pd

import dslr_stat


class Analysis:
    def __init__(self, df):
        self.df = df

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
