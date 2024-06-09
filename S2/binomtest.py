########################
#
# test av andel i binomisk forsøk
#
# EKSEMPEL
# ========
# La X være antallet lyspærer som er brukbare, og la p være sannsynligheten
# for at en tilfeldig valgt lyspære er brukbar
#
# I dette eksempelet tester H₀: p = 0.9 mot Hₐ: p ≠ 0.9
# Vi har tatt en stikkprøve på 20 lyspærer. 5 av pærene er defekte.
#
########################

from scipy.stats import binomtest

# binomtest tar inn (antall_suksesser, antall_forsøk, p_0, alternative={'two-sided', 'greater', 'less'})

antall_suksesser = 15
antall_forsøk = 20
p_0 = 0.9

# alternative kan være "two-sided" (dobbeltsidig), "greater" (p er større enn
# nullhypotesen), "less" (p er mindre enn nullhypotsen)
p = binomtest(antall_suksesser, antall_forsøk, p_0, alternative="two-sided")

# p.pvalue henter ut p-verdien fra objektet p
print(f"P-verdi: {p.pvalue:.4f}")
