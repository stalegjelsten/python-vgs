# %%

import math


n = 10
k = 2
pos = 1


overlevende = list(range(1, n + 1))

while len(overlevende) > 1:
    print(overlevende)
    overlevende.remove(pos)
    pos += 1


print(overlevende)
# while n > 1:
#    print(f"Personen i posisjon {pos+k-1}")

# %%

n = 10
k = 2
pos = 1


overlevende = list(range(1, n + 1))
print(overlevende)


while len(overlevende) > 1:
    pos = pos + k
    pos = pos % len(overlevende)
    overlevende.pop(pos - 2)
    pos = pos - 1
    print(pos, overlevende)


print(overlevende)
# while n > 1:
#    print(f"Personen i posisjon {pos+k-1}")

# %%

n = 10
k = 2
pos = 0
overlevende = n * [1]
print(overlevende)
s = 0

while sum(overlevende) > 2 and s < 10:
    pos = pos + k
    pos = pos % n
    overlevende[pos - 1] = 0
    print(overlevende)

    s += 1

if sum(overlevende) == 2:
    print(f"Vinneren er {posisjon_til_første_overlevende}")

# %%
pos = 1
for i in range(2, n + 1):
    pos = (pos + k - 1) % i + 1

print(pos)

# n = 2 => 1
# n = 3 => 3
# n = 4 => 1
# n = 5 => 1
# n = 6 => 1
# n = 6 => 1

# %%

n = 10
k = 2
pos = 1

for i in range(2, n + 1):
    pos = pos + k
    pos = pos % i
    if pos % 2 == 0:
        pos = pos - 1

    print(pos)
    pos = 1

# %%
# forsøk med å endre k
n = 41
k = 2
pos = 1
antall_drept = 0
while antall_drept < n - 1:
    last_pos = pos
    if pos == n:
        pos = k
    pos = (pos + k) % (n + 1)

    if pos < last_pos:
        k = k + 1
    if pos == 0:
        pos = 1
    print(pos)
    antall_drept += 1
print(pos + 1)
