n,m = int(input()),int(input())
n1 = 0
d = 1
while d<(n+1):
    a = 1
    i = 1
    u = 0
    while (a+(2*d))<=m:
        print(a)
        u+=1
        a+=d
        i+=1
        if (a+(2*d)) == m:
            n1+=u
    d+=1
print(n1)

