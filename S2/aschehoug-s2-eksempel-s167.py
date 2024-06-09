import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

################# FUNKSJONSUTTRYKK TIL REGRESJON
# funksjonsuttrykket du bruker kan ha så mange koeffisienter som du ønsker
# denne funksjonen bruker to koeffisienter a og b
def modell(t, a, b, c):
    return a * (np.exp(-b*t) - np.exp(-c*t))
#################


################# INNDATA
# dataene du skal gjøre regresjon på
x = [0.25, 0.50, 1, 2, 3, 5, 8, 12, 24]
y = [6.99, 9.64, 10.52, 10.20, 9.80, 8.18, 6.25, 3.48, 0.63]
#################


################# REGRESJON
# gjør regresjonen og lagrer koeffisientene i listen koeffisienter
# Syntaks: scipy.optimize.curve_fit(f, xdata, ydata, p0=None)
#
koeffisienter, kovarians = opt.curve_fit(modell, x, y, p0=[10, 1, 1])
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


################# LAGE X-VERDIER TIL GRAFEN TIL MODELLEN
# Her bør du tilpasse x_min og x_max i np.linspace til definisjonsområdet ditt.
# Akkurat nå så velger den 0 som minste verdi siden det er den minste verdien
# i lista x, og 10 som største verdi fordi 10 er den største verdien i lista.
#
x_min = min(x)  # Velger minste verdi fra lista x
x_max = max(x)  # Velger største verdi fra lista x
N = 1000        # Antall punkter vi ønsker bruke når vi tegner grafen
modell_x = np.linspace(x_min, x_max, N)
#################


################# BEREGNE Y-VERDIER TIL MODELLEN
# her har jeg brukt et triks i python som tar lista koeffisienter
# og "pakker ut" alle verdiene til lista. På den måten vil neste linje fungere
# uansett hvor mange koeffisienter du bruker i funksjonsuttrykket ditt
#
modell_y = modell(modell_x, *koeffisienter)
#################

################# PLOTTE MODELLEN
plt.plot(modell_x, modell_y, color="red")
plt.xlabel("Navn på x-akse")
plt.ylabel("Navn på y-akse")
plt.title("Tittel på diagrammet")
plt.legend(["Datapunkter", "Modell"])    # liste med forklaringer til hver sak
										# som plottes
plt.show()
#################
