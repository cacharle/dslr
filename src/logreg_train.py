import sys

from model import Model


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise 'Usage: {} dataset_path'.format(sys.argv[0])
    m = Model()
    m.train()
    # write
