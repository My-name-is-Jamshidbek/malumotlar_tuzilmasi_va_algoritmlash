b,c,x=list(map(int,input().split()))
s = 0
for a in range(5,13):s+=(a*x+b*c)/(a**2+x)
print(s)
