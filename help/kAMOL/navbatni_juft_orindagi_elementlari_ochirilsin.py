n = int(input('avbat uzunligi>>'))
m = list(map(int,input('navbat elementlarini probel bilan ajratgan holda kiriting>>').split()))[:n]
n1 = 1
while n1<=n/2:
    m.pop(n1)
    n1+=1
print(m)