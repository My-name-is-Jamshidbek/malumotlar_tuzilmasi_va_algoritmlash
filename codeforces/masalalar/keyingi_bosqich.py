n,m=list(map(int,input().split())),list(map(int,input().split()))
n1 = 0
n = m[n[1]-1]
t=True
q = m[0]
for i in m:
    if q!=i:t=False
    if i>=n:n1+=1
if n==0:print(0)
elif t:print('1')
else:print(n1)
