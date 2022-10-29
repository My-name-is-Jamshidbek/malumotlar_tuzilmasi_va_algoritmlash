m,n,s = list(map(int,input().split()))
n= n-m
for i in range(s-1):
    m+=n
print(m)