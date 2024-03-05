import random
import typing
from copy import deepcopy

from backtesting.strategies.strategy import Strategy


# TODO: should generating parameters be random or in order,
# TODO: check raise condition

def generate_parameters(strategy_instance: Strategy, population_size: int) -> typing.List[typing.Dict]:
    parameters = []

    i = 0
    while i != population_size:
        strategy_name = strategy_instance.__str__()
        for param_code, param in strategy_instance.__PARAMETERS_INFO__.items():
            if param['type'] == str:
                strategy_instance.parameters = (param_code, random.choice(param['list']))

            elif param['type'] == int:
                strategy_instance.parameters = (param_code, random.randint(param['min'], param['max']))

            elif param['type'] == float:
                strategy_instance.parameters = (param_code, round(random.uniform(param["min"], param["max"]),
                                                                  param["decimals"]))
        unique_param = deepcopy(strategy_instance.parameters)

        if unique_param in parameters:
            if len(parameters) == max_possible_param_variations(strategy_instance.__PARAMETERS_INFO__):
                raise ValueError("Population size bigger than max possible variations")
            continue

        parameters.append(unique_param)

        i += 1

    return parameters


def max_possible_param_variations(param_info) -> int:
    total_combinations = 1

    for param_code, param in param_info.items():
        if param['type'] == str:
            total_combinations *= len(param['list'])
        elif param['type'] == int:
            total_combinations *= param['max'] - param['min'] + 1
        elif param['type'] == float:
            decimal_places = 0 if 'decimals' not in param else param['decimals']
            total_combinations *= round((param['max'] - param['min']) * 10 ** decimal_places) + 1

    return total_combinations
