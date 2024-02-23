import pandas as pd
import numpy as np
from .strategy import Strategy
import talib


class ProfitMaximizerStrategy(Strategy):
    __PARAMETERS_INFO__ = {
        "ma_type": {"name": "Moving Average Type (ema, sma)", "type": str, 'list': ['EMA', 'SMA']},
        "ma_length": {"name": "Moving Average Length", "type": int, 'min': 5, 'max': 70},
        "atr_length": {"name": "ATR Length", "type": int, 'min': 5, 'max': 70},
        "atr_multiplier": {"name": "ATR multiplier", "type": float, 'min': 1.0, 'max': 5.0, 'decimals': 1},
    }

    def apply_strategy(self, df: pd.DataFrame) -> pd.DataFrame:
        last_row = len(df)
        atr = talib.ATR(high=df['high'], low=df['low'], close=df['close'])
        src = df['close']

        if self.parameters['ma_type'] == 'ema':
            mavg = talib.EMA(src, timeperiod=self.parameters['ma_length'])
        elif self.parameters['ma_type'] == 'sma':
            mavg = talib.SMA(src, timeperiod=self.parameters['ma_length'])  # Default moving average type
        else:
            mavg = talib.SMA(src, timeperiod=self.parameters['ma_length'])  # Default moving average type

        mavg_array = mavg.values

        basic_ub = (mavg + (self.parameters['atr_multiplier'] * atr)).values
        basic_lb = (mavg - (self.parameters['atr_multiplier'] * atr)).values

        # Compute final upper and lower bands
        final_ub = np.zeros(last_row)
        final_lb = np.zeros(last_row)

        for i in range(self.parameters['atr_length'], last_row):
            final_ub[i] = basic_ub[i] if basic_ub[i] < final_ub[i - 1] or mavg_array[i - 1] > final_ub[i - 1] else \
                final_ub[i - 1]
            final_lb[i] = basic_lb[i] if basic_lb[i] > final_lb[i - 1] or mavg_array[i - 1] < final_lb[i - 1] else \
                final_lb[i - 1]

        pm = np.zeros(last_row)
        for i in range(self.parameters['atr_length'], last_row):
            pm[i] = final_ub[i] if pm[i - 1] == final_ub[i - 1] and mavg_array[i] <= final_ub[i] else \
                final_lb[i] if pm[i - 1] == final_ub[i - 1] and mavg_array[i] > final_ub[i] else \
                    final_lb[i] if pm[i - 1] == final_lb[i - 1] and mavg_array[i] >= final_lb[i] else \
                        final_ub[i] if pm[i - 1] == final_lb[i - 1] and mavg_array[i] < final_lb[i] else 0.00

        df['signal'] = np.where((pm > 0.00),
                                np.where((mavg_array < pm), -1, 1),
                                np.NaN)
        df['pm'] = pm
        df['source'] = src
        df.fillna(0, inplace=True)
        return df
