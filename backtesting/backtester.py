from libs.utils.utils import StrategyLoader


class Backtester:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.strategies = StrategyLoader().load_strategies()  # references


if __name__ == '__main__':
    x = Backtester()
