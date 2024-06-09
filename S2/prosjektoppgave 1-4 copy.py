#%%

import matplotlib.pyplot as plt

r = 2.05
n_liste = []
a_liste = []
n = 0
a = 0.5


for i in range(1, 101):
    n_liste.append(n)
    a_liste.append(a)
    # n = 0 # her må du skrive et uttrykk for n
    # a = 0 # her må du skrive et uttrykk for a_n
    n += 1
    a = r * a * (1 - a)

plt.plot(n_liste, a_liste)

#%%
import numpy as np
import matplotlib.pyplot as plt

interval = (2.8, 4)  # start, end
accuracy = 0.0001
reps = 600  # number of repetitions
numtoplot = 200
lims = np.zeros(reps)

fig, biax = plt.subplots()
fig.set_size_inches(16, 9)

lims[0] = np.random.rand()
for r in np.arange(interval[0], interval[1], accuracy):
    for i in range(reps - 1):
        lims[i + 1] = r * lims[i] * (1 - lims[i])

    biax.plot([r] * numtoplot, lims[reps - numtoplot :], "b.", markersize=0.02)

biax.set(xlabel="r", ylabel="x", title="logistic map")
plt.show()

#%%
i_lag = 1
min_sum = 0
n = 100

for i in range(1, n + 1):
    i_lag = i_lag + (i - 1) * 5
    print(i_lag)
    min_sum += i_lag

print(min_sum)

#%%
# sekskanttall
# 1  7  19  37
#  6  12  18

i_lag = 1
min_sum = 0
n = 100
for i in range(1, n + 1):
    i_lag += 6 * (i - 1)
    min_sum += i_lag
    print(i_lag)
print(min_sum)

#%%
# cellepopulasjoner
#
import matplotlib.pyplot as plt

n = 10000
x = 9900
y = 100
x_list = []
y_list = []

for i in range(1, n + 1):
    x_forrige = x
    x = round(x * 0.97 + 0.01 * y)
    y = round(y * 0.99 + x_forrige * 0.03)
    x_list.append(x)
    y_list.append(y)
    print(f"Friske: {x}. Syke: {y}")
plt.plot(range(n), x_list, range(n), y_list)

#%%
# 1, 3, 4, 8, 15, 27, 50…

n = 50
tall = 1
for i in range(1,n+1):
    if i == 1:
        tall = 1
    elif i == 2:
        forrige_tall = tall
        tall = 3
    elif i == 3:
        overforrige_siden = forrige_tall
        forrige_tall = tall
        tall = 4
    else:
        tall = tall + forrige_tall + overforrige_siden
        overforrige_siden = forrige_tall
        forrige_tall = tall

    print(tall)

#%%
# Python3 implementation to print the
# N terms of the series whose three
# terms are given
 
# Function to print the series
def printSeries(n, a, b, c):
 
    # Generate the ith term and
    # print it
    if (n == 1):
        print(a, end = " ");
        return;
     
    if (n == 2):
        print(a, b, end = " ");
        return;
     
    print(a, b, c, end = " ");
 
    for i in range (4, n + 1):
        d = a + b + c;
        print(d, end = " ");
        a = b;
        b = c;
        c = d;
     
# Driver Code
N = 10; a = 1; b = 3;
c = 4;
 
# Function Call
printSeries(N, a, b, c);


 

#%%
# 1.306 s. 310
#
# c_(n+1) = c_n + 2^n

c = 2
n = 20

for i in range(2,n+1):
    c = c + 2**i
    print(f"a_{i}: {c}")

