import random
import matplotlib.pyplot as plt
import numpy as np

N = 10000
antall_terninger = 8
resultater = []

for i in range(N):
    sum_øyne = 0
    for i in range(antall_terninger):
        terning = random.randint(1, 6)
        sum_øyne += terning

    resultater.append(sum_øyne)

utfall = np.arange(antall_terninger - 0.5, antall_terninger * 6 + 1 + 0.5)
plt.hist(resultater, bins=utfall, density=True)
