import numpy as np
m1 = input()
m2 = input()
i = 0
l = len(m1)
while l>i:
    if (m1[i]!=m2[i]):print(1,end='')
    else:print(0,end='')
    i += 1
