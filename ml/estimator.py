from abc import ABCMeta, ABC


class BaseEstimator(ABC):
    @abstractmethod
    def fit(cls):
        pass

    @abstractmethod
    def predict(cls):
        pass


class Estimator(BaseEstimator):
    pass
