n = int(input())
m1 = list(map(int,input().split()))[:n]
n = int(input())
m2 = list(map(int,input().split()))[:n]
x= int(input())
n=0
for i1 in m1:
    for i2 in m2:
        if i1+i2==x:
            n+=1
print(n)