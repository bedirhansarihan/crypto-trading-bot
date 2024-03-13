from ..strategies.strategy import Strategy
from backtesting.metrics import PerformanceEvaluator


class BacktestInfo:
    """ This class is used as a instance of each backtest. It is not related to database"""
    _current_id = 1

    def __init__(self, strategy_instance: Strategy, performance_evaluator: PerformanceEvaluator):
        self.id = BacktestInfo.create_unique_id()
        self.strategy = strategy_instance
        self.performance_evaluator = performance_evaluator

    @classmethod
    def create_unique_id(cls) -> int:
        current_id = cls._current_id
        cls._current_id += 1
        return current_id

    @classmethod
    def total_instance(cls) -> int:
        return cls._current_id
