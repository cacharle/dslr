import sys

from analysis import Analysis


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise "Usage: {} dataset_path".format(sys.argv[0])
    a = Analysis(sys.argv[1])
    a.describe()
    print(a.df_scores.describe())
