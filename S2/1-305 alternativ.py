# Write your code here :-)

n = 100
for i in range(2, n + 1,2):
    # modulusoperatoren gir resten fra en deling
    rest = (i**2 + i) % 4
    if rest == 0:
        print(f"{i} lapper kan deles likt i to bunker")
