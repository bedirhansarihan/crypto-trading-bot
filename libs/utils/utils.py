import importlib
import os
import warnings
from backtesting.strategies.strategy import Strategy
warnings.simplefilter(action='ignore', category=FutureWarning)


class StrategyLoader():
    @staticmethod
    def load_strategies() -> dict:
        strategies = {}

        strategy_modules = [f.replace('.py', '') for f in os.listdir('strategies') if
                            f.endswith('.py') and not f.startswith('__')]
        for module_name in strategy_modules:
            module = importlib.import_module(f'backtesting.strategies.{module_name}')

            for name in dir(module):
                obj_ref = getattr(module, name)
                if (
                        isinstance(obj_ref, type) and
                        issubclass(obj_ref, Strategy) and
                        obj_ref != Strategy and
                        obj_ref.__module__ == module.__name__
                ):
                    strategies[obj_ref.__name__] = obj_ref  # TODO OBJ_REF IS REFERENCE NOT OBJECT ITSELF

        return strategies

class UserInput:

    @staticmethod
    def input_parameters(strategy_instance: Strategy) -> None:

        for param_code, param in strategy_instance.__PARAMETERS_INFO__.items():
            while True:
                try:
                    strategy_instance.parameters[param_code] = param["type"](input(param["name"] + ": "))
                    break
                except ValueError:
                    continue



