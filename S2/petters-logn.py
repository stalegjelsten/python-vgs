from scipy.stats import t
import numpy as np
import matplotlib.pyplot as plt
mu = 180                                # gjennomsnitt i nullhypotesen
obs = [ 220, 205, 209, 256, 214 ]       # observasjoner
alfa = 0.05                             # signifikansnivå på testen
x_gjennomsnitt = np.average(obs)        # regner ut gjennomsnittet av observasjoner
s = np.std(obs, ddof=1)                 # finner standardfeilen
n = len(obs)                            # finner antall observasjoner
df = n - 1                              # antall frihetsgrader = n - 1
t_obs = ( x_gjennomsnitt - mu ) / ( s/np.sqrt(n)) # beregner t-verdi
P = t.cdf(t_obs, df)                    # finner sannsynlighetn for P(T<=t)

# tegner student-t fordelingen mellom -5 og 5
x = np.linspace(-5,5,1000)  # lager 1000 punkter mellom -5 og 5
nedre_grense = 0.05         # øvre og nedre grense for konfidensintervallet.
ovre_grense = 0.95          # sett til 0.025 og 0.975 for tosidig test med
                            # signifikansnivå 0.05
T = t.pdf(x, df=df)         # beregner sannsynlighetstettheten i hvert punkt
                            # husk at sannsynlighetstetthet er det samme som
                            # f(x) og at sannsynlighet er ∫ f(x) dx
                            # over intervall fra -∞ fram til t_obs
plt.plot(x,T)               # plotter sannynlighetstetthet mot x


nedre_persentil = t.ppf(nedre_grense, df=df)          # regner ut nedre persentil
ovre_persentil = t.ppf(ovre_grense, df=df)           # regner ut øvre persentil

# fyller området mellom nedre og øvre grense med blåfarge
plt.fill_between(x, 0, T, where=(nedre_persentil < x) & (ovre_persentil > x))
plt.text(0,0.1, f"{ovre_grense-nedre_grense:.2%}", ha="center", c="white")
plt.vlines(t_obs,0,max(T), color="magenta", label="t_observator")
plt.legend()
plt.show()
