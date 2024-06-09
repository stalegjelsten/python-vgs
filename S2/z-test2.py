########################
#
# test av gjennomsnitt med normalfordeling (Z-fordeling)
#
# i dette eksempelet tester H₀: μ = 180 mot Hₐ: μ ≠ 180 med σ = 7
# vi gjør et utvalg på 20 og får et gjennomsnitt på 179,3
# vi beregner p-verdien til dette resultatet
# (p-verdien er sannsynligheten for å få 179,3 eller mindre i gjennomsnitt
# på 20 observasjoner gitt at forventningsverdien μ = 180 er sann)
########################

from scipy.stats import norm
from math import sqrt

my = 100
sigma = 2
N = 50
X_strek = 99.4

SD_X_strek = sigma / sqrt(N)

# VENSTRESIDIG TEST
# vi skal finne P(X ≤ X_strek)
P = norm.cdf(X_strek, my, SD_X_strek)
print(f"Venstresidig test. p-verdien: P(X ≤ {X_strek}) = {P:.4f}")

# HØYRESIDIG TEST
# vi skal finne P(X ≥ X_strek)
P = 1 - norm.cdf(X_strek, my, SD_X_strek)
print(f"Høyresidig test. p-verdien: P(X ≥ {X_strek}) = {P:.4f}")

# DOBBELTSIDIG TEST
# vi skal finne P(X ≠ X_strek)
# Vi sjekker først om gjennomsnittet vårt et større eller mindre enn
# forventningsverdien. Hvis gjennomsnittet er mindre en forventningsverdien
# så bruker vi 2 * svaret av venstresidig test
# ellers bruker vi 2 * svaret av høyresidig test
#
# OBS: Læreboka deres regner ut p-verdi som om det var en ensidig test
# på s. 275 og s. 279. DET ER IKKE RIKTIG!

if X_strek <= my:
    P = 2 * norm.cdf(X_strek, my, SD_X_strek)
else:
    P = 2 * (1 - norm.cdf(X_strek, my, SD_X_strek))

print(f"Dobbeltsidig test. p-verdien: 2·P(X ≤ {X_strek}) = {P:.4f}")
