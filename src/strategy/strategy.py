import abc
from abc import ABC


def Strategy(ABC):

    def __init__(self):
        pass
    @abc.abstractmethod
    def run(self):
        pass

class StrategyBacktest(Strategy):

    def __init__(self, rsi_period: int,
                 rsi_upper: int,
                 rsi_lower: int,
                 currency: str,
                 time_frame: str,
                 side: str):
        pass


    def run(self):
        df = self.open(currency, time_frame, side)
        df = self.calculate_features(df)
        df = self.calculate_signals(df)
        df = self.calculate_entries(df)
        df = self.calculate_exits(df)
        df_trades = self.calculate_trades(df)
        self.save(df_tardes)


    def open(self, currency, time_frame, side) -> pd.DataFrame:
        pass









