from random import randint

antall_gunstige = 0
N = 10000

for i in range(N):
    # lager 3 terninger
    t1 = randint(1,6)
    t2 = randint(1,6)
    t3 = randint(1,6)

    produkt = t1 * t2 * t3

    if produkt % 3 == 0:
        antall_gunstige = antall_gunstige + 1

print(f"Etter {N} simuleringer estimerer jeg at sannsynligheten"
    f"for at produktet av tre terninger er delelig med 3 er"
    f"omtrent {antall_gunstige/N*100:.2f} %.")
