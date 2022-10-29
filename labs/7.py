n = int(input('royxat uzunligi>>'))
m = list(map(int,input('royxat elementlarini probel bilan ajratgan holda kiriting>>').split()))[:n]
n1 = 1
while n1<=n/2:
    m.pop(n1)
    n1+=1
print(m)