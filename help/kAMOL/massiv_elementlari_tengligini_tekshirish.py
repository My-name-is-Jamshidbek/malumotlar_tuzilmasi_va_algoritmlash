def f(m):
    n = m[0]
    for i in range(1,len(m)):
        if n!=m[i]:return False
        n = m[i]
    return True
print(f([5,5,5,5,5]))

m = list(map(int,input('massiv elementlarini probel bilan ajratgan holda kiriting>>').split()))  #massivni qabul qilish
mn = []  #bosh massiv
for i in m:mn.append(i)  #nusxalash
for i in mn:print(i)   #ekranga chiqarish