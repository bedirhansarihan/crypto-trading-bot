import random
from backtesting.strategies.strategy import Strategy


class ParameterGenerator:

    def __init__(self):
        pass
    #TODO contğinue
    def generate_parameters(self, strategy_instance: Strategy, population_size: int):

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
