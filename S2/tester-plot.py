# Write your code here :-)
import numpy as np
import time

x = np.linspace(0, 4*np.pi)

for i in range(len(x)):
    print((np.sin(x[i]),))
    time.sleep(0.005)


