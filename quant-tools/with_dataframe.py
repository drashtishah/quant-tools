import pandas as pd
import numpy as np
from .constants import *

def get_returns_from_prices(df):
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

def get_volatility_from_returns(df):
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

def get_annualized_volatility_from_returns(df):
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

def get_compound_return_from_returns(df):
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

def get_annualized_return_from_returns(df):
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