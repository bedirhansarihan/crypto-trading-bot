import pandas as pd
import numpy as np
from .strategy import Strategy
import talib
from libs.utils.decorators import timer, validate_param_info

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', 99)


@validate_param_info
class ProfitMaximizerStrategy(Strategy):
    __PARAMETERS_INFO__ = {
        "ma_type": {"name": "Moving Average Type (ema, sma)", "type": str, 'list': ['EMA', 'SMA'], 'default': 'SMA'},
        "ma_length": {"name": "Moving Average Length", "type": int, 'min': 5, 'max': 70, 'default': 10},
        "atr_length": {"name": "ATR Length", "type": int, 'min': 5, 'max': 70, 'default': 10},
        "atr_multiplier": {"name": "ATR multiplier", "type": float, 'min': 1.0, 'max': 5.0, 'decimals': 1,
                           'default': 3.0},
    }
    @timer
    def apply_strategy(self, df: pd.DataFrame) -> pd.DataFrame:

        last_row = len(df)
        #atr = talib.ATR(high=df['high'], low=df['low'], close=df['close'], timeperiod= 10)
        # ********* ATR ********
        src = df['close']
        high, low, prev_close = df['high'], df['low'], df['close'].shift()
        tr_all = [high - low, high - prev_close, low - prev_close]
        tr_all = [tr.abs() for tr in tr_all]
        tr = pd.concat(tr_all, axis=1).max(axis=1)
        atr = tr.ewm(alpha=1 / self.parameters['atr_length']).mean()
        # ********* ATR *********


        if self.parameters['ma_type'] == 'ema':
            mavg = talib.EMA(src, timeperiod=self.parameters['ma_length'])
        elif self.parameters['ma_type'] == 'sma':
            mavg = talib.SMA(src, timeperiod=self.parameters['ma_length'])
        else:
            mavg = talib.SMA(src, timeperiod=self.parameters['ma_length'])  # Default moving average type
        MAVG_array = mavg.values

        basic_ub = (mavg + (self.parameters['atr_multiplier'] * atr)).values
        basic_lb = (mavg - (self.parameters['atr_multiplier'] * atr)).values

        # Compute final upper and lower bands
        final_ub = np.zeros(last_row)
        final_lb = np.zeros(last_row)

        for i in range(self.parameters['atr_length'], last_row):
            final_ub[i] = basic_ub[i] if basic_ub[i] < final_ub[i - 1] or MAVG_array[i - 1] > final_ub[i - 1] else \
            final_ub[i - 1]
            final_lb[i] = basic_lb[i] if basic_lb[i] > final_lb[i - 1] or MAVG_array[i - 1] < final_lb[i - 1] else \
            final_lb[i - 1]

        pm = np.zeros(last_row)
        for i in range(self.parameters['atr_length'], last_row):
            pm[i] = final_ub[i] if pm[i - 1] == final_ub[i - 1] and MAVG_array[i] <= final_ub[i] else \
                final_lb[i] if pm[i - 1] == final_ub[i - 1] and MAVG_array[i] > final_ub[i] else \
                    final_lb[i] if pm[i - 1] == final_lb[i - 1] and MAVG_array[i] >= final_lb[i] else \
                        final_ub[i] if pm[i - 1] == final_lb[i - 1] and MAVG_array[i] < final_lb[i] else 0.00

        df['signal'] = np.where((pm > 0.00),
                                np.where((MAVG_array < pm), -1, 1),
                                np.NaN)
        #df['pm'] = pm
        #df['source'] = src
        df.fillna(0, inplace=True)

        return df




