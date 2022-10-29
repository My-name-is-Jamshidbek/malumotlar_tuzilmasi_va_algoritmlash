k = int(input('K ni kiriting>>'))-1
i = int(input('I ni kiriting>>'))-1
massiv = list(map(int,input('Massiv elementlarini probel bilan ajratgan holda kiriting>>').split()))
kelement = massiv[k]
massiv[k] = massiv[i]
massiv[i] = kelement
for i in massiv:print(i,end=' ')