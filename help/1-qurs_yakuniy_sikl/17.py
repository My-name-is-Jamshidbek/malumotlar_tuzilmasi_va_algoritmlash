import math

s = 0
for a in range(1,27):s+=(a**2+2*a)/(a**3+a*math.cos(a+1)**2)
print(s)
