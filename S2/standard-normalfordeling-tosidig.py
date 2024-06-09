##########################
#
# finne P(X < a) vha.
# standard normalfordeling
#
##########################

from scipy.stats import norm

# legger inn opplysninger fra oppgaven
a = 170
b = 190
μ = 180
σ = 7

# beregner z
z1 = (a - μ) / σ
z2 = (b - μ) / σ

# finner Φ (Fi)
Φ1 = norm.cdf(z1)
Φ2 = norm.cdf(z2)

print(
    f"P({a} < X < {b}) = Φ({z2:.3f}) - Φ({z1:.3f}) ="
    f" {Φ2:.4f} - {Φ1:.4f} = {Φ2-Φ1:.4f}"
)
