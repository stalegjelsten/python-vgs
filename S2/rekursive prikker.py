i = 1
a_i = 8

print("Dette programmet regner ut antallet røde prikker i en gitt figur.")
figurnummer = int(input("Hvilket figurnummer ønsker du å sjekke? "))

for i in range(2, figurnummer + 1):
    a_i = a_i + (i + 3)

print(f"Det er {a_i} røde prikker i figur {i}.")
