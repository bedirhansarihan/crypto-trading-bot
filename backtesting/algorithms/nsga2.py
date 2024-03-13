import typing

from ..strategies.strategy import Strategy
from libs.utils.parameter_generator import generate_parameters
from algorithm import Algorithm


    
class Nsga2(Algorithm):

    def __init__(self, strategy_class: type[Strategy], population_size: int):
        super().__init__()
        self.population_size = population_size
        self.strategy_class = strategy_class
        self.population_params = []

    def run_algorithm(self) -> None:
        pass
