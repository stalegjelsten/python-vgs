# I et pengespill er innsatsen 6 kr, og du spiller ved å kaste en terning
# Hvis du får 6 øyne er gevinsten 15 kr
# Hvis du får 5 øyne er gevinsten 10 kr
# Hvis du får 4 øyne er gevinsten 5 kr
# Hvis du får 1, 2, eller 3 øyne får du ingen gevinst
# La X være nettogevinsten når du spiller en gang
#
# a) Bestem sannsynlighetsfordelingen til X
# b) Lag et diagram som viser sannsynlighetsfordelingen

from random import randint

antall_spill = 100_000
total_gevinst = 0
for i in range(antall_spill):
    terningkast = randint(1, 6)
    if terningkast == 6:            # sjekker terningkastet og utbetaler gevinst
        total_gevinst += 15
    elif terningkast == 5:
        total_gevinst += 10
    elif terningkast == 4:
        total_gevinst += 5
    total_gevinst -= 6              # ta bort 6 kr som var innsatsen

print(f"Vi kan forvente å tjene {total_gevinst / antall_spill} kr per spill.")
