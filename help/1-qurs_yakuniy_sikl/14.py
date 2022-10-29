b,x=list(map(int,input().split()))
p = 1
for a in range(3,12):p*=((a*x**2+b)/(2*a))**0.3
print(p)
