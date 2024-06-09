# Write your code here :-)
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt


################# INNDATA
# dataene du skal gjøre regresjon på
x = [0, 2, 4, 6, 8, 10]
y = [1.4, 1.2, 1.1, 0.9, 0.8, 0.6]
#################


################# FUNKSJONSUTTRYKK TIL REGRESJON
# funksjonsuttrykket du bruker kan ha så mange koeffisienter som du ønsker
# denne funksjonen bruker to koeffisienter a og b
def modell(x, a, b):
    return a*x + b
#################


################# REGRESJON
# gjør regresjonen og lagrer koeffisientene i listen koeffisienter
# Syntaks: scipy.optimize.curve_fit(f, xdata, ydata, p0=None)
#

koeffisienter, kovarians = opt.curve_fit(modell, x, y)

#
# alt. 2: koeffisienter, kovarians = opt.curve_fit(modell, x, y, p0=[1, 0])
# hvis man legger inn p0=[250, 2, 0.05, ...] som en siste parameter til curve_fit
# så gir man regresjonen noen startverdier. Det kan være at regresjonen
# trenger litt hjelp for å finne riktig funksjonsuttrykk. Hvis du skal ha en
# logistisk funksjon og vet sånn ca. hva bæreevnen N må være så kan du legge
# inn denne
#
print("Koeffisienter:", koeffisienter)
print("Kovarians:", kovarians)
#################


################# SPREDNINGSPLOTT
# matplotlib.pyplot.scatter viser x-data og y-data som punkter (spredningsplott)
# Syntaks: plt.scatter(xdata, ydata, color="hotpink", s=2)
# her er color(string) navnet på en farge, og s(int) et tall som sier
# hvor stor hver prikk skal være
#
plt.scatter(x,y, color="blue")
#################
vg
