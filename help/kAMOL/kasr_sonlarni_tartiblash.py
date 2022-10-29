n = int(input())
m = []
for i in range(n):
    n1,n2=list(map(int,input().split()))
    t=True
    for i in range(len(m)):
        if float(m[i][0]/m[i][1])>float(n1/n2):
            m.insert(i,[n1,n2])
            t=False
            break
    if t:m.append([n1,n2])


print(m)
