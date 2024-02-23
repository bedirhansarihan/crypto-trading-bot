from abc import ABC, abstractmethod
import pandas as pd
class Strategy(ABC):
    __PARAMETERS_INFO__: dict

    def __init__(self):
        self.parameters = {key: None for key in self.__PARAMETERS_INFO__}

    @abstractmethod
    def apply_strategy(self, df: pd.DataFrame) -> pd.DataFrame:
        """ The returned dataframe must have a signal column and a value of 1 or -1
            Dataframe 'df' has open high low close timestamp columns              """

        pass

