import numpy as np

r = 1

sample_size = 1000

crossed = 0
for i in range(sample_size):
    theta = np.random.random() * (np.pi)
    mu = np.random.random()
    pro = mu + np.cos(theta) * r
    if pro > 1 or pro < 0:
        crossed += 1

print(crossed/sample_size)
