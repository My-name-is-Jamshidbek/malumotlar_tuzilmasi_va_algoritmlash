def f(n,a,m=1):
    if a:return f(m=m*n,n=n,a=a-1)
    else: return m
print(f(4,1))
