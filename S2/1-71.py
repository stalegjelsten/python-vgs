#%%


def geometrisk_sum(a_1, k, stopp):
    ledd = a_1
    minsum = a_1
    while round(ledd, 0) != stopp:
        ledd = ledd * k
        minsum += ledd
    return minsum


# #a) 1+3+9+27. Ser at k = 3
print(f"a) {geometrisk_sum(1,3,19683)}")

# b) 384 - 192 + 96 - ... Ser at k = -1/2
print(f"b) {geometrisk_sum(384, -0.5, -3)}")

# c) 5 + 10 + 20 + ... + 5120. Ser ut til at k = 2
print(f"c) {geometrisk_sum(5, 2, 5120)}")

# d) 50 + 50 * 1.05 + 50*1.09^1o9
# print(f"c) {geometrisk_sum(50, 1.05, 50*1.05**19)}")
# %%
