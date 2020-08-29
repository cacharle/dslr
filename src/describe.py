#!/bin/python3

import sys

import pandas as pd
import numpy as np

from dataset import Dataset
import dslr_stat


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise "Usage: {} dataset_path".format(sys.argv[0])
    d = Dataset(sys.argv[1])
    desc_df = pd.DataFrame(
        dtype=np.float64,
        columns=[c for c, t in zip(d.df.columns, d.df.dtypes) if t == np.float64],
        index=['Count', 'Mean', 'Std', 'Min', '25%', '50%', '75%', 'Max']
    )
    for col in desc_df.columns:
        desc_df.loc['Count', col] = len(d.df[col])
        desc_df.loc['Mean', col] = dslr_stat.mean(d.df[col])
        desc_df.loc['Std', col] = dslr_stat.std(d.df[col])
        desc_df.loc['Min', col] = dslr_stat.min(d.df[col])
        desc_df.loc['25%', col] = dslr_stat.q25(d.df[col])
        desc_df.loc['50%', col] = dslr_stat.median(d.df[col])
        desc_df.loc['75%', col] = dslr_stat.q75(d.df[col])
        desc_df.loc['Max', col] = dslr_stat.max(d.df[col])
    print(desc_df)
