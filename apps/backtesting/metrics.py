from abc import ABC, abstractmethod

class Metric(ABC):

    @abstractmethod
    def evaluate(self):
        pass


class PNL():
    pass