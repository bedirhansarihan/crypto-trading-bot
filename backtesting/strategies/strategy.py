from abc import ABC, abstractmethod
import pandas as pd

from libs.utils.validators import validate_parameters


class Strategy(ABC):
    __PARAMETERS_INFO__: dict

    def __init__(self):
        self._parameters = self.set_default_parameters()

    @property
    def parameters(self) -> dict:
        return self._parameters

    @parameters.setter
    def parameters(self, key_val: tuple) -> None:
        validate_parameters(key_val, self._parameters, self.__PARAMETERS_INFO__)

    def set_default_parameters(self) -> dict:
        parameters = {}
        for key, value in self.__PARAMETERS_INFO__.items():
            parameters[key] = value.get('default', None)

        return parameters

    @abstractmethod
    def apply_strategy(self, df: pd.DataFrame) -> pd.DataFrame:
        """ The returned dataframe must have a signal column and a value of 1 or -1
            Dataframe 'df' has timestamp open high low close signal columns              """

        pass

    def __str__(self) -> str:
        return self.__class__.__name__
