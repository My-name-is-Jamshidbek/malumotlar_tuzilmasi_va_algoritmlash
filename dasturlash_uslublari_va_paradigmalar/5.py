def massiv_matritsa(d_massiv):return [d_massiv[i:i+4] for i in range(0, len(d_massiv), 4)]
print(massiv_matritsa([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))

# def massiv_matritsa(d_massiv):
#     matritsa = [d_massiv[i:i+4] for i in range(0, len(d_massiv), 4)]
#     return matritsa

# d_massiv = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# matritsa = massiv_matritsa(d_massiv)
# print(matritsa)
