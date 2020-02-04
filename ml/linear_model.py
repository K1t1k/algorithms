import numpy as np


class LinearRegression():
    def __init__(self, learning_rate: float, max_iter: int, random_state=None):
        self.learning_rate = learning_rate
        self.max_iter = max_iter
        self.w = None
        self.X = None
        self.y = None
        self.cost = None
        self.random_state = random_state

    def fit(self, X, y):
        self.X = np.ones((X.shape[0], X.shape[1] + 1))
        self.w = np.random.normal(loc=0., scale=1., size=self.X.shape[1])
        self.X[:, 1:] = X
        self.y = y
        self.cost = []
        for _ in range(self.max_iter):
            predict = self.predict(self.X)
            error = self.y - predict
            for i in range(len(self.w)):
                self.w[i] += error.T.dot(self.X[:, i]) * self.learning_rate
            self.cost.append((1 / 2) * sum(error ** 2))
            if len(self.cost) > 2 and self.cost[-2] < self.cost[-1]:
                break
        return self

    def predict(self, X):
        return X.dot(self.w)

    @property
    def intercept_(self):
        return self.w[0]

    @property
    def coef_(self):
        return self.w[1:]


class LogisticRegression():
    def __init__(self, learning_rate, max_iter, random_state):
        self.learning_rate = learning_rate
        self.max_iter = max_iter
        self.w = None

    def fit(self, X, y):
        self.w = np.random.normal(loc=0.0, scale=1.0, size=self.X.shape[1])
        for _ in range(self.max_iter):
            pass

    def predict(self, X):
        pass

    @property
    def intercept_(self):
        return self.w[0]

    @property
    def coef_(self):
        return self.w[1:]
