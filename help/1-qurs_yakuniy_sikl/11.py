a,b,x=list(map(int,input().split()))
s = 0
for i in range(10,20):s+=((a*x+b)**i)**0.5
print(s)
