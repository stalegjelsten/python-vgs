# 5.50
import math

# Setter opp hypergeometrisk modell
n = 48
k = 8
n_1 = 12


################################
# finne forventningsverdi
EX = 0
for i in range(k+1):
    P = (math.comb(n_1,i) * math.comb(n-n_1,k-i)) / (math.comb(n,k))
    EX += P*i


################################
# finne varians og std.avvik 
VarX = 0
for i in range(k+1):
    P = (math.comb(n_1,i) * math.comb(n-n_1,k-i)) / (math.comb(n,k))
    kvadratavvik = (i - EX)**2 * P                                      
    VarX += kvadratavvik

print(f"E(X) = {EX:.2f}. Var(X) = {VarX:.2f}. SD(X) = {math.sqrt(VarX):.2f}.")
