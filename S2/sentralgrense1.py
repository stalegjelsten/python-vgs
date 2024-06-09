import random
import matplotlib.pyplot as plt
import numpy as np

N = 10000
resultater = []
antall_terninger = 50

for i in range(N):
    sum_øyne = 0
    for j in range(antall_terninger):
        terning = random.randint(1,6)
        sum_øyne += terning

    resultater.append(sum_øyne)

plt.hist(resultater, density=True, edgecolor="White")
plt.show()
