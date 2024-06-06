import numpy as np
import matplotlib.pyplot as plt

def nonhomogeneous_poisson(lambda_func, T, alpha=2):
    t = 0
    S = []
    lambda_max = max(lambda_func(np.linspace(0, T, 1000)))

    while t < T:
        u = np.random.rand()
        lambda_t = lambda_func(t)
        p = 1 - np.exp(-alpha * lambda_t / lambda_max)
        if u < p:
            S.append(t)
        t += np.random.exponential(1 / lambda_max)
    return S

def lambda_func(t):
    return np.sin(t)

for i in range(3):
    x = nonhomogeneous_poisson(lambda_func, 100)
    y = np.arange(0, len(x))
    plt.step(x,y)
plt.show()


