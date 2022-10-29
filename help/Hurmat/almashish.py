massiv = list(map(str,input('malumotlarni probel bilan ajratgan holda kiritin>>').split()))
i1 = int(input('1 - element indexini kiriting>>'))-1
i2 = int(input('2 - element indexini kiriting>>'))-1
massiv[i1],massiv[i2]=massiv[i2],massiv[i1]
for i in massiv:print(i)