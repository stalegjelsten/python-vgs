import math 

rod = 9
bla = 6

for n in range(18, 201, 2): 
    # lager ei løkke som tester alle partall fra 18 til og med 200
    n1 = int(n/2) # halvparten av ballene er røde (må gjøre om til heltall)
    ssh = ( math.comb(n1, rod) * math.comb(n1, bla) ) / math.comb(n, (rod+bla))
    print(f"Ved {n} baller P(R=9) = {ssh:.5f}")
