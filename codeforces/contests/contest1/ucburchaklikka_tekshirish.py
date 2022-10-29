"""a,b,c = int(input()),int(input()),int(input())
n = 0
while a!=0 and b!=0 and c!=0:
    if ((a+b)>c) and ((a+c)>b) and ((c+b)>a):
        n+=1
        a-=1
        b-=1
        c-=1
    else:
        print(n)
        break"""

a = int(input())
b = int(input())
c = int(input())

a, b, c = min(a, b, c), a + b + c - min(a, b, c) - max(a, b, c), max(a, b, c)

ans = 0
step = 10 ** 9

while step > 1:
    while a - ans + b - ans > c - ans:
        ans += step
        ans -= 2 * step
        step //= 10
        while a - ans + b - ans > c - ans:
            ans += step

print(ans)