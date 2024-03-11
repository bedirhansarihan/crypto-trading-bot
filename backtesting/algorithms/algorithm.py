from abc import ABC, abstractmethod


class Algorithm(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def run_algorithm(self):
        pass
