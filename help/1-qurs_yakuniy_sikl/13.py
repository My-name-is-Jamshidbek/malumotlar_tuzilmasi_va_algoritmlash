import math

b,x=list(map(int,input().split()))
p = 1
for a in range(3,9):p*=math.cos(a*b)+a*x
print(p)
