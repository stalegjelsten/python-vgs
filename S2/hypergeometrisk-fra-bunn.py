# %%


def fakultet(n):
    resultat = 1
    for i in range(2, n + 1):
        resultat = resultat * i
    return resultat


def nCr(n, k):
    teller = fakultet(n)
    nevner = fakultet(k) * fakultet(n - k)
    return teller / nevner


def hypergeometrisk(n, n_1, r, k):
    # Finner punktsannsynlighet P(X = k) i hypergeometrisk
    # n: totalt antall
    # n_1: antall av type 1
    # r: antall trekninger
    # k: hvor mange gunstige utfall vi ønsker
    teller = nCr(n_1, k) * nCr(n - n_1, r - k)
    nevner = nCr(n, r)
    return teller / nevner


# %%
