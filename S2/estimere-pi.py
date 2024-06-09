#%%

import random
from math import sqrt

N = 1000000
antall_innenfor = 0
for i in range(N):
    x = 2*random.random()-1
    y = 2*random.random()-1
    r = sqrt(x**2+y**2)
    if r <= 1:
        antall_innenfor += 1

print(f"{antall_innenfor/N*4}")

# %%
