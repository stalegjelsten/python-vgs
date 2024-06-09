import matplotlib.pyplot as plt

fig, ax = plt.subplots()

frukter = ['epler', 'pærer', 'bananer', 'appelsiner']
antall = [40, 100, 30, 55]

ax.bar(frukter, antall)

ax.set_ylabel('Antall frukter')
ax.set_title('Salg av ulike frukter')
fig.show()

fig.savefig("frukter.svg")
