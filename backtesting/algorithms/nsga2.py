import typing

from ..strategies.strategy import Strategy
from libs.utils.parameter_generator import generate_parameters


class Nsga2:

    def __init__(self, strategy_class: type[Strategy], population_size: int):
        self.population_size = population_size
        self.strategy_class = strategy_class
        self.population_params = []

    def create_population(self) -> typing.List[typing.Dict]:
        population = []

        parameters: list[dict] = generate_parameters(self.strategy_class(), self.population_size)

        for params in parameters:
            strategy_i = self.strategy_class()
            strategy_i.parameters = params
            self.population_params.append(strategy_i.parameters)

        return population
