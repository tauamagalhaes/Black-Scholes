
"""
@author: tauamagalhaes
"""

##### Libraries

import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

##### Data

#The data was collected about the adjusted closeing prices from Yahoo Finance, 
#for Proctor & Gamble, Apple, Microsoft and S&P500. From 2010 to the present.

assets = ['PG', 'AAPL', 'MSFT', '^GSPC']
pf_data = pd.DataFrame()

for a in assets:
    pf_data[a] = wb.DataReader(a, data_source = 'yahoo', start = '2010-1-1')['Adj Close']
    
pf_data.tail()

#Normalizing the data for 100 base and plotting
(pf_data / pf_data.iloc[0] * 100).plot(figsize = (10, 5))


##### Markowitz Frontier

#Log returns
log_returns = np.log(pf_data / pf_data.shift(1))
log_returns.mean() * 250
log_returns.cov() * 250
log_returns.corr()

#Number of assets
num_assets = len(assets)
num_assets

#Random weights
weights = np.random.random(num_assets)
weights /= np.sum(weights)
weights
weights[0]+weights[1]+weights[2]+weights[3]

#Expected Portfolio Return
np.sum(weights * log_returns.mean()) * 250

#Expected Portfolio Variance
np.dot(weights.T, np.dot(log_returns.cov() * 250, weights))

#Expected Portfolio Volatility
np.sqrt(np.dot(weights.T, np.dot(log_returns.cov() * 250, weights)))

#Considering a thousand combinations of those four tickers
pfolio_returns = []
pfolio_volatilities = []

for x in range (1000):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    pfolio_returns.append(np.sum(weights * log_returns.mean()) * 250)
    pfolio_volatilities.append(np.sqrt(np.dot(weights.T, np.dot(log_returns.cov() * 250, weights))))
    
pfolio_returns = np.array(pfolio_returns)
pfolio_volatilities = np.array(pfolio_volatilities)
pfolio_returns, pfolio_volatilities

portfolios = pd.DataFrame({'Return': pfolio_returns, 'Volatility': pfolio_volatilities})
portfolios.head()
portfolios.tail()

portfolios.plot(x = 'Volatility', y = 'Return', kind = 'scatter', figsize = (10, 6));
plt.xlabel('Expected Volatility')
plt.ylabel('Expected Return')

##### Beta of a stock

#Usually is calculated for five years

assets = ['MSFT', '^GSPC']
beta_data = pd.DataFrame()

for a in assets:
    beta_data[a] = wb.DataReader(a, data_source = 'yahoo', start = '2014-12-18', end = '2019-12-19')['Adj Close']
    
beta_data.tail()

#Logarithmic returns
sec_returns = np.log(beta_data/beta_data.shift(1))
cov = sec_returns.cov()*250
cov

#Covariance between the stock and the market
cov_with_market = cov.iloc[0,1]
cov_with_market

#Market volatility
market_var = sec_returns['^GSPC'].var() * 250
market_var

#Beta of Microsoft
MSFT_beta = cov_with_market / market_var
MSFT_beta

##### CAPM

# r = rf + beta * (rm - rf)
# Expected return of Microsoft
# Reasonable values for USA
# rf = 0.025
# (rm - rf) = 0.05 

MSFT_er = 0.025 + MSFT_beta * 0.05
MSFT_er

##### Sharpe Ratio

# Sharpe_ratio = (r_bond - rf)/[std(bond)]

MSFT_sharpe = (MSFT_er - 0.025)/(sec_returns['MSFT'].std() * 250 ** 0.5)
MSFT_sharpe

