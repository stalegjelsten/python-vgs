from scipy.stats import norm # henter nødvendige pakker for normalfordeling
from random import randint

N = 10_000
antall_gunstige = 0
for j in range(N):
    n = 20
    sum_karakterer = 0
    for i in range(n):
        # trekker et tilfeldig tall fra 1 til 3. 
        # Dette tilsvarer skole A, B og C
        skole = randint(1,3)
        if skole == 1:
            # hvis det tilfeldige tallet er 1, så skal vi trekke 
            # tilfeldig elev fra skole A. I dette tilfellet har 
            # normalfordelingen my = 3.8 og sigma = 1.2             
            # # vi trekker en tilfeldig elev med norm.rvs()
            elev = norm.rvs(3.8,1.2)
        elif skole == 2:
            elev = norm.rvs(3.4,1.4)
        else:
            elev = norm.rvs(4.1,1.1)
        # vi legger til elevens karakter på summen
        sum_karakterer += elev
    if sum_karakterer/n > 4:
        # hvis snittkarakteren er over 4 så har vi et gunstig utfall
        antall_gunstige += 1

print(f"Etter {N} simuleringer estimerer jeg at sannsynligheten for at"
      f"gjennomsnittskarakteren er over 4 til {antall_gunstige/N:.4f}.")
