b,x=list(map(int,input().split()))
p = 1
for a in range(3,10):p*=(a*x+b)/((a**2)+b**2)**0.5
print(p)
