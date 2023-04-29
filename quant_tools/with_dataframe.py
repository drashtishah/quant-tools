import pandas as pd
import numpy as np
from .constants import *

def get_returns_from_prices(df:pd.DataFrame) -> pd.DataFrame:
    '''Get returns from prices
    
    Input: Pandas DataFrame
     - date as index (must be datetime object)
     - assets/stocks as columns
     - prices as values
    Output: Pandas DataFrame
     - date as index
     - assets/stocks as columns
     - returns as values (not in %)
    '''
    df = df.sort_index()
    return df.pct_change().dropna(how='all')

def get_volatility_from_returns(df:pd.DataFrame) -> pd.Series:
    '''Get volatility from returns
    
    Input: Pandas DataFrame
     - date as index (must be datetime object)
     - assets/stocks as columns
     - returns as values
    Output: Pandas Series
     - assets/stocks as columns
     - standard deviation/volatility as values (not in %)
    '''
    return df.std()

def get_annualized_volatility_from_returns(df:pd.DataFrame) -> pd.Series:
    '''Get annualized volatility from returns
    
    Input: Pandas DataFrame
     - date as index (must be datetime object)
     - assets/stocks as columns
     - returns as values
    Output: Pandas Series
     - assets/stocks as columns
     - annualized volatility as values (not in %)
    '''
    return df.std()*np.sqrt(MONTHS_PER_YEAR)

def get_compound_return_from_returns(df:pd.DataFrame) -> pd.Series:
    '''Get compound return from returns per column
    
    Input: Pandas DataFrame
     - date as index (must be datetime object)
     - assets/stocks as columns
     - returns as values
    Output: Pandas Series
     - assets/stocks as columns
     - compund returns as values (not in %)
    '''
    return (df + 1).prod() - 1

def get_annualized_return_from_returns(df:pd.DataFrame) -> pd.Series:
    '''Get annualized compound return from returns per column
    
    Input: Pandas DataFrame
     - date as index (must be datetime object)
     - assets/stocks as columns
     - returns as values
    Output: Pandas Series
     - assets/stocks as columns
     - annualized returns as values (not in %)
    '''
    number_of_periods = df.shape[0]
    return (df + 1).prod()**(MONTHS_PER_YEAR/number_of_periods) - 1

def get_wealth_index_from_returns(df:pd.DataFrame, amount:float=1000.0) -> pd.DataFrame:
    '''Get wealth index from returns
    
    Input: Pandas DataFrame
     - date as index (must be datetime object)
     - assets/stocks as columns
     - returns as values
    Output: Pandas DataFrame
     - date as index
     - assets/stocks as columns
     - wealth index as values
    '''
    df = amount * (df + 1)
    return df.cumprod()

def get_previous_peaks_from_wealth_index(df:pd.DataFrame) -> pd.DataFrame:
    '''Get previous peaks from wealth index
    
    Input: Pandas DataFrame
     - date as index (must be datetime object)
     - assets/stocks as columns
     - wealth index as values
    Output: Pandas DataFrame
     - date as index
     - assets/stocks as columns
     - previous peaks as values
    '''
    return df.cummax()

def get_drawdown_from_returns(df:pd.DataFrame, amount:float=1000.0) -> pd.DataFrame:
    '''Get drawdown from returns
    
    Input: Pandas DataFrame
     - date as index (must be datetime object)
     - assets/stocks as columns
     - returns as values
    Output: Pandas DataFrame
     - date as index
     - assets/stocks as columns
     - drawdown as values (not in %)
    '''
    wealth_index = get_wealth_index_from_returns(df, amount)
    previous_peaks = get_previous_peaks_from_wealth_index(wealth_index)
    return (wealth_index - previous_peaks) / previous_peaks

def get_max_drawdown_from_returns(df:pd.DataFrame, amount:float=1000.0) -> pd.DataFrame:
    '''Get maximum drawdown from returns
    
    Input: Pandas DataFrame
     - date as index (must be datetime object)
     - assets/stocks as columns
     - returns as values
    Output: Pandas DataFrame
    '''
    drawdown = get_drawdown_from_returns(df, amount)
    return pd.DataFrame({'Date': drawdown.idxmin(), 'Maximum Drawdown': drawdown.min()})