# estimerer pi

import random
import math
N = 10_000_000
antall_gunstige = 0
areal_kvadrat = 2*2
for i in range(N):
    # lager x- og y-koordinater i intervallet [-1 , 1> (burde strengt
    # tatt vært i intervallet [-1, 1], men det er tror jeg er vanskelig
    # å få til, og det skal ikke ha noe å si så lenge den variablene er
    # kontinuerlige)
    x = 2*random.random() - 1
    y = 2*random.random() - 1

    # sjekker om (x² + y² ≤ 1). Vi kjenner igjen pytagoras. 1 er hypotenusen
    # og radius til sirkelen. Dersom x²+y² = 1 så befinner vi oss nøyaktig på
    # kanten av sirkelen. Dersom x²+y²<1 så befinner vi oss innenfor kanten av
    # sirkelen. Altså må vi befinne oss på sirkelen dersom (x² + y² ≤ 1)
    if x**2 + y**2 <= 1:
        antall_gunstige += 1

estimat_pi = antall_gunstige/N * areal_kvadrat
avvik = estimat_pi - math.pi
print(f"{antall_gunstige/N*100:.2f} % av ballene traff på innsiden av sirkelen.")
print(f"Estimatet vårt av π er {estimat_pi:.6f}.")
print(f"Differansen mellom estimatet og π er {avvik:.6f}.")
