import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
x = np.linspace(0,3,100)
y1 = x**2
y2 = 2*x

ax.plot(x, y1, c="blue", label="$x^2$")
ax.plot(x, y2, c="red", linestyle="dashed", label="$2x$")
ax.legend()
ax.set_title("$x^2$ og $2x$")
fig.show()
