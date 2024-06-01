import random
 
N = 100_000
antall_gunstige = 0
 
for j in range(N):
    n = 20
    sum_karakterer = 0
    for i in range(n):
        # trekker et tilfeldig tall fra 1 til 3. Dette tilsvarer
        # skole A, B og C
        skole = random.randint(1,3)
        if skole == 1:
            # hvis det tilfeldige tallet er 1, så skal vi trekke 
            # tilfeldig elev fra skole A. I dette tilfellet har 
            # normalfordelingen my = 3.8 og sigma = 1.2             
            elev = random.gauss(3.8, 1.2)
        elif skole == 2:
            elev = random.gauss(3.4, 1.4)
        else:
            elev = random.gauss(4.1, 1.1)
        # vi legger til elevens karakter på summen
        sum_karakterer += elev
 
    snittkarakter = sum_karakterer / n
    
    if snittkarakter > 4:
        antall_gunstige += 1
 
print(f"Gjennomsnittskarakteren til de {N} elevene er {antall_gunstige/N:.3f}.")
