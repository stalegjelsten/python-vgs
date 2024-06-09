# Antall seksere på n terningkast
from random import randint
antall_kast = 1000
antall_seksere = 0                      # vi starter variabelen antall_seksere på 0
                                        # siden vi enda ikke har fått noen seksere
for i in range(antall_kast):
    terningkast = randint(1,6)          # trekker tilfeldig tall mellom 1 og 6
    if terningkast == 6:                # hvis terningkastet er 6 så...
        antall_seksere += 1             # øker vi variablen antall_seksere med 1
print(f"Vi fikk {antall_seksere} seksere på {antall_kast} terningkast.")
print(f"Dette tilsvarer en relativ frekvens på {antall_seksere / antall_kast * 100:.1f} %.")
