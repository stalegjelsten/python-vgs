# P(S) = 0.8. P(T) = 0.75. Sannsynligheten for å skåre på straffespark

import random
ssh_tufte = 0.75
ssh_sleivdal = 0.8
N = 10000
antall_seire_sleivdal = 0

for i in range(N):
    antall_mål_tufte = 0
    antall_mål_sleivdal = 0
    for j in range(5):
        if random.random() < ssh_tufte:
            antall_mål_tufte += 1
        if random.random() < ssh_sleivdal:
            antall_mål_sleivdal += 1
    if antall_mål_sleivdal > antall_mål_tufte:
        antall_seire_sleivdal += 1

ssh_for_sleivdal_seier = antall_seire_sleivdal/N
print(f"Sleivdal vinner i {ssh_for_sleivdal_seier*100:.2f} % av tilfellene")
