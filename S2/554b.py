# 5.50
import math
import numpy as np

# Setter opp hypergeometrisk modell
n = 48
k = 8
n_1 = 12

# lager en liste med x fra 0 til k
x = np.linspace(0,k,k+1)

# beregner sannsynlighetsfordelingen til X med formel for hypergeometrisk
# legger hver verdi inn i lista P
P = []
for i in range(k+1):
    P.append((math.comb(n_1,i) * math.comb(n-n_1,k-i)) / (math.comb(n,k)))

# beregner P*x for hvert element i listene
Px = P*x

# forventningsverdien er summen av P*x
EX = sum(Px)

# beregner kvadratavvikene. Variansen er summen av kvadratavvikene
kvadratavvik = (x-EX)**2 * P
VarX = sum(kvadratavvik)

print(f"E(X) = {EX:.2f}. Var(X) = {VarX:.2f}. SD(X) = {math.sqrt(VarX):.2f}.")

#for v in zip(x, P*x, 
