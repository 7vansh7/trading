import numpy as np 
from scipy.stats import norm 

r = 0.01
S = 22450
K = 22350
T = 4/252
sigma = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
type = 'c'

def blackScholes(r, S, K, T, sigma, type):
    "Calculate BS price of call/put"
    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    try:
        if type == "c":
            price = S*norm.cdf(d1, 0, 1) - K*np.exp(-r*T)*norm.cdf(d2, 0, 1)
        elif type == "p":
            price = K*np.exp(-r*T)*norm.cdf(-d2, 0, 1) - S*norm.cdf(-d1, 0, 1)
        return price
    except:
        print("Please confirm option type, either 'c' for Call or 'p' for Put!")


with open('./price.txt','w') as f:
    for x in sigma:
        text= f" σ = {x},option value = {blackScholes(r, S, K, T, x,type)} \n "
        f.write(text)
