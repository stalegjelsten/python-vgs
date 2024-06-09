# Eksempel s. 186–187 alternativ løsning
from random import randint

##################
# Hovedprinsipper
# - Vi kaller loddene 1, 2, 3 og 4
# - Vi sier at vinnerloddet alltid er nr 1
##################

resultater = []
antall_simuleringer = 400

for i in range(antall_simuleringer):

    # det er alltid 4 lodd i krukken i starten
    lodd_i_krukken = 4

    # neste linje er nødvendig for at while-løkka skal starte
    lodd = 5

    while trukket_lodd_nr > 1:
        # vi trekker et tilfeldig lodd av dem som er igjen i krukka
        lodd = randint(1, lodd_i_krukken)
        lodd_i_krukken -= 1

    # vi finner ut hvor mange lodd som ble trukket og legger
    # til svaret i lista resultater
    antall_lodd_trukket = 4 - lodd_i_krukken
    resultater.append(antall_lodd_trukket)


# vi teller antallet enere, toere, treere og firere i lista resultater
print(f"X = 1 | {resultater.count(1)}")
print(f"X = 2 | {resultater.count(2)}")
print(f"X = 3 | {resultater.count(3)}")
print(f"X = 4 | {resultater.count(4)}")

# for i in range(1,5):
#     print(f"X = {i} | {resultater.count(i)}")

print(f"{sum(resultater) / 400}")
