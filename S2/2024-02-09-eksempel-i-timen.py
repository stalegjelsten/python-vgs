# Write your code here :-)
from random import randint

# en tom liste med alle resultatene
resultater = []
antall_serier = 1000

for i in range(antall_serier):
    antall_lodd_igjen = 5
    lodd = 6
    while (lodd > 1):
        lodd = randint(1,antall_lodd_igjen)
        antall_lodd_igjen -= 1

    antall_lodd_trukket = 4-antall_lodd_igjen
    resultater.append(antall_lodd_trukket)

print(f"X = 1 | {resultater.count(1)}")
print(f"X = 2 | {resultater.count(2)}")
print(f"X = 3 | {resultater.count(3)}")
print(f"X = 4 | {resultater.count(4)}")
print(f"X = 5 | {resultater.count(5)}")
