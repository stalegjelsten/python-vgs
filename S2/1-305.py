# Write your code here :-)
# 1.305 s. 310 i læreboka
# Her prøver jeg alle naturlige tall opptil n. Jeg må
# sette n lik et tall, se linje 6.

n = 100


# lager en liste med tallene fra 1 til n
tall = [l for l in range(1,n+1)]

# regner ut summen av tallene fra 1 til n (dette kan vi også
# gjøre med formelen for aritmetisk rekke
minsum = sum(tall)

# det er ikke mulig å fordele et oddetall antall lapper likt i
# to bunker. Altså trenger jeg kun å sjekke for n ∈ partall
for i in range(2,n+1,2):

    # jeg oppretter en tom list som skal inneholde tall
    bunke1 = []
    bunke2 = []

    # her skal jeg fordele tallene i hver sin bunke slik at
    # summene blir like
    #
    # en måte vi *kan* fordele tallene på er å gjøre på samme måte
    # Gauss gjorde med tallene [1,100] ∈ ℕ
    #
    # Vi lager da par med det største og minste tallet, så 100 og 1
    # Disse to tallene legger vi i en bunke. Deretter tar vi 99 og 2
    # og legger disse i den andre bunken.
    # Vi må altså trekke ut to tall n/2 ganger
    for j in range(0,int(n/2),2):
        bunke1.append(tall[j])
        bunke1.append(tall[-(j+1)])
        bunke2.append(tall[j+1])
        bunke2.append(tall[-(j+2)])

    if sum(bunke1) == sum(bunke2):
        print(f"{i} fungerer")






