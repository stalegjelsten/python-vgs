# S2 5.131 s. 373

import numpy as np
from scipy.stats import hypergeom

n = 35
n_1 = 20
k = 5

# lager liste med x-verdier fra 0 til og med k
x = np.linspace(0,k,k+1)

# lager liste med P(X=x) verdier. Beregner vha. pmf-funksjonen
P = []
for i in range(k+1):
    P.append(hypergeom.pmf(i,n,n_1,k))


# i lista P så ligger nå de tilhørende sannsynligheter for P(X=0), P(X=1) osv.
# Indeks 0 er SSH P(X=0), dvs at P[2] = P(X=2).
print(f"P(X=2) = {P[2]:.3f}")

# summerer opp sannsynlighetene for P(X=2) + P(X=3) + P(X=4)
print(f"P(2<=X<=4) = {sum(P[2:5]):.3f}")

print(f"P(X=5) = {P[5]:.3f}")
