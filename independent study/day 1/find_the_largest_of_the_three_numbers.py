#1-step: Start
#2-step: Enter a,b and c
#3-step: a>b
#           a>c return a
#           return c
#        b>a return b
#        return c
#4-step: Stop

def func(a,b,c):
    if a>b:
        if a>c:return a
        return c
    if b>a:return b
    return c
