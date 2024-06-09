# Ada har laget et spill der det koster 30 kr å delta
# Man kaster en firesidet terning nummerert fra 1 til 4
# Man vinner 10 kr for hvert øye terningen viser
# La Y være nettogevinsten.
#
# Bruk python til å estimere forventningsverdien til Y
# (Tenk på forventningsverdi som hvor mye vi kan forvente
# å tjene dersom vi blir med på spillet)


# Nettogevinst = gevinst - 30 kr
from random import randint

pris = 30
kr_per_øye = 10
antall_kast = 100_000
samlet_gevinst = 0
for i in range(antall_kast):
    terningkast = randint(1, 4)
    samlet_gevinst += kr_per_øye * terningkast

forventningsverdi = (samlet_gevinst - antall_kast * pris) / antall_kast
print(
    f"Vi tjener {samlet_gevinst} kr på {antall_kast} omganger, men "
    f"betaler {antall_kast * pris} i inngangspenger."
    f"Dette gir en forventningsverdi på {forventningsverdi}"
)
