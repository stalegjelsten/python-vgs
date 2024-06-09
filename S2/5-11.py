# Write your code here :-)
# Write your code here :-)
from random import randint

gevinster_per_lodd = 4*[0]

antall_simuleringer = 1000
for i in range(antall_simuleringer):
    vinnerlodd = randint(1,5)        # vi velger posisjonen til et vinnerlodd
    vinnerlodd2 = randint(1,5)       # vi velger posisjonen til vinnerlodd2
    while vinnerlodd == vinnerlodd2:
        vinnerlodd2 = randint(1,5)
    gevinster_per_lodd[min(vinnerlodd, vinnerlodd2) - 1] += 1

##############################################
# Alternativ 2 for printing av resultatene
for i, gevinster in enumerate(gevinster_per_lodd):
    print(f"X = {i+1} | {gevinster / antall_simuleringer}")
##############################################

#print(f"I gjennomsnitt må man trekke {antall_lodd_trukket/antall_simuleringer} lodd for å få gevinst.")
##############################################
# Alternativ 1 for printing av resultatene
print("X = 1 |", gevinster_per_lodd[0] / antall_simuleringer)
print("X = 2 |", gevinster_per_lodd[1])
print("X = 3 |", gevinster_per_lodd[2])
print("X = 4 |", gevinster_per_lodd[3])
##############################################

