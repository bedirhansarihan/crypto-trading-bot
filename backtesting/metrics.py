from abc import ABC, abstractmethod

class PerformanceMetric(ABC):
    @abstractmethod
    def evaluate(self, df):
        """ df have open, high, low, close, volume, signal columns """

        pass


class PNL(PerformanceMetric):

    def evaluate(self, df):

        pass