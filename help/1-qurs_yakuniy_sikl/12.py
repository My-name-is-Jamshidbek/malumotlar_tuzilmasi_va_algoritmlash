import math
c,x=list(map(int,input().split()))
p = 1
for a in range(1,6):p*=(a*x+c)/math.sin(a*x)**2
print(p)
