# Write your code here :-)
# Dette programmet finnet punktsannsynligheten i et
# hypergeometrisk forsøk
from scipy.stats import hypergeom
# Vi skal bruke hypergeom.pmf() for å finne SSH
# hypergeom.pmf(x, n, n_1, k) trenger 4 parametere:
#   x: x-verdien i P(X = x), altså alle verdier i utfallsrommet
#   n: totalt antall objekter i krukka
#   n_1: antall objekter av type 1
#   k: hvor mange objekter vi skal trekke

# her trekker vi 5 objekter fra en krukke med 15 objekter
# det er 8 objekter av type 1 (og dermed 7 av type 2)
# Vi sjekker sannsynligheten for at vi trekker nøyaktig 2
# stk av type 1 (altså P(X = 2))

x = 2
n = 15
k = 5
n_1 = 8

P = hypergeom.pmf(x, n, n_1, k)
print(f"P(X = {x}) = {P:.3f}")
