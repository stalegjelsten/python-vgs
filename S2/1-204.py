import matplotlib.pyplot as plt
import numpy as np

# Write your code here :-)
a = 1
for n in range(1,11):
    ledd = 0
    delsum = 0
    while delsum < n:
        ledd = ledd + 1
        delsum = delsum + 1/ledd
    print(ledd)

x = np.linspace(0,4*np.pi,1000)
y = np.sin(x)
plt.plot(x,y)

plt.show()
