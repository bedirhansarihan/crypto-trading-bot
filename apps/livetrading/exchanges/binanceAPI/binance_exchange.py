from abc import ABC, abstractmethod

from ..exchange import Exchange
from binance import Client


class BinanceExchange(ABC, Exchange, Client):

    pass

