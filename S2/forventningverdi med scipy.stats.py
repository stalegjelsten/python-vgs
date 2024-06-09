from math import comb

n_1 = 18
n_2 = 12
n = n_1 + n_2
k = 5
forventningsverdi = 0
for x in range(k + 1):
    P = comb(n_1, x) * comb(n_2, 5 - x) / comb(n, k)
    forventningsverdi += x * P
print(f"E(X) = {forventningsverdi:.2f}")
