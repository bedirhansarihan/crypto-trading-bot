import typing
from binance import client, enums
from dataclasses import dataclass
from pandas import DataFrame
from numpy import ndarray, array


@dataclass
class Candle:
    timestamp: int
    open: float
    high: float
    low: float
    close: float
    volume: float


class DataFetcher:
    def __init__(self, klines_type: typing.Literal['SPOT', 'FUTURES'] = 'SPOT'):
        self.client = client.Client()
        self.klines_type = enums.HistoricalKlinesType.SPOT if klines_type == 'SPOT' else enums.HistoricalKlinesType.FUTURES

    def get_historical_klines_as_candles(self, symbol: str, interval: str, start_str=None, end_str=None,
                                         limit=1000) -> typing.List[Candle]:
        requests = self.client.get_historical_klines(symbol, interval, start_str, end_str, limit,
                                                     klines_type=self.klines_type)
        candles = []
        for c in requests:
            candles.append(Candle(c[0], c[1], c[2], c[3], c[4], c[5]))

        return candles

    def get_historical_klines_as_dataframe(self, symbol: str, interval: str, start_str=None, end_str=None,
                                           limit=1000) -> DataFrame:
        requests = self.client.get_historical_klines(symbol, interval, start_str, end_str, limit,
                                                     klines_type=self.klines_type)
        df = DataFrame(requests)
        df.columns = ['timeframe', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote', 'nof_trades',
                      'buy_base', 'buy_quote', 'unused']
        df.drop(columns=['close_time', 'quote', 'nof_trades', 'buy_base', 'buy_quote', 'unused'], inplace=True)
        return df

    def get_historical_klines_as_ndarray(self, symbol: str, interval: str, start_str=None, end_str=None,
                                         limit=1000) -> ndarray:
        requests = self.client.get_historical_klines(symbol, interval, start_str, end_str, limit,
                                                     klines_type=self.klines_type)

        arr = []
        for row in requests:
            arr.append(row[:-6])

        return array(arr)


if __name__ == '__main__':
    d = DataFetcher()
    print(d.get_historical_klines_as_ndarray('BTCUSDT', '1h')[1])
