from abc import ABC, abstractmethod


class PerformanceMetric(ABC):
    @abstractmethod
    def evaluate(self, applied_df):
        """ df have timeframe, open, high, low, close, volume, signal columns """

        pass


class PNL(PerformanceMetric):

    def evaluate(self, applied_df):
        applied_df["pnl"] = applied_df["close"].pct_change() * applied_df["signal"].shift(1)
        applied_df["cum_sum"] = applied_df['pnl'].cumsum()
        applied_df['final_pnl'] = applied_df['cum_sum'].where(applied_df['signal'] != applied_df['signal'].shift(),
                                                              None)
        final_pnl = applied_df['final_pnl'].dropna().iloc[-1]

        pnl = round(final_pnl, 2)
        return pnl
