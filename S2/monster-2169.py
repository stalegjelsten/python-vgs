#%%
def f(x):
    return x**2 + 1


a = 0
b = 2
n = 10
delta_x = (b - a) / n

x = a
areal = 0

for i in range(n):
    # rektangel = f(x) * delta_x
    # areal = areal + rektangel
    trapes = (f(x) + f(x + delta_x))/2 * delta_x
    areal = areal + trapes
    x = x + delta_x

# %%
