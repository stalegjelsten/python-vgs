from scipy.stats import norm

my = 180
sigma = 7
######################
#
# norm.cdf(x, my, sigma) regner ut
# P(X <= x)
#
######################
x1 = 175
x2 = 185
print(norm.cdf(x2, my, sigma) - norm.cdf(x1, my, sigma))
