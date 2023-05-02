import math
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if d > 0:
    for i in range(d+1):
        S = a*i*i*i + b*i*i + c*i + d
        if S == 0: print(i)
    for j in range(0, -1*d, -1):
        S = a*j*j*j + b*j*j + c*j + d
        if S == 0: print(j)
else:
    for i in range(-1*d+1):
        S = a*i*i*i + b*i*i + c*i + d
        if S == 0: print(i)
for j in range(0, d, -1):
    S = a*j*j*j + b*j*j + c*j + d
    if S == 0: print(j)
