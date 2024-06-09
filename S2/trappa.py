# Gå opp en trapp med n trinn. Du kan enten gå 1 eller 2 trinn om gangen.
# Hvor mange ulike måter kan du gå opp trappa?

n = 15

a = 1
b = 1

for i in range(n):
    c = a + b
    a = b
    b = c
    print(c)
