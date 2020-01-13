
"""
@author: tauamagalhaes
"""
##### Monte Carlo Simulation to predict Stock price

# Brownian Movement
# price_1 = price_0 * e^(ln(price_1/price_0))

# drift: directions of the return rates in the past [ln(price_1/price_0)]
# drift = [r_m - 0.5 * r_std^2]
# Drift can be thinked as the daily expected return of the stock

# volatility: random variable
# Assuming gaussian distribution 
# random_variable = std * Z(Rand(0;1))

# price_1 = price_0 * e^([r_m - 0.5 * r_std^2] + std * Z(Rand(0;1))

# We will run this simultaion a 1000 times

### Libraries
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
from scipy.stats import norm

### Data of Microsoft from Yahoo Finance
ticker = 'MSFT'
data = pd.DataFrame()
data[ticker] = wb.DataReader(ticker, data_source = 'yahoo', start = '2010- 1- 1')['Adj Close']

#Log returns
log_returns = np.log(1 + data.pct_change())
log_returns.tail()
data.plot(figsize=(10, 6))
log_returns.plot(figsize=(10, 6))

# Defining the parameters of the Brownian Movement
u = log_returns.mean()
u

var = log_returns.var()
var

drift = u - (0.5 * var)
drift

std = log_returns.std()
std

# Transforming the data in array
type(drift)
np.array(drift)
type(std)
np.array(std)

# Random variable Z
norm.ppf(0.95)

x = np.random.rand(10, 2)
x

Z = norm.ppf(np.random.rand(10, 2))
Z

# Forecasting for 1000 days using 10 series
t_intervals = 1000
iterations = 10

# Daily returns
daily_returns = np.exp(drift.values + std.values * norm.ppf(np.random.rand(t_intervals, iterations)))
daily_returns

# Price_0
S_0 = data.iloc[-1]
S_0

# Price list
price_list = np.zeros_like(daily_returns)
price_list[0] = S_0
for t in range(1, t_intervals):
    price_list[t] = price_list[t -1] * daily_returns[t]
price_list

plt.figure(figsize = (10, 6))
plt.plot(price_list)