a_0 = 0
a_1 = 1
a_2 = 3
a_3 = 4

a_minus1 = 4
a_minus2 = 3
a_minus3 = 1
a_minus4 = 0

a = a_minus1

for i in range(1,11):
    a = a*2 - a_minus4
    a_minus4 = a_minus3
    a_minus3 = a_minus2
    a_minus2 = a_minus1
    a_minus1 = a
    print(a)
