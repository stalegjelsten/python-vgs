import random
 
n_x = 323
n_y = 301
mu_x = 168
mu_y = 180
s_x = 6
s_y = 8
grense = 175
antall_simuleringer = 100000
 
antall_gunstige = 0
 
# trekk antall_simuleringer elever
for i in range(antall_simuleringer):
    # Vi trekker en tilfeldig elev, men vi må finne ut om
    # eleven er gutt eller jente.
    # Det er 301 gutter. Hvis vi trekker et tilfeldig tall mellom
    # 1 og 301+323=624 så kan vi si at dersom tallet er mindre enn
    # eller lik 301, så er det en gutt.
    if (random.randint(1, n_x + n_y) <= n_y):
        # Her har vi altså trukket en gutt og vi trekker en tilfeldig gutt
        # fra en normalfordeling
        hoyde = random.gauss(mu_y, s_y)
    else:
        # ellers har vi trukket ei jente
        hoyde = random.gauss(mu_x, s_x)
 
    if (hoyde > grense):
        antall_gunstige += 1
 
print(f"Sannsynligheten for å trekke en tilfeldig eleve over 175 cm er "
      f"estimert til {(antall_gunstige / antall_simuleringer) * 100:.1f} "
      f"med {antall_simuleringer} simuleringer")
 
