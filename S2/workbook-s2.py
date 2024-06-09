#%%

antall_ledd = 1000
#%%

forrige_ledd = 1
to_ledd_siden = 1
print(forrige_ledd)
print(to_ledd_siden)

for n in range(3, antall_ledd + 1):
    ledd = forrige_ledd + to_ledd_siden
    to_ledd_siden = forrige_ledd
    forrige_ledd = ledd
    print(ledd)

#%%


def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for n in range(1, antall_ledd + 1):
    print(fibonacci(n))

#%%


fibonacci = [1, 1]
for n in range(3, antall_ledd + 1):
    fibonacci.append(sum(fibonacci[-2:]))
print(fibonacci)


#%%
# legge sammen en uendelig rekke med a_n = (1/2)^n

import matplotlib.pyplot as plt

antall_ledd = 10

min_sum = 0
x = []
y = []
for i in range(1, antall_ledd + 1):
    x.append(i)
    min_sum = min_sum + (1 / 2) ** i
    y.append(min_sum)

print(min_sum)
plt.plot(x, y)

#%%
# eksempel s. 14
min_sum = 0
for n in range(1, 101):
    min_sum += 2 * n - 1
print(min_sum)
