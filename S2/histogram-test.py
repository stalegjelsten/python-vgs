from scipy.stats import binom
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

N = 1000

# binom.rvs(n, p, size=N) trekker N stk fra binomisk fordeling
# med n og sannsynlighet p
X = binom.rvs(100, 0.3, size=N)

antall_stolper = 10     # antall stolper i histogrammet
ax.hist(X, bins=antall_stolper, density=False, edgecolor='white')
fig.show()
fig.savefig("hist-binom-matplotlib.svg")
