b,x=list(map(int,input().split()))
s = 0
for a in range(1,7):s+=(a*x+b)/(a+b)**0.5
print(s)
