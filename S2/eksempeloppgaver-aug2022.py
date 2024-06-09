#%%
# oppgave 7

from math import sqrt
from unicodedata import decimal

a = 0
b = 2
n = 10000


def f(x):
    return x**2 + 2


I = 0
h = (b - a) / n

for i in range(n):
    I = I + f(a + i * h) * h


print(round(I, 3))
# %%
# På en skole er det 323 jenter og 301 gutter.
# X er høyde på tilf. jente
# Y er høyde på tilf. gutt
# Anta at X og Y er normalfordelt med
#   μₓ = 168
#   μᵧ = 180
#   σₓ = 6
#   σᵧ = 8
# Lag et program som du kan bruke til å smulere sannsynligheten for at en
# tilfeldig valgt elev er høyere enn 175 cm.

from scipy.stats import norm

grense = 175
antall_simuleringer = 1000

n_x = 323
n_y = 301
mu_x = 168
mu_y = 180
s_x = 6
s_y = 8


antall_over = 0
for i in range(antall_simuleringer):
    X = norm.rvs(mu_x, s_x, n_x).round(decimals=2)
    Y = norm.rvs(mu_y, s_y, n_y).round(decimals=2)

    elever = list(X) + list(Y)

    for j in elever:
        if j > grense:
            antall_over += 1


print(f"Andelen elever over {grense} cm er: {antall_over/((n_x+n_y)*antall_simuleringer) * 100:.1f} %")

# %%
print(f"{i}: elev nummer {elever.index(175)} av {len(elever)} ({elever.index(175)/len(elever) * 100:.1f} %)")

# %% [markdown]
Hvordan skal vi klare 

#%%
import numpy as np
import matplotlib.pyplot as plt

n_x = 323
n_y = 301
mu_x = 168
mu_y = 180
s_x = 6
s_y = 8
grense = 175
antall_simuleringer = 1000


x = np.random.normal(mu_x, s_x, size=n_x*antall_simuleringer)
y = np.random.normal(mu_y, s_y, size=n_y*antall_simuleringer)
elever = np.concatenate((x,y), axis=0)
elever.sort()

grense_elev = np.argmax(elever>grense)
print(f"{(1-(grense_elev)/len(elever))*100:.1f} % av elevene er høyere enn {grense} cm")


plt.hist(elever, bins=50, density=True)


# %%
import numpy as np
import random

n_x = 323
n_y = 301
mu_x = 168
mu_y = 180
s_x = 6
s_y = 8
grense = 175
antall_simuleringer = 10000

antall_gunstige = 0

# trekk antall_simuleringer elever
for i in range(antall_simuleringer):
    # Vi trekker en tilfeldig elev, men vi må finne ut om
    # eleven er gutt eller jente.
    # Det er 301 gutter. Hvis vi trekker et tilfeldig tall mellom
    # 1 og 301+323=624 så kan vi si at dersom tallet er mindre enn
    # eller lik 301, så er det en gutt.
    if (random.randint(1, n_x + n_y) <= n_y):
        # Her har vi altså trukket en gutt og vi trekker en tilfeldig gutt
        # fra en normalfordeling
        hoyde = np.random.normal(mu_y, s_y)
    else:
        # ellers har vi trukket ei jente
        hoyde = np.random.normal(mu_x, s_x)

    if (hoyde > grense):
        antall_gunstige += 1

print(f"Sannsynligheten for å trekke en tilfeldig elever over 175 cm er "
      f"estimert til {(antall_gunstige / antall_simuleringer) * 100:.1f} "
      f"med {antall_simuleringer} simuleringer")

#%%
import numpy as np
from scipy.stats import norm

n_x = 323
n_y = 301
mu_x = 168
mu_y = 180
s_x = 6
s_y = 8
grense = 175
N = 100000

antall_over = 0
for i in range(N):
    if (np.random.randint(1,n_x+n_y+1)) > 301:
        if (norm.rvs(mu_x, s_x, size=1) > grense):
            antall_over += 1
    else:
        if (norm.rvs(mu_y, s_y, size=1) > grense):
            antall_over += 1

print(f"Det er {antall_over/N:.2%}")


# %%
# kapittelprøve s1 oppgave 6e
# Sleivdal 80% sjanse
# Anta at hver av de 5 spillerne til Tufte har 75 % sjanse for å skåre på sitt straffespark.
#Bruk simuleringer til å finne sannsynligheten for at Sleivdal skårer flere mål på sine
#5 straffespark enn Tufte gjør på sine 5 straffespark
import numpy as np

antall_forsøk = 10_000
ssh_sleivdal = 0.8
ssh_tufte = 0.75
antall_seire_sleivdal = 0

for i in range(antall_forsøk):
    mål_sleivdal = 0
    mål_tufte = 0
    for j in range(5):
        if np.random.random() < ssh_sleivdal:
            mål_sleivdal += 1
        if np.random.random() < ssh_tufte:
            mål_tufte += 1
    if mål_sleivdal > mål_tufte:
        antall_seire_sleivdal += 1
        
print(antall_seire_sleivdal)

# %%
import random
import numpy as np
print(f"Random \t Numpy random")
for i in range(10):
    print(random.randint(0,3), "\t" , np.random.randint(0,3))

#%%
import random
print(random.random())

#%%
mu = 5
sigma = 1
from scipy.stats import norm
print(norm.rvs(mu, sigma))

import numpy as np
print(np.random.normal(mu, sigma))
# %%
from random import randint

antall_gunstige = 0
N = 10000

for i in range(N):
	# lager 4 terninger
	t1 = randint(1,6)
	t2 = randint(1,6)
	t3 = randint(1,6)
	t4 = randint(1,6)
	
	if (t1 == 6) or (t2 == 6) or (t3 == 6) or (t4 == 6):
		antall_gunstige = antall_gunstige + 1

print(f"Vi får minst en sekser i {antall_gunstige/N*100:.2f} % av tilfellene.")
#%%
from random import randint

antall_gunstige = 0
antall_terninger = 4
N = 10000

for i in range(N):
    for terning in range(antall_terninger):
        if (randint(1,6) == 6):
            antall_gunstige += 1
            break # break stanser den innerste for-løkka

print(f"Vi får minst en sekser i {antall_gunstige/N*100:.2f} % av tilfellene.")

#%%
i
