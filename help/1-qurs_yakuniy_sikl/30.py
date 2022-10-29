import math

s = 0
for i in range(1,81):s+=(i+2**i+7)/(i**2-1+math.cos(i)**2)
print(s)
