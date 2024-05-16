import numpy as np
import matplotlib.pyplot as plt

# Parameters
T = 1  # Total time
N = 1000  # Number of time steps
dt = T / N  # Time step size
mu = 0  # Drift rate
sigma = 0.1  # Volatility

# Initialize arrays
t = np.linspace(0, T, N+1)
W = np.zeros(N+1)  # Wiener process (Brownian motion)

# Generate random increments (standard normal distribution)
dW = np.sqrt(dt) * np.random.randn(N)

# Compute Brownian motion
for i in range(1, N+1):
    W[i] = W[i-1] + dW[i-1]

# Generate Brownian motion paths
S = mu * t + sigma * W

# Plot Brownian motion
plt.figure(figsize=(10, 5))
plt.plot(t, S, label='Brownian Motion')
plt.title('Brownian Motion Simulation')
plt.xlabel('Time')
plt.ylabel('Position')
plt.grid(True)
plt.legend()
plt.show()
