from abc import ABC, abstractmethod
import pandas as pd

from libs.utils.validators import validate_parameters_info, validate_parameters


class Strategy(ABC):
    __PARAMETERS_INFO__: dict

    def __init__(self):
        validate_parameters_info(self.__PARAMETERS_INFO__)
        self._parameters = self.set_default_parameters()

    @property
    def parameters(self) -> dict:
        return self._parameters

    @parameters.setter
    def parameters(self, key_val: tuple) -> None:
        validate_parameters(key_val, self._parameters, self.__PARAMETERS_INFO__)

    def set_default_parameters(self):
        parameters = {}
        for key, value in self.__PARAMETERS_INFO__.items():
            parameters[key] = value.get('default', None)

        return parameters

    def display_dataframe(self, df):
        columns = df.columns.tolist()
        columns_to_show = ['timestamp', 'open', 'high', 'low', 'close', 'volume', 'signal']
        display_columns = [col for col in columns_to_show if col in columns]

        if display_columns:
            display_df = df[display_columns]

            if 'timestamp' in display_df.columns:
                display_df['timestamp'] = pd.to_datetime(display_df['timestamp'],
                                                         unit='s')

            print(display_df)

    @abstractmethod
    def apply_strategy(self, df: pd.DataFrame) -> pd.DataFrame:
        """ The returned dataframe must have a signal column and a value of 1 or -1
            Dataframe 'df' has timestamp open high low close signal columns              """

        pass

    def __str__(self) -> str:
        return self.__class__.__name__
