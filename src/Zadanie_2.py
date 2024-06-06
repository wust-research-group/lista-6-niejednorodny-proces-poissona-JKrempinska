import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def generate_event_times(lamb, T):
    N_t = np.random.poisson(lamb * T)
    event_times = T * np.sort(np.random.uniform(0, 1, N_t))
    return event_times

def l(s):
    return 1

def integrate_m(t):
    I, err = quad(l, 0, t)
    return I

print(integrate_m(1))
'''
def plot_event_times_step(event_times, T):
    plt.figure(figsize=(10, 4))
    plt.step(np.concatenate([[0], event_times]), np.arange(len(event_times) + 1), where='post')
    plt.title("Event Times Step Function")
    plt.xlabel("Time")
    plt.ylabel("Cumulative Number of Events")
    plt.show()

lamb = 2.0  
T = 10  

event_times = generate_event_times(lamb, T)
plot_event_times_step(event_times, T)'''
