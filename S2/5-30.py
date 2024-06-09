# 5.30 a sannsynlighetsfordeling til X
from math import comb

gutter = 8
jenter = 7

for i in range(6):
    P = comb(gutter, i) * comb(jenter, 5 - i) / comb(gutter + jenter, 5)
    print(f"P(X = {i}) = {P:.3f}")


# oppgave b
ssh_mer_enn_2 = 0
for i in range(6):
    P = comb(gutter, i) * comb(jenter, 5 - i) / comb(gutter + jenter, 5)
    if i > 2:
        ssh_mer_enn_2 += P

print(f"P(X > 2) = {ssh_mer_enn_2:.3f}.")
