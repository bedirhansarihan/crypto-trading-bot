import typing
from abc import ABC, abstractmethod


class PerformanceEvaluator:
    def __init__(self, metrics):
        self.metrics = metrics
        self.results = {}

    def evaluate_all(self, applied_df):
        for metric_name, metric_instance in self.metrics.items():
            result = metric_instance.evaluate(applied_df)
            self.results[metric_name] = result


# TODO check whether value should be added or not

class PerformanceMetric(ABC):
    P_INF = 9999
    N_INF = -9999

    @abstractmethod
    def evaluate(self, applied_df) -> typing.Any:
        pass


class ProfitAndLoss(PerformanceMetric):
    def evaluate(self, applied_df):
        applied_df["pnl"] = applied_df["close"].pct_change() * applied_df["signal"].shift(1)
        applied_df["cum_sum"] = applied_df['pnl'].cumsum()
        applied_df['final_pnl'] = applied_df['cum_sum'].where(applied_df['signal'] != applied_df['signal'].shift(), None)
        final_pnl = applied_df['final_pnl'].dropna().iloc[-1]

        # Sonuçları yazdır
        pnl = round(final_pnl, 2)
        return pnl if pnl > 0 and pnl < 2 else self.N_INF  # TODO OR EKLENDI


class MaximumDrawdown(PerformanceMetric):
    def evaluate(self, applied_df):
        pass


class WinLoss(PerformanceMetric):
    def evaluate(self, applied_df):
        pass
