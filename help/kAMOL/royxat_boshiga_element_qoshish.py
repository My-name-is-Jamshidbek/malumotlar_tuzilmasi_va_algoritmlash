n = int(input('royxat uzunligi>>'))
m = list(map(int,input('royxat elememtlarini probel bilan ajratgan holda kiriting>>').split()))[:n]
x = int(input('royxat boshiga qoshiladgan element>>'))
m.insert(0,x)
print('royxat elementlari:')
for i in m:print(i,end=' ')