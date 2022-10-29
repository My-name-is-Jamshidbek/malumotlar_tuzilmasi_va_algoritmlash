def f(n):
    n = str(n)
    m = 0
    for i in n:
        m+=int(i)
    return m
def f1(x):
    return (x**2)+f(x)*x
a = int(input())
for i in range(a):
    if f1(i) == a:print(i)
