p = 1
for m in range(0,12):p*=((abs(m-5)+1)**0.5)/(m**3+4*m+(-1)**3)
print(p)
