import math

a, b, c = map(int, input().split())
s = 1
for k in range(1, 18):
    s = s * ((a * k**2 + c**3) / (math.pow(b * k**2 + 7,1/3)))

g = 0
for z in range(5, 20):
    z = z + ((a * z + b) / (math.pow(z**2 + 8,1/5)))

P = math.pow((a * b),1/3) * s + (a / b) * z
print(P)