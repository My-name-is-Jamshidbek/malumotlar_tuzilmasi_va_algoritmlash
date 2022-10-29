massiv = list(map(int,input('Massiv elementlarini probel bilan ajratgan holda kiriting>>').split()))
kvadrat_yigindisi = 0
elementlar_soni = 0
elementlar_yigindisi = 0
for i in massiv:
    kvadrat_yigindisi+=i**2
    elementlar_soni+=1
    elementlar_yigindisi+=i
print(f"Kvadratlar yig`indisi>> {kvadrat_yigindisi}")
print(f"Ortacha qiymati>> {elementlar_yigindisi/elementlar_soni}")
