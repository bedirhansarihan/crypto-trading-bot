from libs.utils.utils import StrategyLoader, UserInput
from libs.data_fetcher import DataFetcher
from strategies.profit_maximizer_strategy import ProfitMaximizerStrategy


class Backtester:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.strategies = StrategyLoader().load_strategies()  # references
        self.data_fetcher = DataFetcher()

    def start(self):
        pass


    def single_test(self, strategy_instance):
        df = self.data_fetcher.get_historical_klines_as_dataframe('BTCUSDT', '1d')

        print(strategy_instance.apply_strategy(df))

if __name__ == '__main__':
    b = Backtester()
    pm = ProfitMaximizerStrategy()
    b.single_test(pm)
