# Write your code here :-)
from scipy.stats import binom
print(binom.pmf(2, 5, 0.5)) # denne skriver ut sannsynligheten
						    # for å få 2 kron på 5 myntkast

# denne utfører 5 myntkast og skriver ut hvor stor
# sannsynligheten er for å få {0, 1, …, 5} kron
for i in range(6):
  P = binom.pmf(i,5,0.5)
  print(f"Sannsynligheten for {i} kron er {round(P, 3)}.")
