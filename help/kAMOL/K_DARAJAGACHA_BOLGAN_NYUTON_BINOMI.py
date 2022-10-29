import math
def f(n):
    m1=[]
    for n in range(n):
        m = []
        for k in range(n+1):
            m.append(int(math.factorial(n)/(math.factorial(k)*(math.factorial(n-k)))))
        m1.append(m[int(len(m)/2)])
    return m1
print(f(5))