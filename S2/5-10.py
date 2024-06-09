# Write your code here :-)
# Write your code here :-)
from random import randint

gevinster_per_lodd = 5*[0]

antall_simuleringer = 1000
antall_lodd_trukket = 0
for i in range(antall_simuleringer):
    vinnerlodd = randint(1,5)
    antall_lodd_trukket += vinnerlodd
    gevinster_per_lodd[vinnerlodd-1] += 1


##############################################
# Alternativ 2 for printing av resultatene
for i, gevinster in enumerate(gevinster_per_lodd):
    print(f"X = {i+1} | {gevinster}")
##############################################

print(f"I gjennomsnitt må man trekke {antall_lodd_trukket/antall_simuleringer} lodd for å få gevinst.")
##############################################
# Alternativ 1 for printing av resultatene
#print("X = 1 |", gevinster_per_lodd[0])
#print("X = 2 |", gevinster_per_lodd[1])
#print("X = 3 |", gevinster_per_lodd[2])
#print("X = 4 |", gevinster_per_lodd[3])
##############################################
vinnerlodd = randint(1,5)
vinnerlodd2 = randint(1,5)
while vinnerlodd == vinnerlodd2:
    vinnerlodd2 = randint(1,5)
