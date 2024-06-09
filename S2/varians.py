#########################################
#
# Denne beregner variansen i hypergeometrisk
# fordeling ved å først beregne
# forventningsverdien og deretter summere
# kvadratavvikene
#
# Vi har n_1 objekter av type 1
# Vi har n-2 objekter av type 2
# Vi har til sammen n objekter
# Vi trekker k objekter
#
#########################################
from math import comb, sqrt

n_1 = 12
n_2 = 36
n = n_1 + n_2
k = 8
forventningsverdi = 0
for x in range(k + 1):
    P = comb(n_1, x) * comb(n_2, k - x) / comb(n, k)
    forventningsverdi += x * P

varians = 0
for x in range(k + 1):
    P = comb(n_1, x) * comb(n_2, k - x) / comb(n, k)
    varians += (x - forventningsverdi) ** 2 * P
stdavvik = sqrt(varians)
print(f"E(X) = {forventningsverdi:.2f}, Var(X) = {varians:.2f}, σ = {stdavvik:.2f}.")
