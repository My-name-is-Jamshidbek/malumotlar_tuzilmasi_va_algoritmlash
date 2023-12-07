# 2.	Bir o`lchamli sonli massiv  [a,b] qismidagi elementlari massivni eng kichik elementiga bo`lib chiqilsin

uzunligi = int(input("Massiv uzunligi>>"))
massiv = []
for i in range(uzunligi):
    son = int(input(f"{i+1} - son>>"))
    massiv.append(son)
a = int(input("a son>>"))
b = int(input("b son>>"))

_min = massiv[0]
for i in massiv:
    if i < _min:
        _min = i

for i in range(a-1, b-1):
    massiv[i] /= _min

for i in massiv:
    print(f"{i} ")