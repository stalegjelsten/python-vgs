# %%
a = 2
d = 3

for i in range(10):
    print(a, end=", ")
    a = a + d
# %%
innskudd = 50_000
rente = 0.025
aarlig_innskudd = 5000

for i in range(2021, 2031):
    innskudd = innskudd*(1+rente)
    print(f"Innskudd i {i}: {innskudd:.2f}")
    innskudd = innskudd + aarlig_innskudd
# %%
