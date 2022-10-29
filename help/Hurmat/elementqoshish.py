massiv = list(map(str,input('malumotlarni probel bilan ajratgan holda kiritin>>').split()))
i1 = int(input('element qoshiladigan indexni kiriting>>'))-1
i2 = str(input('elementni kiriting>>'))
massiv.insert(i1,i2)
for i in massiv:print(i)