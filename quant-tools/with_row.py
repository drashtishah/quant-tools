import numpy as np
from .constants import *

def from_monthly_to_annualized_return(rm):
    return (1 + rm) ** MONTHS_PER_YEAR - 1

def from_quarterly_to_annualized_return(rq):
    return (1 + rq) ** QUARTERS_PER_YEAR - 1

def from_daily_to_annualized_return(rd):
    return (1 + rd) ** DAYS_PER_YEAR - 1

def from_monthly_to_annualized_volatility(vm):
    return vm * np.sqrt(MONTHS_PER_YEAR)