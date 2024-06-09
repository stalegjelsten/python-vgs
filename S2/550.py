# 5.50
import math

x = [0, 50, 200]
P = [195/360, 120/360, 45/360]

################################
#
# finne forventningsverdi
#
################################

EX = 0
for i in range(len(x)):       # denne kjører 3 ganger siden lengden av x er 3
                              # lengden av lista x. Du kan bytte ut med tallet 3 hvis
                              # du ønsker, men da blir ikke koden like gjenbrukbar
    Px = x[i] * P[i]          # regner ut P * x for hver x
    EX += Px                  # legger sammen resultatene i variabelen EX


################################
#
# finne varians og std.avvik
#
################################
    
VarX = 0
for i in range(len(x)):
    kvadratavvik = (x[i] - EX)**2 * P[i]    # regner kvadratavviket
    VarX += kvadratavvik                    # legger til hvert kvadratavvik i variabelen 
                                            # VarX

print(f"E(X) = {EX:.2f}. Var(X) = {VarX:.2f}. SD(X) = {math.sqrt(VarX):.2f}.")
