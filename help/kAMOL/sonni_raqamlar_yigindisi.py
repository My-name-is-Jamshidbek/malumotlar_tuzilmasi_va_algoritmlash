def f(raqam,n=0):
    """
    :param raqam: type str min len = 1
    :param n: type int value 0
    :return: type int raqamlar yig'indisi
    """
    if len(raqam) == 1:return n+int(raqam)
    else:return f(raqam[1:],n=n+int(raqam[0]))

import math
a,b,x = list(map(int,input().split()))
j=0
if a*b!=0:
    j = ((((a**2)+(b**2))**0.3)+(2*x**3))/((3*a*b)-x)
elif x*2>a*b:
    j = (((x**2)-2*a*b)**0.5)/((((x**2)-2*a*b)**0.5)/((a**2)+(b**2)+(2*a*b*math.sin(x))))
else:
    j=0
