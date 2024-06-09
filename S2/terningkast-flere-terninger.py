#####################################################################
# Terninkast med flere terninger
#
# Dette programmet kan sammenligne antall øyne på ulike terninger og
# telle opp hvor mange gunstige utfall vi får
#
# Antall øyne på hver terning lagres i en liste
#####################################################################

from random import randint

antall_terninger = 3

terninger = []  # oppretter tom liste til terningene

for i in range(antall_terninger):
    terninger.append(randint(1, 6))  # legger til et terninkast til lista

################################################
#
# Funksjon: sjekk om alle terninger er over n
# Funksjonen tar inn en liste med terninger og 
# en grense n. Returnerer True eller False.
#
################################################
def sjekkOver(terninger,n):
    for terning in terninger:   # lager en løkke som går gjennom lista
        if terning <= n:        # sjekker om en terning er mindre eller
                                # lik n
            return False        
    return True                 # Hvis funksjonen aldri har funnet noen 
                                # terning mindre eller lik n, så retur-
                                # nerer vi True

################################################
#
# Sjekk om alle terninger er like
#
################################################
def sjekkLike(terninger):
    første_terning = terninger[0]   # lagrer det første terningkastet i ny variabel
    for terning in terninger:
        if terning == første_terning:
            continue
        else:
            return False
    return True



print(sjekkOver(terninger, 2))
