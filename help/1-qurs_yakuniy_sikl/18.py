import math

p = 1
for n in range(1,17):p*=math.cos((n+n**0.5)/(n-n**0.2))**2
print(p)
