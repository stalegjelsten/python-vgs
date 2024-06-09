import random

N = 100000
innsats = 15

antall_øyne_over_10 = 0
for i in range(N):
    terning1 = random.randint(1, 6)
    terning2 = random.randint(1, 6)
    sum_terninger = terning1 + terning2
    if (sum_terninger) >= 10:
        antall_øyne_over_10 += sum_terninger

total_gevinst = 10 * antall_øyne_over_10
nettogevinst = total_gevinst - (innsats * N)

print(
    f"Etter {N} simuleringer har du tjent {nettogevinst/N:.2f} kr i gjennomsnitt per spill."
)
