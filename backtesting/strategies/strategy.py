from abc import ABC, abstractmethod
import pandas as pd

from libs.utils.validator import validate_parameters_info


class Strategy(ABC):
    __PARAMETERS_INFO__: dict

    def __init__(self):
        validate_parameters_info(self.__PARAMETERS_INFO__)
        self._parameters = {key: None for key in self.__PARAMETERS_INFO__}

    @property
    def parameters(self):
        return self._parameters

    @parameters.setter
    def parameters(self, value):
        pass

    @abstractmethod
    def apply_strategy(self, df: pd.DataFrame) -> pd.DataFrame:
        """ The returned dataframe must have a signal column and a value of 1 or -1
            Dataframe 'df' has open high low close timestamp columns              """
        pass
