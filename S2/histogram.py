########################
#
# Tegner histogram for sannsynlighetsfordelinger
# Du kan endre type fordeling ved å kommentere ut
# linjene for X
#
########################
from scipy.stats import uniform
from scipy.stats import norm
from scipy.stats import binom
import matplotlib.pyplot as plt

N = 10000

# uniform.rvs(a, b, size=N) trekker N stk fra uniform
# fordeling mellom tallene a og b
X = uniform.rvs(0,1, size=N)

# norm.rvs(μ, σ, size=N) trekker N stk fra normalfordeling
# med μ og σ
#X = norm.rvs(180,7, size=N)

# binom.rvs(n, p, size=N) trekker N stk fra binomisk fordeling
# med n og sannsynlighet p
#X = binom.rvs(N, 0.3, size=N)

antall_stolper = 10     # antall stolper i histogrammet
plt.hist(X, bins=antall_stolper, density=True, edgecolor='white')
plt.show()
