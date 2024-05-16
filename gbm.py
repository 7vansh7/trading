import numpy as np
import matplotlib.pyplot as plt


# drift coefficent
mu = 0.13
# number of steps
n = 1000
# time in years
T = 10/252
# number of sims
M = 1000
# initial stock price
S0 = 22144
# volatility
sigma = 0.3


def gbm(mu,n,T,M,S0,sigma):
    # calc each time step
    dt = T/n
    
    # simulation using numpy arrays
    St = np.exp(
        (mu - sigma ** 2 / 2) * dt
        + sigma * np.random.normal(0, np.sqrt(dt), size=(M,n)).T
    )
    
    # include array of 1's
    St = np.vstack([np.ones(M), St])
    
    # multiply through by S0 and return the cumulative product of elements along a given simulation path (axis=0).
    St = S0 * St.cumprod(axis=0)
    
    
    
    # Define time interval correctly
    time = np.linspace(0,T,n+1)
    
    # Require numpy array that is the same shape as St
    tt = np.full(shape=(M,n+1), fill_value=time).T
    
    
    plt.plot(tt, St)
    plt.xlabel("Years $(t)$")
    plt.ylabel("Stock Price $(S_t)$")
    plt.title(
        "Realizations of Geometric Brownian Motion\n $dS_t = \mu S_t dt + \sigma S_t dW_t$\n $S_0 = {0}, \mu = {1}, \sigma = {2}$".format(S0, mu, sigma)
    )
    plt.yticks(np.arange(18000,28000,500))
    plt.savefig(fname='gbm.png')
    plt.show()

gbm(mu,n,T,M,S0,sigma)