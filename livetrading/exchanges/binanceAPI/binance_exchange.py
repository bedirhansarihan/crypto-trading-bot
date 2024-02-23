from abc import ABC, abstractmethod

from ..exchange import Exchange
from binance import Client as BaseClient


class BinanceExchange(Exchange, BaseClient):

    pass


BinanceExchange.get_exchange_info()