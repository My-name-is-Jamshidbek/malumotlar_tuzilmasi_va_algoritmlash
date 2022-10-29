b,x=list(map(int,input().split()))
p = 1
for a in range(10,25):p*=(a+b)/((a**2)+x**2)**0.5
print(p)
