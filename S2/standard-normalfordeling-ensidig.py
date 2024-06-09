##########################
#
# finne P(X < a) vha.
# standard normalfordeling
#
##########################

from scipy.stats import norm

# legger inn opplysninger fra oppgaven
a = 170
μ = 180
σ = 7

# beregner z
z = (a - μ) / σ

# finner Φ (Fi)
Φ = norm.cdf(z)

print(f"P(X < {a}) = Φ({z}) = {Φ:.4f}")
