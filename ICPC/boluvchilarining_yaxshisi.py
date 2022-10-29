n = int(input())
m = 0
mn = 0
def ry(n,m=0):
    if n<10:return m+n
    else:return ry(n=n//10,m=m+(n%10))
for i in range(2,n):
    if n%i == 0:
        print(n)
        print(ry(n))
        if mn < ry(n):
            mn = ry(n)
            m = n
print(m)