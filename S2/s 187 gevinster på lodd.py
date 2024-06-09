# Write your code here :-)
from random import randint

gevinster_per_lodd = 4*[0]

antall_simuleringer = 400
for i in range(antall_simuleringer):
    vinnerlodd = randint(1,4)
    gevinster_per_lodd[vinnerlodd-1] += 1

##############################################
# Alternativ 1 for printing av resultatene
print("X = 1 |", gevinster_per_lodd[0])
print("X = 2 |", gevinster_per_lodd[1])
print("X = 3 |", gevinster_per_lodd[2])
print("X = 4 |", gevinster_per_lodd[3])
##############################################

##############################################
# Alternativ 2 for printing av resultatene
for i, gevinster in enumerate(gevinster_per_lodd):
    print(f"X = {i+1} | {gevinster}")
##############################################

