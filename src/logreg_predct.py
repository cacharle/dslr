import sys

from model import Model


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise 'Usage: {} dataset_path weights_path'.path(*sys.argv[1:])
    m = Model()
    m.predict()

