e=list(map(int,input().split()))
p = 0
for i in range(1,19):p+=(3+(i**4)+i**2)/(i+e**i)**0.5
print(p)
