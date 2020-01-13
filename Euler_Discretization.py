
"""
@author: tauamagalhaes
"""
##### Assuming a different approach for the Brownian movement

# S_t = S_(t-1) * e^[(r - 0.5 * std^2) * delta_t + std * (delta_t)^2 * Z_t]


### Libraries
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
from scipy.stats import norm
import matplotlib.pyplot as plt

### Data
ticker = 'MSFT'
data = pd.DataFrame()
data[ticker] = wb.DataReader(ticker, data_source = 'yahoo', start = '2010- 1 - 1')['Adj Close']  

# Log returns
log_returns = np.log(1 + data.pct_change())

# Assuming the value for the risk-free rate
r = 0.025

# Standard deviation
std = log_returns.std() * 250 ** 0.5
std = std.values

# Assuming T equals one year, so 250 days of transactions
T = 1.0
t_intervals = 250
delta_t = T / t_intervals

# Monte Carlo simulations
iterations = 10000

Z = np.random.standard_normal((t_intervals + 1, iterations))
S = np.zeros_like(Z)
S_0 = data.iloc[-1]
S[0] = S_0

# Euler discretization
for t in range(1, t_intervals + 1):
    S[t] = S[t - 1] * np.exp((r - 0.5 * std ** 2) * delta_t + std * delta_t ** 0.5 * Z[t])
    
S
S.shape
plt.figure(figsize = (10, 6))
plt.plot(S[:, :10]);

# Payoff
p = np.maximum(S[-1] - 110, 0)
p
p.shape

#Price of a call
C = np.exp(-r * T) * np.sum(p) / iterations
C 

