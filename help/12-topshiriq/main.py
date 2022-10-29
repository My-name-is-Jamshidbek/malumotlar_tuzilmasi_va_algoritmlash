n,m=list(map(int,input().split()))
n_mass = list(map(int,input().split()))[:n]
m_mass = list(map(int,input().split()))[:m]
j = 0
for i in m_mass:
    for i1 in n_mass:
        if i1<=i:j+=1
print(j)
