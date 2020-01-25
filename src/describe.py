import sys

import pandas as pd
from analysis import Analysis


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} dataset_path".format(sys.argv[0]))
        sys.exit(1)
    try:
        df = pd.read_csv(sys.argv[1])
    except FileNotFoundError:
        print("Could not find dataset at: {}".format(sys.argv[1]))
        sys.exit(1)
    df = df.loc[:, 'Arithmancy':'Flying']
    df.dropna(inplace=True)
    a = Analysis(df)
    a.describe()
    print(df.describe())
