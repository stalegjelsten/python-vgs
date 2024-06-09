F = 1                   # første figur består av en sirkel
diff = 12               # differansen er 12 i starten

# lager ei løkke som går fra figur nummer 2 til og med 100
for n in range(2,101):
    F = F + diff        # legger til differansen på figurtallet
    diff = diff + 12    # øker differansen med 12

print(f"F_100 = {F}")
