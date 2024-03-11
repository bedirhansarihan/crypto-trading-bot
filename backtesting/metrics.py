import typing
from abc import ABC, abstractmethod


class PerformanceMetricsCollector:
    def __init__(self, metrics):
        self.metrics = metrics
        self.results = {}

    def evaluate_all(self, applied_df):
        for metric_name, metric_instance in self.metrics.items():
            result = metric_instance.evaluate(applied_df)
            self.results[metric_name] = result


class PerformanceMetric(ABC):

    def __init__(self):
        self.value = None
    @abstractmethod
    def evaluate(self, applied_df) -> typing.Any:
        pass


class ProfitAndLoss(PerformanceMetric):
    def evaluate(self, applied_df):
        pass


class MaximumDrawdown(PerformanceMetric):
    def evaluate(self, applied_df):
        pass


class WinLoss(PerformanceMetric):
    def evaluate(self, applied_df):
        pass
