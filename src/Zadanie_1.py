import numpy as np
import matplotlib.pyplot as plt


def lambda_t(t):
    return 5 * np.sin(t) ** 2 + 1

T = 10

x = np.linspace(0,T,1000)
func_vals = np.zeros(1000)
for i in range(1000):
    func_vals[i] = lambda_t(i)

lambda_max = np.max(func_vals)  

N = np.random.poisson(lambda_max * T)
times = np.sort(np.random.uniform(0, T, N))

filtered_times = []
for t in times:
    if np.random.uniform(0, 1) < lambda_t(t) / lambda_max:
        filtered_times.append(t)

filtered_times = np.array(filtered_times)

step_times = np.concatenate(([0], filtered_times, [T]))
step_counts = np.arange(len(step_times))

plt.figure(figsize=(10, 4))
plt.step(step_times, step_counts, where='post')
plt.title("Niejednorodny proces Poissona")
plt.xlabel("Czas")
plt.ylabel("Liczba zdarzeń")
plt.show()



