
"""
@author: tauamagalhaes
"""

##### Black Scholes

# C(S, t) = N(d_1) - N(d_2) * K * e^[-r * (T - t)]

# d_1 = [1 / s * ((T - t)^0.5)] * [ln(S / K) + (r + ((s^2)/2)) * (T -t)]

# d_2 = d_1 - s * ((T - t)^0.5)

# S: current stock price
# K: option stock price
# t: time until option expires
# r: risk-free interest rate
# s: sample standard deviation
# N: Standard Gaussian distribution
# e: exponential term
# C: Call premium

### Libraries
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
from scipy.stats import norm

# Defining functions to calculate d_1 and d_2
def d_1(S, K, r, std, T):
    return (np.log(S / K) + (r + std ** 2 / 2) * T) / (std * np.sqrt(T))

def d_2(S, K, r, std, T):
    return (np.log(S / K) - (r + std ** 2 / 2) * T) / (std * np.sqrt(T))

# Defining Black-Sholes-Merlon equation
def BSM(S, K, r, std, T):
    return (S * norm.cdf(d_1(S, K, r, std, T))) - (K * np.exp(-r * T) * norm.cdf(d_2(S, K, r, std, T)))

### Data
ticker = 'MSFT'
data = pd.DataFrame()
data[ticker] = wb.DataReader(ticker, data_source = 'yahoo', start = '2010- 1 - 1')['Adj Close']    

# Defining S
S = data.iloc[-1]
S

# Log returns
log_returns = np.log(1 + data.pct_change())

# Defining std
std = log_returns.std() * 250 ** 0.5

# Assuming the values for the other parameters
r = 0.025
K = 110.0
T = 1

d_1(S, K, r, std, T)
d_2(S, K, r, std, T)
BSM(S, K, r, std, T)