class Model:
    def __init__(self, weights_filename='weights'):
        self.weights_filename = weights_filename

    def train(self, xs, ys, alpha=1, epoch=1000):
        for _ in range(epoch):
            theta = theta - alpha * self.gradient(xs, ys)

    def gradient(self, xs, ys):
        return np.array([self.partial(xs, ys, i) for i in range(len(self.theta))])

    def partial(self, xs, ys, theta_j):
        total = 0
        for x_i, y_i in zip(xs, ys):
            temp = self.hypothesis(x_i) - y_i
            if theta_j != 0:
                temp *= x_i[theta_j - 1]
                total += temp
                return total / len(xs)

    def hypothesis(self, x):
        return 1 if  self._sigmoid(x.dot(self.theta)) >= 0.5 else 0

    def logloss(self, x, y):
        if y == 1:
            return -np.ln(self.hypothesis(x))
        elif y == 0:
            return -np.ln(1 - self.hypothesis(x))
        else:
            raise "y != 1 and y != 0"

    def cost(self, xs, ys):
        return sum([self.logloss(x, y) for x, y in zip(xs, ys)]) / len(xs)

    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def _normalize(self, x):
        return (x - x.min()) / (x.max() - x.min())

    def _read_weights(self):
        try:
            with open(self.weights_filename, 'r') as file:
                self.weights = np.array(
                    [float(s) for s in file.read().strip().split(',')])
        except IOError:
            raise 'Couldn\'t read weights file at: {}'.format(self.weights_filename)

    def _write_weights(self):
        try:
            with open(self.weights_filename, 'w') as file:
                file.write(','.join([str(w) for w in self.weights])
        except IOError:
            raise 'Couldn\'t write weights file at: {}'.format(self.weights_filename)
