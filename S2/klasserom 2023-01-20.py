# Write your code here :-)
from random import randint
gevinster_per_lodd = 4*[0]
antall_simuleringer = 400

for i in range(antall_simuleringer):
    vinnerlodd = randint(1,4)
    gevinster_per_lodd[vinnerlodd-1] += 1

print(gevinster_per_lodd)
