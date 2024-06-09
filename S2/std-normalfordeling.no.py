##########################
#
# finne P(a < X < b) vha.
# standard normalfordeling
#
##########################

from scipy.stats import norm

# legger inn opplysninger fra oppgaven
a = 173
b = 187
μ = 180
σ = 7

# beregner z
z_a = (a - μ) / σ
z_b = (b - μ) / σ

# finner Φ (Fi)
Φ_a = norm.cdf(z_a)
Φ_b = norm.cdf(z_b)

# finne sannsynligheten for P(a < X <b) vha Φ
P = Φ_b - Φ_a

# lage en pen utskrift
print(f"P({a} < X < {b}) = Φ({z_b:.4f}) - Φ({z_a:.4f}) = {Φ_b:.4f} - {Φ_a:.4f} = {P:.4f}")
