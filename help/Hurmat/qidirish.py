massiv = list(map(str,input('malumotlarni probel bilan ajratgan holda kiritin>>').split()))
n = str(input('qidirilayotgan malumotni kiriting>>'))
n1 = 0
for i in massiv:
    if i==n:
        print(n1)
        break
    n1 += 1
