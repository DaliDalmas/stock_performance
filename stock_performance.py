import math
import pandas as pd

class StockPerformance:
    """
    class for measuring perfomance of securities
    """

    def __init__(self, data: pd.DataFrame) -> None:
        self.data: pd.DataFrame = data
        self.volatility: float = None
        self.performance_data: pd.DataFrame = None
        
        self.compute_performance()

    def percent_return(self, price_t1: float, price_t2: float):
        """
        return received at t2 for each dollar invested at t1
        """
        return (price_t2-price_t1)/price_t1

    def log_return(self, price_t1: float, price_t2: float):
        """
        I think the difference is not taken here because it could result to 0
        """
        return math.log(price_t2/price_t1)


    def compute_volatility(self, price_series_data: pd.Series):
        """
        """
        return price_series_data.std()

    def daily_price_range(high: float, low: float):
        """
        """
        return high-low

    def coefficient_of_variation(self, the_return: float):
        """
        """
        return the_return/self.volatility

    def sharpe_ratio(self, the_return: float):
        """
        """
        return self.volatility/the_return

    def compute_performance(self):
        """
        combining all the above functions
        """
        self.performance_data = self.data.copy()
        self.performance_data['Price_t_minus_1'] = self.performance_data['Price'].shift()
        self.performance_data.dropna(inplace=True)
        
        self.performance_data['percent_return'] = self.performance_data.apply(
            lambda row: self.percent_return(row['Price_t_minus_1'], row['Price']),
            axis=1
        )
        self.performance_data['log_return'] = self.performance_data.apply(
            lambda row: self.log_return(row['Price_t_minus_1'], row['Price']),
            axis=1
        )
        
        
        self.volatility = self.compute_volatility(self.performance_data['Price'])
        
        self.performance_data['Price_Range'] = self.performance_data['High']\
            - self.performance_data['Low']
        
        self.performance_data['coefficient_of_variation'] = self.performance_data['percent_return']\
        .apply(
            self.coefficient_of_variation
        )
        
        self.performance_data['sharpe_ratio'] = self.performance_data['percent_return']\
        .apply(
            self.sharpe_ratio
        )
        
        self.performance_data.drop(columns=['Change %', 'Open'], inplace=True)