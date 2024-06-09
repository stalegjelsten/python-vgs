lån = float(input("Lånebeløp: "))
rentefot = float(input("Rentefot: "))
antall_år = int(input("Antall år i nedbetalingstid: "))
terminer_per_år = int(input("Antall terminer per år: "))

n = antall_år * terminer_per_år
v = (1 + rentefot / 100) ** (1 / terminer_per_år)
F = (1 - 1 / v ** n) / (v - 1)
terminbeløp = lån/F

print(f"Terminbeløpene er på {round(terminbeløp)} kr.")
print(f"Rentene var på til sammen "
      f"{round(n*terminbeløp - lån)} kr.")
