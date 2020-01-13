
"""
@author: tauamagalhaes
"""
##### Monte Carlo Simulations to predict Gross Profit

### Libraries
import numpy as np
import matplotlib.pyplot as plt

### Defining parameters for the simulation
# Expected revenue (in millions dollars)
rev_m = 170
# Standard deviation of the expected revenue (in million dollars)
rev_std = 20
# Number of iterations
iterations = 1000

### Gaussian distirbution to generate data
rev = np.random.normal(rev_m, rev_std, iterations)
rev

### Plot
plt.figure(figsize = (15,6))
plt.plot(rev)
plt.axhline(y=170, color='r', linestyle='-')
plt.axhline(y=190, color='r', linestyle='dotted')
plt.axhline(y=150, color='r', linestyle='dotted')
plt.show

### Subtracting Cost of Goods Solds
# Assuming that 60% of the revenue is used in the production, with 10% of standard deviation
COGS = - (rev * np.random.normal(0.6, 0.1))
plt.figure(figsize = (15, 6))
plt.axhline(y = COGS.mean(), color = 'r', linestyle = '-')
plt.axhline(y = COGS.mean() - COGS.std(), color = 'r', linestyle = 'dotted')
plt.axhline(y = COGS.mean() + COGS.std(), color = 'r', linestyle = 'dotted')
plt.plot(COGS)
plt.show()
COGS.mean()
COGS.std()

### Gross Profit
Gross_Profit = rev + COGS
Gross_Profit

plt.figure(figsize = (15, 6))
plt.plot(Gross_Profit)
plt.show()

max(Gross_Profit)
min(Gross_Profit)

Gross_Profit.mean()
Gross_Profit.std()

# Histogram
plt.figure(figsize = (10, 6))
plt.hist(Gross_Profit, bins = 20)
plt.show()