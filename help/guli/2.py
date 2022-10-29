def f(a,b):
    if a!=0 and b!=0:
        if a>b:return f(a=a%b,b=b)
        else:return f(a=a,b=b%a)
    else:return a+b
print(f(30,18))