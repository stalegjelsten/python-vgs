# Dette programmet finner sannsynlighet og kummulativ sannsynlighet ved
# binomisk fordeling og tegner histogram med sannsynlighetfordelingen
# Kummulativ SSH brukes til å finne P(X <= k)
from scipy.stats import binom
import matplotlib.pyplot as plt
import numpy as np

n = 10
p = 0.30
# np.linspace(0, 5, 6) gir oss en liste med 6 elementer. Det første elementet
# er 0, det siste elementet er 5. Altså blir lista [0, 1, 2, 3, 4, 5]
x_verdier = np.linspace(0, n, n + 1)
# 11*[0] gir en liste med 11 nuller. Kommandoen under gir en liste med like mange
# nuller som vi har x-verdier
y_verdier = (n + 1) * [0]
# lager en liste med n+1 nuller som skal lagre den kummulative verdien
y_kummulativ = (n + 1) * [0]
for i in range(n + 1):
    P = binom.pmf(i, n, p)  # finner SSH for P(X=i) ved binomial-
    # fordeling
    y_verdier[i] = P  # endrer element nr i i lista y_verdier
    # til den beregnede SSH
    if i == 0:
        y_kummulativ[i] = P
    else:  # tar forrige kummulative verdi og legger
        # til sannsynligheten P(X = i)
        y_kummulativ[i] = y_kummulativ[i - 1] + P
    print(f"P(X = {i:2d}) = {P:.3f} | P(X <= {i:2d}) = {y_kummulativ[i]:.3f}")
    # printer i (:2d gjør at vi tar opp
    # plassen til 2 siffer slik at utskriften
    # blir penere). {P:.3f} skriver ut SSH
    # med 3 desimal.30
# matplotlib.pyplot.bar(x, y) gir et stolpediagram hvor x er en liste
# med x-verdiene til stolpene og y er en liste ned y-verdiene til stolpene
# width=1 er en innstilling som gjør at stolpene blir stående inntil hverandre.
plt.bar(x_verdier, y_verdier, width=1)
# plt.plot(x_verdier, y_kummulativ, c="red")
plt.title("Binomisk fordeling")
plt.show()
