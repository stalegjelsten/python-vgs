# %%
import matplotlib.pyplot as plt
import numpy as np

t_slutt = 15  # total lengde simulering [s]
dt = 0.001  # tidsintervall [s]
g = 9.81  # tyngdeaks [m/s^2]
r = 0.02  # luftmostanstandskonst [1/m]

n = int(t_slutt / dt)  # antall steg
t = np.linspace(0, t_slutt, n)  # array med tidspunkter [s]
s = np.zeros(n)  # tom array med pos [m]
v = np.zeros(n)  # tom array med fart [m/s]
a = (-g) * np.ones(n)  # array med aks hvor alle elementer er -g [m/s^2]


for i in range(n - 1):
    s[i + 1] = s[i] + v[i] * dt
    v[i + 1] = v[i] + a[i] * dt
    a[i + 1] = a[i + 1] + r * v[i + 1] ** 2

fig, axs = plt.subplots(3, 1, sharex=True)

fig.set_size_inches(6, 8)
for ax in axs.flat:
    ax.grid()

axs[0].plot(t, a)
axs[0].set_title("Akselerasjon")
axs[0].set_ylabel("$a$ [ms$^{-2}$]")

axs[1].plot(t, v)
axs[1].set_title("Fart")
axs[1].set_ylabel("$v$ [m/s]")

axs[2].plot(t, s)
axs[2].set_title("Posisjon")
axs[2].set_ylabel("$s$ [m]")
axs[2].set_xlabel("$t$ [s]")

print(fig.get_size_inches())

plt.show()