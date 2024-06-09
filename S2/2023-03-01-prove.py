########################################
#
# eksempel uten bruk av eksterne pakker
#
########################################

from math import comb, sqrt

n = 360
p = 0.67

μ = 0
for x in range(n + 1):
    P = comb(n, x) * p**x * (1 - p) ** (n - x)
    μ += x * P

VarX = 0
for x in range(n + 1):
    P = comb(n, x) * p**x * (1 - p) ** (n - x)
    VarX += (x - μ) ** 2 * P

σ = sqrt(VarX)
print(f"E(X) = {μ:.2f} og σ = {σ:.2f}")
######################################################

########################################
#
# eksempel med bruk av eksterne pakker
#
########################################

from scipy.stats import binom
from math import sqrt

n = 360
p = 0.67

μ = 0
for x in range(n + 1):
    P = binom.pmf(x, n, p)
    μ += x * P

VarX = 0
for x in range(n + 1):
    P = binom.pmf(x, n, p)
    VarX += (x - μ) ** 2 * P

σ = sqrt(VarX)
print(f"E(X) = {μ:.2f} og σ = {σ:.2f}")
######################################################

########################################
#
# eksempel med bruk av lister
#
########################################

from scipy.stats import binom
import numpy as np

n = 360
p = 0.67

μ = 0

x = np.linspace(0, n, n + 1)
P = binom.pmf(x, n, p)
EX = sum(x * P)
VarX = sum((x - EX) ** 2 * P)
SDX = np.sqrt(VarX)
print(f"E(X) = {EX:.2f} og σ = {SDX:.2f}")
