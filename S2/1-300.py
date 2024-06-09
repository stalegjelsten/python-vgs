# Sinus S2 1.300

#############################
#
# Hvor mange greiner i år 50?
#
#############################

T = 1
for n in range(2,51):
    T = 3*T

print(n, T)

############################
#
# Samlede lengden av greiner i år 50?
#
############################

T = 1
S = 100
for n in range(2,51):
    T = 3*T
    S = S + T * (2/5)**(n-2) * 30
    print(f"n={n:2} T={T:25} S={S:15.2f}")

